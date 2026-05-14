"""
gen_academy_cards.py
====================
레벨1(도) 및 레벨2(시/구) index.html에 NEIS API 학원 데이터로
'해당 지역 인기학원 모음' 섹션을 삽입/업데이트합니다.

실행 모드 (MODE 변수):
  'lv1' — 도 단위 16개 파일
  'lv2' — 시/구 단위 파일 전체

규칙:
  - 교습과정목록명에 수학/영어/국어 중 하나 포함
  - 등록상태 = 개원만
  - 수강료 있는 것만
  - 학원명 6글자 이상 겹치면 중복 제거
  - 수학→영어→국어 순환, 총 16개
"""

import os, re, json, time, random
import urllib.request, urllib.parse

# ── 실행 모드 설정 ──────────────────────────────────────────────────────
MODE = 'lv2'   # 'lv1' 또는 'lv2'

BASE     = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
NEIS_KEY = '1e15a9adec0647c4a5d52cfc2c5cc9fe'
NEIS_URL = 'https://open.neis.go.kr/hub/acaInsTiInfo'

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


def is_duplicate(name, selected_names, min_len=6):
    for existing in selected_names:
        for i in range(len(name) - min_len + 1):
            if name[i:i + min_len] in existing:
                return True
    return False


# 시 이름이 API 행정구역명과 다를 때 매핑 (여러 구를 합산 조회)
SI_ZONE_MAP = {
    '청주시': ['청주시', '상당구', '서원구', '청원구', '흥덕구'],
}


def fetch_academies(code, si_name=None, count=16):
    # 다중 구역 조회 (예: 청주시 → 4개 구 합산)
    zones = SI_ZONE_MAP.get(si_name, [si_name] if si_name else [None])

    all_rows = []
    for zone in zones:
        params = {
            'KEY': NEIS_KEY,
            'Type': 'json',
            'pIndex': 1,
            'pSize': 500,
            'ATPT_OFCDC_SC_CODE': code,
        }
        if zone:
            params['ADMST_ZONE_NM'] = zone
        with urllib.request.urlopen(
            f'{NEIS_URL}?{urllib.parse.urlencode(params)}', timeout=20
        ) as r:
            data = json.loads(r.read().decode('utf-8'))
        rows = data.get('acaInsTiInfo', [{}, {}])
        if len(rows) >= 2:
            all_rows += rows[1].get('row', [])
        if len(zones) > 1:
            time.sleep(0.2)

    rows = all_rows

    buckets = {'수학': [], '영어': [], '국어': []}
    selected_names = []

    for row in rows:
        if row.get('REG_STTUS_NM') != '개원':
            continue
        crse = row.get('LE_CRSE_LIST_NM') or row.get('LE_CRSE_NM') or ''
        fee_raw = row.get('PSNBY_THCC_CNTNT', '')
        if not fee_raw or not fee_raw.strip():
            continue
        name = row.get('ACA_NM', '')
        if is_duplicate(name, selected_names):
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
        name  = row.get('ACA_NM', '')
        img   = academy_img_url(name, imgs[i % len(imgs)])
        num   = row.get('ACA_ASNUM', '')
        crse  = row.get('LE_CRSE_LIST_NM') or row.get('LE_CRSE_NM') or ''
        fee   = format_fee(row.get('PSNBY_THCC_CNTNT', ''))
        addr  = row.get('FA_RDNMA', '')
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
    if '<!-- ACADEMY_SECTION_START -->' in html:
        return re.sub(
            r'      <!-- ACADEMY_SECTION_START -->.*?<!-- ACADEMY_SECTION_END -->',
            section,
            html,
            flags=re.DOTALL
        )
    if '해당 지역 인기학원 모음' in html:
        html = re.sub(
            r'\s*<section class="section">\s*<div class="container">\s*<h2[^>]*>해당 지역 인기학원 모음</h2>.*?</section>',
            '',
            html,
            flags=re.DOTALL
        )
    main_idx = html.find('<main>')
    if main_idx == -1:
        return html
    pos = html.find('</section>', main_idx)
    if pos == -1:
        return html
    pos += len('</section>')
    return html[:pos] + '\n\n' + section + html[pos:]


def process(path, area_name, code, si_name=None):
    print(f'처리 중: {area_name}', end=' ... ', flush=True)
    try:
        academies = fetch_academies(code, si_name)
        if not academies:
            print('학원 데이터 없음, 건너뜀')
            return
        section = make_section(academies, area_name)
        with open(path, encoding='utf-8') as f:
            html = f.read()
        with open(path, 'w', encoding='utf-8') as f:
            f.write(insert_or_replace(html, section))
        print(f'{len(academies)}개 삽입 완료')
        time.sleep(0.3)
    except Exception as e:
        print(f'오류: {e}')


# ── 실행 ──────────────────────────────────────────────────────────────
if MODE == 'lv1':
    for do, code in DO_CODE.items():
        path = os.path.join(BASE, do, 'index.html')
        if not os.path.exists(path):
            print(f'건너뜀 (파일 없음): {do}')
            continue
        process(path, do, code)

elif MODE == 'lv2':
    for do, code in DO_CODE.items():
        do_path = os.path.join(BASE, do)
        if not os.path.isdir(do_path):
            continue
        for si in sorted(os.listdir(do_path)):
            path = os.path.join(do_path, si, 'index.html')
            if not os.path.exists(path):
                continue
            process(path, si, code, si_name=si)

print('\n완료')
