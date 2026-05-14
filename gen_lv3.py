"""
gen_lv3.py
==========
동 단위(Level 3) index.html에 NEIS API 학원 데이터로
'해당 지역 인기학원 모음' 섹션을 삽입/업데이트합니다.

규칙:
  - 교습과정목록명에 수학/영어/국어 중 하나 포함
  - 등록상태 = 개원만
  - 수강료 있는 것만
  - 학원명 6글자 이상 겹치면 중복 제거
  - 수학→영어→국어 순환, 총 16개
  - 동 매칭: FA_RDNDA 필드의 괄호 안 첫 토큰에 폴더명이 포함되는 것만
    예) FA_RDNDA = "경기 고양시 일산서구 강촌로X (마두동)" → "마두동" 추출
  - 5개 미만이면 미분류.txt에 기록 (도<TAB>시구<TAB>동)
  - 삽입 위치: <main> 안 첫 번째 </section> 바로 뒤
"""

import os, re, json, time, random
import urllib.request, urllib.parse
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE     = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
NEIS_KEY = '1e15a9adec0647c4a5d52cfc2c5cc9fe'
NEIS_URL = 'https://open.neis.go.kr/hub/acaInsTiInfo'
UNCLASSIFIED = os.path.join(BASE, '미분류.txt')

DO_CODE = {
    '서울특별시':     'B10',
    '부산광역시':     'C10',
    '대구광역시':     'D10',
    '인천광역시':     'E10',
    '광주광역시':     'F10',
    '대전광역시':     'G10',
    '울산광역시':     'H10',
    '세종시':         'I10',
    '경기도':         'J10',
    '강원도':         'K10',
    '충청북도':       'M10',
    '충청남도':       'N10',
    '전북특별자치도': 'P10',
    '경상북도':       'R10',
    '경상남도':       'S10',
    '제주도':         'T10',
}

# 시 이름이 API 행정구역명과 다를 때 매핑 (여러 구를 합산 조회)
SI_ZONE_MAP = {
    '청주시': ['상당구', '서원구', '청원구', '흥덕구'],
    '세종':   ['세종특별자치시'],
}

CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
IMGS = [
    f'{CLOUDINARY_BASE}/v1778659603/1_w3frn8.webp',
    f'{CLOUDINARY_BASE}/v1778659605/2_qasyxi.webp',
    f'{CLOUDINARY_BASE}/v1778659602/3_tbgizh.webp',
    f'{CLOUDINARY_BASE}/v1778659605/4_p7olqt.webp',
    f'{CLOUDINARY_BASE}/v1778659604/5_sk7t7e.webp',
    f'{CLOUDINARY_BASE}/v1778659605/6_outenk.webp',
    f'{CLOUDINARY_BASE}/v1778659604/7_s5oz3w.webp',
    f'{CLOUDINARY_BASE}/v1778659605/8_wmax55.webp',
    f'{CLOUDINARY_BASE}/v1778659605/9_cfwxso.webp',
    f'{CLOUDINARY_BASE}/v1778659603/10_qsoaya.webp',
    f'{CLOUDINARY_BASE}/v1778659609/11_ix4mpp.webp',
    f'{CLOUDINARY_BASE}/v1778659603/12_pi4we3.webp',
    f'{CLOUDINARY_BASE}/v1778659603/13_u9t1h3.webp',
    f'{CLOUDINARY_BASE}/v1778659605/14_reqxkg.webp',
    f'{CLOUDINARY_BASE}/v1778659604/15_hrfepx.webp',
    f'{CLOUDINARY_BASE}/v1778659604/16_kshki1.webp',
]

# API 결과 캐시: (do_code, si_name) -> all_rows
_api_cache = {}


def fetch_all_rows(code, si_name):
    """시/구 단위 전체 학원 rows 조회 (캐시 활용)"""
    cache_key = (code, si_name)
    if cache_key in _api_cache:
        return _api_cache[cache_key]

    zones = SI_ZONE_MAP.get(si_name, [si_name] if si_name else [None])
    all_rows = []
    for zone in zones:
        params = {
            'KEY':  NEIS_KEY,
            'Type': 'json',
            'pIndex': 1,
            'pSize': 500,
            'ATPT_OFCDC_SC_CODE': code,
        }
        if zone:
            params['ADMST_ZONE_NM'] = zone
        try:
            with urllib.request.urlopen(
                f'{NEIS_URL}?{urllib.parse.urlencode(params)}', timeout=20
            ) as r:
                data = json.loads(r.read().decode('utf-8'))
            rows = data.get('acaInsTiInfo', [{}, {}])
            if len(rows) >= 2:
                all_rows += rows[1].get('row', [])
        except Exception as e:
            print(f'  API 오류 ({zone}): {e}')
        if len(zones) > 1:
            time.sleep(0.2)

    _api_cache[cache_key] = all_rows
    return all_rows


def extract_dong_from_rdnda(fa_rdnda):
    """FA_RDNDA에서 괄호 안 첫 번째 토큰 추출. 예: '(마두동, 201호)' -> '마두동'"""
    if not fa_rdnda:
        return ''
    m = re.search(r'\(([^,)]+)', fa_rdnda)
    if m:
        return m.group(1).strip()
    return ''


def is_duplicate(name, selected_names, min_len=6):
    for existing in selected_names:
        for i in range(len(name) - min_len + 1):
            if name[i:i + min_len] in existing:
                return True
    return False


def filter_by_dong(all_rows, dong_folder, count=16):
    """
    all_rows에서 dong_folder에 해당하는 학원만 선별.
    dong_folder=None 이면 동 필터 없이 시/구 전체에서 선별 (미분류 폴백용).
    """
    buckets = {'수학': [], '영어': [], '국어': []}
    selected_names = []

    for row in all_rows:
        if row.get('REG_STTUS_NM') != '개원':
            continue
        crse = row.get('LE_CRSE_LIST_NM') or row.get('LE_CRSE_NM') or ''
        fee_raw = row.get('PSNBY_THCC_CNTNT', '')
        if not fee_raw or not fee_raw.strip():
            continue
        name = row.get('ACA_NM', '')
        if is_duplicate(name, selected_names):
            continue

        # 동 매칭 (dong_folder=None 이면 건너뜀 → 시/구 전체 사용)
        if dong_folder is not None:
            fa_rdnda = row.get('FA_RDNDA', '') or ''
            dong_in_addr = extract_dong_from_rdnda(fa_rdnda)
            if not dong_in_addr:
                continue
            if dong_folder not in dong_in_addr:
                continue

        for kw in ['수학', '영어', '국어']:
            if kw in crse and len(buckets[kw]) < count:
                buckets[kw].append(row)
                selected_names.append(name)
                break

    result = []
    iters = {kw: iter(buckets[kw]) for kw in ['수학', '영어', '국어']}
    while len(result) < count:
        added = False
        for kw in ['수학', '영어', '국어']:
            if len(result) >= count:
                break
            row = next(iters[kw], None)
            if row:
                result.append(row)
                added = True
        if not added:
            break
    return result


def tag_class(crse):
    if '수학' in crse: return 'academy-tag-math'
    if '영어' in crse: return 'academy-tag-eng'
    if '국어' in crse: return 'academy-tag-kor'
    return 'academy-tag-etc'


def tag_label(crse):
    if '수학' in crse: return '수학'
    if '영어' in crse: return '영어'
    if '국어' in crse: return '국어'
    return crse[:6]


def format_fee(raw):
    if not raw or not raw.strip():
        return '수강료 정보 준비 중'
    parts = [p.strip() for p in raw.split(',')][:2]
    out = []
    for p in parts:
        if ':' in p:
            name, amt = p.rsplit(':', 1)
            try:
                out.append(f'{name.strip()} {int(amt.strip()):,}원')
            except ValueError:
                out.append(p)
        else:
            out.append(p)
    return ' | '.join(out)


def parse_fee_offers(raw):
    """PSNBY_THCC_CNTNT → Offer 리스트 [{"name":..., "price":...}, ...]"""
    if not raw or not raw.strip():
        return []
    offers = []
    for part in raw.split(','):
        part = part.strip()
        if ':' in part:
            name, amt = part.rsplit(':', 1)
            try:
                offers.append({'name': name.strip(), 'price': str(int(amt.strip()))})
            except ValueError:
                pass
    return offers


def academy_img_url(name, base_img_url):
    encoded = urllib.parse.quote(f'{name} 내부', safe='')
    upload_idx = base_img_url.find('/upload/') + len('/upload/')
    rest = base_img_url[upload_idx:]
    base = base_img_url[:upload_idx]
    return (
        f'{base}w_740,h_400,c_fill,q_auto,f_auto/'
        f'l_text:NanumGothic_28_bold:{encoded},'
        f'co_white,g_south_west,x_16,y_12,b_rgb:00000055/{rest}'
    )


def make_section(academies, area_name):
    imgs = IMGS.copy()
    random.shuffle(imgs)

    cards = []
    jsonld_items = []

    for i, row in enumerate(academies):
        name   = row.get('ACA_NM', '')
        img    = academy_img_url(name, imgs[i % len(imgs)])
        num    = row.get('ACA_ASNUM', '')
        crse   = row.get('LE_CRSE_LIST_NM') or row.get('LE_CRSE_NM') or ''
        fee    = format_fee(row.get('PSNBY_THCC_CNTNT', ''))
        addr   = row.get('FA_RDNMA', '')
        detail = (row.get('FA_RDNDA') or '').strip()
        if detail:
            addr = f'{addr} {detail}'

        cards.append(f'''
            <article class="academy-card">
              <img src="{img}" alt="{area_name} {name} 내부" class="academy-card-img" loading="lazy" width="740" height="400">
              <div class="academy-card-body">
                <h3 class="academy-card-name">{name}</h3>
                <p class="academy-card-num">학원지정번호 {num}</p>
                <div class="academy-card-tags"><span class="{tag_class(crse)}">{tag_label(crse)}</span></div>
                <p class="academy-card-fee">{fee}</p>
                <p class="academy-card-addr">{addr}</p>
              </div>
            </article>''')

        offers = parse_fee_offers(row.get('PSNBY_THCC_CNTNT', ''))
        item = {
            '@type': 'EducationalOrganization',
            'name': name,
            'identifier': num,
            'address': {
                '@type': 'PostalAddress',
                'streetAddress': addr,
                'addressLocality': area_name,
                'addressCountry': 'KR'
            }
        }
        if offers:
            item['hasOfferCatalog'] = {
                '@type': 'OfferCatalog',
                'name': '수강료',
                'itemListElement': [
                    {
                        '@type': 'Offer',
                        'name': o['name'],
                        'price': o['price'],
                        'priceCurrency': 'KRW'
                    } for o in offers
                ]
            }
        jsonld_items.append({
            '@type': 'ListItem',
            'position': i + 1,
            'item': item
        })

    jsonld = json.dumps({
        '@context': 'https://schema.org',
        '@type': 'ItemList',
        'name': f'{area_name} 인기학원 모음',
        'itemListElement': jsonld_items
    }, ensure_ascii=False, indent=2)

    cards_html = ''.join(cards)
    return (
        '      <!-- ACADEMY_SECTION_START -->\n'
        '      <section class="section">\n'
        '        <div class="container">\n'
        f'          <h2 class="section-title">해당 지역 인기학원 모음</h2>\n'
        f'          <p class="section-desc">{area_name} 수학·영어·국어 학원 {len(academies)}곳을 모았습니다.</p>\n'
        '          <div class="academy-grid">'
        f'{cards_html}\n'
        '          </div>\n'
        '        </div>\n'
        '      </section>\n'
        f'      <script type="application/ld+json">\n{jsonld}\n      </script>\n'
        '      <!-- ACADEMY_SECTION_END -->'
    )


def insert_or_replace(html, section):
    # 이미 삽입된 섹션이면 교체
    if '<!-- ACADEMY_SECTION_START -->' in html:
        return re.sub(
            r'      <!-- ACADEMY_SECTION_START -->.*?<!-- ACADEMY_SECTION_END -->',
            section,
            html,
            flags=re.DOTALL
        )
    # <main> 안 첫 번째 </section> 뒤에 삽입
    main_idx = html.find('<main>')
    if main_idx == -1:
        return html
    pos = html.find('</section>', main_idx)
    if pos == -1:
        return html
    pos += len('</section>')
    return html[:pos] + '\n\n' + section + html[pos:]


# ── 미분류 기록 ──────────────────────────────────────────────────────────
unclassified_lines = []

# ── 실행 ──────────────────────────────────────────────────────────────
total = 0
done  = 0
skip  = 0
unclassified_count = 0

for do, code in DO_CODE.items():
    do_path = os.path.join(BASE, do)
    if not os.path.isdir(do_path):
        continue
    for si in sorted(os.listdir(do_path)):
        si_path = os.path.join(do_path, si)
        if not os.path.isdir(si_path):
            continue
        for dong in sorted(os.listdir(si_path)):
            dong_path = os.path.join(si_path, dong)
            html_path = os.path.join(dong_path, 'index.html')
            if not os.path.isfile(html_path):
                continue

            total += 1
            print(f'[{do} / {si} / {dong}]', end=' ... ', flush=True)

            try:
                all_rows = fetch_all_rows(code, si)
                academies = filter_by_dong(all_rows, dong)

                if len(academies) < 5:
                    # 폴백: 동 필터 없이 시/구 전체 데이터로 채움
                    academies = filter_by_dong(all_rows, None)
                    if len(academies) < 5:
                        print(f'미분류 ({len(academies)}개) — 시/구도 부족')
                        unclassified_lines.append(f'{do}\t{si}\t{dong}')
                        unclassified_count += 1
                        skip += 1
                        continue
                    print(f'폴백(시/구) ', end='', flush=True)

                section = make_section(academies, dong)
                with open(html_path, encoding='utf-8') as f:
                    html = f.read()
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(insert_or_replace(html, section))
                print(f'{len(academies)}개 삽입')
                done += 1
                time.sleep(0.1)

            except Exception as e:
                print(f'오류: {e}')
                skip += 1

# 미분류 기록
if unclassified_lines:
    with open(UNCLASSIFIED, 'w', encoding='utf-8') as f:
        f.write('도\t시구\t동\n')
        f.write('\n'.join(unclassified_lines) + '\n')
    print(f'\n미분류.txt 저장: {unclassified_count}개')

print(f'\n완료 - 삽입: {done}개 / 미분류: {unclassified_count}개 / 건너뜀: {skip - unclassified_count}개 / 전체: {total}개')
