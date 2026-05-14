"""
gen_root_section.py
===================
루트 index.html에 '전국 베스트 학원모음' 섹션을 삽입/업데이트합니다.

규칙:
  - 전국 각 지역에서 골고루 학원 수집
  - 국어→영어→수학 순환, 총 16개
  - 교습과정목록명에 국어/영어/수학 중 하나 포함
  - 등록상태 = 개원만
  - 수강료 있는 것만
  - 학원명 6글자 이상 겹치면 중복 제거
  - 삽입 위치: <!-- H2 ③ 학부모님 고민거리 --> 바로 앞
"""

import os, re, json, time, random
import urllib.request, urllib.parse
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE     = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
ROOT_HTML = os.path.join(BASE, 'index.html')
NEIS_KEY = '1e15a9adec0647c4a5d52cfc2c5cc9fe'
NEIS_URL = 'https://open.neis.go.kr/hub/acaInsTiInfo'

# 전국 각 지역 코드 + 대표 시구 (다양성을 위해 여러 지역에서 수집)
REGIONS = [
    ('서울특별시', 'B10', '강남구'),
    ('서울특별시', 'B10', '노원구'),
    ('경기도',     'J10', '수원시'),
    ('경기도',     'J10', '성남시'),
    ('부산광역시', 'C10', '해운대구'),
    ('대구광역시', 'D10', '수성구'),
    ('인천광역시', 'E10', '남동구'),
    ('광주광역시', 'F10', '북구'),
    ('대전광역시', 'G10', '서구'),
    ('경상남도',   'S10', '창원시'),
]

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


def fetch_rows(code, si_name):
    params = {
        'KEY':  NEIS_KEY,
        'Type': 'json',
        'pIndex': 1,
        'pSize': 500,
        'ATPT_OFCDC_SC_CODE': code,
        'ADMST_ZONE_NM': si_name,
    }
    try:
        with urllib.request.urlopen(
            f'{NEIS_URL}?{urllib.parse.urlencode(params)}', timeout=20
        ) as r:
            data = json.loads(r.read().decode('utf-8'))
        rows = data.get('acaInsTiInfo', [{}, {}])
        if len(rows) >= 2:
            return rows[1].get('row', [])
    except Exception as e:
        print(f'  API 오류 ({si_name}): {e}')
    return []


def is_duplicate(name, selected_names, min_len=6):
    for existing in selected_names:
        for i in range(len(name) - min_len + 1):
            if name[i:i + min_len] in existing:
                return True
    return False


def collect_nationwide(count=16):
    """전국 각 지역에서 국어/영어/수학 학원 수집 후 국어→영어→수학 순환으로 16개 선별"""
    buckets = {'국어': [], '영어': [], '수학': []}
    selected_names = []

    for do_name, code, si_name in REGIONS:
        print(f'  [{do_name} / {si_name}] 조회 중...', flush=True)
        rows = fetch_rows(code, si_name)
        region_added = 0
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

            for kw in ['국어', '영어', '수학']:
                if kw in crse and len(buckets[kw]) < count * 2:
                    row['_region'] = do_name  # 지역 정보 저장
                    buckets[kw].append(row)
                    selected_names.append(name)
                    region_added += 1
                    break

        print(f'    → {region_added}개 수집 (국어:{len(buckets["국어"])} 영어:{len(buckets["영어"])} 수학:{len(buckets["수학"])})', flush=True)
        time.sleep(0.3)

        # 각 버킷에 충분히 모이면 조기 종료
        if all(len(buckets[kw]) >= count for kw in buckets):
            break

    # 국어→영어→수학 순환으로 16개 선택
    result = []
    iters = {kw: iter(buckets[kw]) for kw in ['국어', '영어', '수학']}
    while len(result) < count:
        added = False
        for kw in ['국어', '영어', '수학']:
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
    if '국어' in crse: return 'academy-tag-kor'
    if '영어' in crse: return 'academy-tag-eng'
    if '수학' in crse: return 'academy-tag-math'
    return 'academy-tag-etc'


def tag_label(crse):
    if '국어' in crse: return '국어'
    if '영어' in crse: return '영어'
    if '수학' in crse: return '수학'
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


def make_section(academies):
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
        region = row.get('_region', '전국')

        cards.append(f'''
            <article class="academy-card">
              <img src="{img}" alt="{region} {name} 내부" class="academy-card-img" loading="lazy" width="740" height="400">
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
                'addressLocality': region,
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
        'name': '전국 베스트 학원모음',
        'itemListElement': jsonld_items
    }, ensure_ascii=False, indent=2)

    cards_html = ''.join(cards)
    return (
        '    <!-- BEST_SECTION_START -->\n'
        '    <section class="section">\n'
        '      <div class="container">\n'
        '        <h2 class="section-title">전국 베스트 학원모음</h2>\n'
        f'        <p class="section-desc">전국 국어·영어·수학 학원 {len(academies)}곳을 선별했습니다.</p>\n'
        '        <div class="academy-grid">'
        f'{cards_html}\n'
        '        </div>\n'
        '      </div>\n'
        '    </section>\n'
        f'    <script type="application/ld+json">\n{jsonld}\n    </script>\n'
        '    <!-- BEST_SECTION_END -->'
    )


def insert_or_replace(html, section):
    # 이미 삽입된 섹션이면 교체
    if '<!-- BEST_SECTION_START -->' in html:
        return re.sub(
            r'    <!-- BEST_SECTION_START -->.*?<!-- BEST_SECTION_END -->',
            section,
            html,
            flags=re.DOTALL
        )
    # <!-- H2 ③ 학부모님 고민거리 --> 바로 앞에 삽입
    marker = '    <!-- H2 ③ 학부모님 고민거리 -->'
    if marker in html:
        return html.replace(marker, section + '\n\n' + marker)
    # fallback: </main> 바로 앞
    return html.replace('  </main>', section + '\n\n  </main>')


# ── 실행 ──────────────────────────────────────────────────────────────
print('전국 학원 데이터 수집 시작...', flush=True)
academies = collect_nationwide(count=16)
print(f'\n총 {len(academies)}개 학원 선별 완료', flush=True)

if len(academies) < 5:
    print('학원 수가 너무 적어 삽입을 건너뜁니다.')
    sys.exit(1)

section = make_section(academies)

with open(ROOT_HTML, encoding='utf-8') as f:
    html = f.read()

with open(ROOT_HTML, 'w', encoding='utf-8') as f:
    f.write(insert_or_replace(html, section))

print(f'루트 index.html에 {len(academies)}개 학원 섹션 삽입 완료')
