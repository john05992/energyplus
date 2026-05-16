"""
all_card.py
===========
전 레벨(1~5) NEIS API 학원카드 생성 모듈.
gen_all.py에서 import해서 사용.

사용법:
    from all_card import get_academies, make_section

    rows = get_academies(level=3, code='J10', si='고양시', dong='마두동')
    html = make_section(rows, area_name='마두동')
"""

import json
import random
import re
import time
import urllib.parse
import urllib.request

# ── 상수 ──────────────────────────────────────────────────────────────
NEIS_KEY = '1e15a9adec0647c4a5d52cfc2c5cc9fe'
NEIS_URL = 'https://open.neis.go.kr/hub/acaInsTiInfo'

CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
CARD_IMGS = [
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

# 시 이름이 API 행정구역명과 다를 때 복수 구 매핑
SI_ZONE_MAP = {
    '청주시': ['상당구', '서원구', '청원구', '흥덕구'],
    '세종':   ['세종특별자치시'],
}

# 학년별 과목 키워드
GRADE_KW = {
    '초등':    ['초등'],
    '중등':    ['중등', '중학'],
    '고등':    ['고등', '고학'],
    '메인학원': [],   # 필터 없음
}

# API 캐시: (code, si) → rows
_api_cache: dict = {}


# ── API 호출 ──────────────────────────────────────────────────────────
def _fetch_rows(code: str, si: str | None) -> list:
    """시/구 단위 전체 학원 rows 반환 (캐시 활용)."""
    cache_key = (code, si)
    if cache_key in _api_cache:
        return _api_cache[cache_key]

    zones = SI_ZONE_MAP.get(si, [si] if si else [None])
    all_rows = []
    for zone in zones:
        params = {
            'KEY':               NEIS_KEY,
            'Type':              'json',
            'pIndex':            1,
            'pSize':             1000,
            'ATPT_OFCDC_SC_CODE': code,
        }
        if zone:
            params['ADMST_ZONE_NM'] = zone
        try:
            url = f'{NEIS_URL}?{urllib.parse.urlencode(params)}'
            with urllib.request.urlopen(url, timeout=20) as r:
                data = json.loads(r.read().decode('utf-8'))
            rows = data.get('acaInsTiInfo', [{}, {}])
            if len(rows) >= 2:
                all_rows += rows[1].get('row', [])
        except Exception as e:
            print(f'  [API 오류] zone={zone}: {e}')
        if len(zones) > 1:
            time.sleep(0.2)

    _api_cache[cache_key] = all_rows
    return all_rows


# ── 필터 헬퍼 ─────────────────────────────────────────────────────────
def _extract_dong(fa_rdnda: str) -> str:
    """FA_RDNDA 괄호 안 첫 토큰 추출. 예: '(마두동, 3층)' → '마두동'"""
    if not fa_rdnda:
        return ''
    m = re.search(r'\(([^,)]+)', fa_rdnda)
    return m.group(1).strip() if m else ''


def _is_duplicate(name: str, selected: list, min_len: int = 6) -> bool:
    for exist in selected:
        for i in range(len(name) - min_len + 1):
            if name[i:i + min_len] in exist:
                return True
    return False


def _grade_match(crse: str, grade: str) -> bool:
    """과목 문자열이 학년 키워드를 포함하는지 확인. 메인학원은 항상 True."""
    kws = GRADE_KW.get(grade, [])
    if not kws:
        return True
    return any(k in crse for k in kws)


def _pick(rows: list, dong: str | None, grade: str | None, count: int = 16) -> list:
    """
    rows에서 조건에 맞는 학원 count개 추출.
    dong=None  → 동 필터 없음
    grade=None → 학년 필터 없음
    수학→영어→국어 순환 인터리브.
    """
    buckets: dict[str, list] = {'수학': [], '영어': [], '국어': []}
    selected_names: list[str] = []

    for row in rows:
        if row.get('REG_STTUS_NM') != '개원':
            continue
        fee = row.get('PSNBY_THCC_CNTNT', '')
        if not fee or not fee.strip():
            continue
        crse = row.get('LE_CRSE_LIST_NM') or row.get('LE_CRSE_NM') or ''
        name = row.get('ACA_NM', '')
        if _is_duplicate(name, selected_names):
            continue

        # 동 필터
        if dong is not None:
            dong_in_addr = _extract_dong(row.get('FA_RDNDA') or '')
            if not dong_in_addr or dong not in dong_in_addr:
                continue

        # 학년 필터
        if grade is not None and not _grade_match(crse, grade):
            continue

        for kw in ['수학', '영어', '국어']:
            if kw in crse and len(buckets[kw]) < count:
                buckets[kw].append(row)
                selected_names.append(name)
                break

    result: list = []
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


# ── 공개 API ──────────────────────────────────────────────────────────
def get_academies(
    level: int,
    code:  str,
    si:    str | None = None,
    dong:  str | None = None,
    grade: str | None = None,
    count: int = 16,
) -> list:
    """
    레벨별 학원 rows 반환.

    level 1: code만 사용, 필터 없음
    level 2: code + si, 필터 없음
    level 3: code + si + dong 필터, 폴백: 동 제거
    level 4: code + si + dong + grade 필터, 3단계 폴백
    level 5: level 4와 동일 (키워드는 URL/title에만 사용)
    """
    rows = _fetch_rows(code, si)

    if level == 1:
        return _pick(rows, dong=None, grade=None, count=count)

    if level == 2:
        return _pick(rows, dong=None, grade=None, count=count)

    if level == 3:
        result = _pick(rows, dong=dong, grade=None, count=count)
        if len(result) < 5:
            result = _pick(rows, dong=None, grade=None, count=count)
        return result

    if level in (4, 5):
        # 1차: 동 + 학년
        result = _pick(rows, dong=dong, grade=grade, count=count)
        if len(result) >= 16:
            return result
        # 폴백1: 동 유지, 학년 제거
        result = _pick(rows, dong=dong, grade=None, count=count)
        if len(result) >= 5:
            return result
        # 폴백2: 동 제거, 학년 유지
        result = _pick(rows, dong=None, grade=grade, count=count)
        if len(result) >= 5:
            return result
        # 폴백3: 동 + 학년 모두 제거
        return _pick(rows, dong=None, grade=None, count=count)

    return []


# ── HTML 생성 ─────────────────────────────────────────────────────────
def _tag_class(crse: str) -> str:
    if '수학' in crse: return 'academy-tag-math'
    if '영어' in crse: return 'academy-tag-eng'
    if '국어' in crse: return 'academy-tag-kor'
    return 'academy-tag-etc'


def _tag_label(crse: str) -> str:
    if '수학' in crse: return '수학'
    if '영어' in crse: return '영어'
    if '국어' in crse: return '국어'
    return crse[:6]


def _format_fee(raw: str) -> str:
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


def _parse_offers(raw: str) -> list:
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


def _card_img_url(area_name: str, academy_name: str, base_img: str) -> str:
    """
    학원카드 이미지 URL.
    텍스트 오버레이: "{area_name} {academy_name} 내부"
    """
    text = f'{area_name} {academy_name} 내부'
    encoded = urllib.parse.quote(text, safe='')
    idx = base_img.find('/upload/') + len('/upload/')
    rest = base_img[idx:]
    base = base_img[:idx]
    return (
        f'{base}w_740,h_400,c_fill,q_auto,f_auto/'
        f'l_text:NanumGothic_10:{encoded},'
        f'co_white,o_25,g_south_west,x_10,y_6/{rest}'
    )


def make_section(academies: list, area_name: str) -> str:
    """학원카드 16개 + ItemList JSON-LD → ACADEMY_SECTION HTML 반환."""
    imgs = CARD_IMGS.copy()
    random.shuffle(imgs)

    cards = []
    jsonld_items = []

    for i, row in enumerate(academies):
        name   = row.get('ACA_NM', '')
        num    = row.get('ACA_ASNUM', '')
        crse   = row.get('LE_CRSE_LIST_NM') or row.get('LE_CRSE_NM') or ''
        fee    = _format_fee(row.get('PSNBY_THCC_CNTNT', ''))
        addr   = row.get('FA_RDNMA', '')
        detail = (row.get('FA_RDNDA') or '').strip()
        if detail:
            addr = f'{addr} {detail}'
        img = _card_img_url(area_name, name, imgs[i % len(imgs)])

        cards.append(f'''
            <article class="academy-card">
              <img src="{img}" alt="{area_name} {name} 내부"
                   class="academy-card-img" loading="lazy" width="740" height="400">
              <div class="academy-card-body">
                <h3 class="academy-card-name">{name}</h3>
                <p class="academy-card-num">학원지정번호 {num}</p>
                <div class="academy-card-tags">
                  <span class="{_tag_class(crse)}">{_tag_label(crse)}</span>
                </div>
                <p class="academy-card-fee">{fee}</p>
                <p class="academy-card-addr">{addr}</p>
              </div>
            </article>''')

        offers = _parse_offers(row.get('PSNBY_THCC_CNTNT', ''))
        item = {
            '@type': 'EducationalOrganization',
            'name': name,
            'identifier': num,
            'address': {
                '@type': 'PostalAddress',
                'streetAddress': addr,
                'addressLocality': area_name,
                'addressCountry': 'KR',
            },
        }
        if offers:
            item['hasOfferCatalog'] = {
                '@type': 'OfferCatalog',
                'name': '수강료',
                'itemListElement': [
                    {'@type': 'Offer', 'name': o['name'],
                     'price': o['price'], 'priceCurrency': 'KRW'}
                    for o in offers
                ],
            }
        jsonld_items.append({'@type': 'ListItem', 'position': i + 1, 'item': item})

    jsonld = json.dumps({
        '@context': 'https://schema.org',
        '@type': 'ItemList',
        'name': f'{area_name} 인기학원 모음',
        'itemListElement': jsonld_items,
    }, ensure_ascii=False, indent=2)

    cards_html = ''.join(cards)
    return (
        '<!-- ACADEMY_SECTION_START -->\n'
        '<section class="section">\n'
        '  <div class="container">\n'
        f'    <h2 class="section-title">해당 지역 인기학원 모음</h2>\n'
        f'    <p class="section-desc">{area_name} 수학·영어·국어 학원 {len(academies)}곳을 모았습니다.</p>\n'
        '    <div class="academy-grid">'
        f'{cards_html}\n'
        '    </div>\n'
        '  </div>\n'
        '</section>\n'
        f'<script type="application/ld+json">\n{jsonld}\n</script>\n'
        '<!-- ACADEMY_SECTION_END -->'
    )
