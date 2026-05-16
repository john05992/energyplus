"""
gen_all.py
==========
서울특별시 index.html 전체 생성.
본문뽑기/서울특별시/...에 result.html 있는 경로만 처리 (레벨1~5).

실행: python gen_all.py
"""

import json
import sys
import hashlib
import urllib.parse
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

from all_card import get_academies, make_section as make_card_section

# ── 경로 상수 ─────────────────────────────────────────────────────────
BASE      = Path(r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원')
BODUN     = Path(r'C:\Users\tlsdy\OneDrive\바탕 화면\본문뽑기')
TARGET_DO = '서울특별시'
SITE      = 'https://energyplus.kr'
BRAND     = '동네학원 찾기 - 에너지+'
CLOUD     = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'

# ── 도 코드 / 도 축약 ──────────────────────────────────────────────────
DO_CODE = {
    '서울특별시':'B10','부산광역시':'C10','대구광역시':'D10',
    '인천광역시':'E10','광주광역시':'F10','대전광역시':'G10',
    '울산광역시':'H10','세종시':'I10','경기도':'J10',
    '강원도':'K10','충청북도':'M10','충청남도':'N10',
    '전북특별자치도':'P10','경상북도':'R10','경상남도':'S10','제주도':'T10',
}
DO_SHORT = {
    '서울특별시':'서울','경기도':'경기','인천광역시':'인천',
    '부산광역시':'부산','대구광역시':'대구','대전광역시':'대전',
    '광주광역시':'광주','울산광역시':'울산','강원도':'강원',
    '충청남도':'충남','충청북도':'충북','전북특별자치도':'전북',
    '경상북도':'경북','경상남도':'경남','세종시':'세종','제주도':'제주',
}

# ── 슬라이더 / 상세페이지 이미지 목록 ────────────────────────────────
SLIDER_IMGS = [
    ('academy/1학원정면',   '학원정면'),
    ('academy/2일대일수업', '일대일수업'),
    ('academy/3기말리뷰',   '기말리뷰'),
    ('academy/4코칭',       '코칭'),
    ('academy/5수업중',     '수업중'),
    ('academy/6상장',       '상장'),
    ('academy/7학교별기출', '학교별기출'),
]
DETAIL_IMGS = [
    ('webp/1합격법',       '합격법'),
    ('webp/2선생님소개',   '선생님소개'),
    ('webp/3일대일지도',   '일대일지도'),
    ('webp/4커리큘럼',     '커리큘럼'),
    ('webp/5타학원차이점', '타학원차이점'),
    ('webp/6성적향상사례', '성적향상사례'),
    ('webp/7플래너사진',   '플래너사진'),
    ('webp/8소통법',       '소통법'),
    ('webp/9관리법',       '관리법'),
    ('webp/10공부공간',    '공부공간'),
    ('webp/11수업방식',    '수업방식'),
    ('webp/12학습코칭',    '학습코칭'),
    ('webp/13국어',        '국어'),
    ('webp/14영어',        '영어'),
    ('webp/15수학',        '수학'),
    ('webp/16비용',        '비용'),
    ('webp/17상담예약',    '상담예약'),
]


# ══════════════════════════════════════════════════════════════════════
# 데이터 로드
# ══════════════════════════════════════════════════════════════════════

def load_titles():
    with open(BASE / '타이틀.txt', encoding='utf-8') as f:
        return [l.strip() for l in f if l.strip()]


def load_grade_keywords():
    """returns {grade: [kw, ...]}"""
    kws: dict[str, list] = {'초등': [], '중등': [], '고등': [], '메인학원': []}
    with open(BASE / '학년학원키워드.txt', encoding='utf-8') as f:
        for line in f:
            parts = line.rstrip('\n').split('\t')
            if len(parts) >= 2:
                kw, grade = parts[0].strip(), parts[1].strip()
                if kw and grade in kws:
                    kws[grade].append(kw)
    with open(BASE / '메인학원키워드.txt', encoding='utf-8') as f:
        for line in f:
            kw = line.strip()
            if kw:
                kws['메인학원'].append(kw)
    return kws


def load_location_ids():
    """location_ids.txt → {key: public_id}"""
    result = {}
    with open(BASE / 'location_ids.txt', encoding='utf-8') as f:
        for line in f:
            parts = line.rstrip('\n').split('\t')
            if len(parts) >= 2:
                key, pid = parts[0].strip(), parts[1].strip()
                if key:
                    result[key] = pid
    return result


def load_dong_loc_map():
    """학원목록.txt col3(동) → col4(위치사진키)"""
    result = {}
    with open(BASE / '학원목록.txt', encoding='utf-8') as f:
        for line in f:
            cols = line.rstrip('\n').split('\t')
            if len(cols) >= 5:
                dong = cols[3].strip()
                loc  = cols[4].strip()
                if dong and loc:
                    result[dong] = loc
    return result


def load_si_loc_map(loc_ids: dict) -> dict:
    """학원목록.txt → {si: [public_id, ...]} (서울특별시 기준)"""
    result: dict[str, list] = {}
    cur_do = cur_si = ''
    with open(BASE / '학원목록.txt', encoding='utf-8') as f:
        for line in f:
            cols = line.rstrip('\n').split('\t')
            if len(cols) < 5:
                continue
            if cols[0].strip(): cur_do = cols[0].strip()
            if cols[1].strip(): cur_si = cols[1].strip()
            if cur_do != TARGET_DO or not cur_si:
                continue
            loc_key = cols[4].strip()
            if loc_key:
                pid = loc_ids.get(loc_key)
                if pid:
                    result.setdefault(cur_si, [])
                    if pid not in result[cur_si]:
                        result[cur_si].append(pid)
    return result


def load_si_dong_map() -> dict:
    """학원목록.txt → {si: [dong, ...]} (서울특별시 기준)"""
    result: dict[str, list] = {}
    cur_do = cur_si = ''
    with open(BASE / '학원목록.txt', encoding='utf-8') as f:
        for line in f:
            cols = line.rstrip('\n').split('\t')
            if len(cols) < 4:
                continue
            if cols[0].strip(): cur_do = cols[0].strip()
            if cols[1].strip(): cur_si = cols[1].strip()
            if cur_do != TARGET_DO or not cur_si:
                continue
            dong = cols[3].strip()
            if dong:
                result.setdefault(cur_si, [])
                if dong not in result[cur_si]:
                    result[cur_si].append(dong)
    return result


# ══════════════════════════════════════════════════════════════════════
# Cloudinary URL 생성
# ══════════════════════════════════════════════════════════════════════

def cld_url(public_id: str, text: str, w: int = 800, h: int = 0,
            crop: str = '', angle: int = 0) -> str:
    enc    = urllib.parse.quote(text, safe='')
    size   = f'w_{w}'
    if h:     size += f',h_{h}'
    if crop:  size += f',c_{crop}'
    prefix = f'a_{angle}/' if angle else ''
    return (
        f'{CLOUD}/{prefix}{size},q_auto,f_auto'
        f'/l_text:NanumGothic_10:{enc},'
        f'co_white,o_25,g_south_west,x_10,y_6'
        f'/{public_id}.webp'
    )


def og_image(akw: str, level: int, kw: str = '') -> str:
    text = f'{akw} {kw} 학원 실제내부' if level == 5 and kw else f'{akw} 학원 실제내부'
    return cld_url('academy/2일대일수업', text, w=1200, h=630, crop='fill')


# ══════════════════════════════════════════════════════════════════════
# 지역키워드 / 타이틀
# ══════════════════════════════════════════════════════════════════════

def get_area_kw(level: int, do: str, si: str, dong: str, grade: str) -> str:
    if level == 1: return DO_SHORT.get(do, do)
    if level == 2: return si
    if level == 3: return dong
    if level == 4: return f'{dong} {grade}'
    return dong  # 레벨5: 지역만, 학원키워드 별도


def pick_title(titles: list, page_key: str) -> str:
    h = int(hashlib.md5(page_key.encode()).hexdigest(), 16)
    return titles[h % len(titles)]


def build_title(level: int, do: str, si: str, dong: str, grade: str, kw: str, tv: str) -> str:
    if level == 1:
        return f'{DO_SHORT.get(do, do)} 영어·수학·국어 학원 {tv}'
    elif level == 2:
        return f'{si} 영어·수학·국어 학원 {tv}'
    elif level == 3:
        return f'{dong} 영어·수학·국어 학원 {tv}'
    elif level == 4:
        return f'{dong} {grade} 영어·수학·국어 학원 {tv}'
    else:
        return f'{dong} {kw} {tv}'


def build_kw_meta(level: int, do: str, si: str, dong: str, grade: str, kw: str) -> str:
    d_s = DO_SHORT.get(do, do)
    if level == 1:
        return f'{d_s} 학원, {d_s} 수학학원, {d_s} 영어학원, {d_s} 국어학원, {do} 학원 추천, {d_s} 학원 모음'
    elif level == 2:
        return f'{si} 학원, {si} 수학학원, {si} 영어학원, {si} 국어학원, {d_s} {si} 학원, {si} 학원 추천'
    elif level == 3:
        return f'{dong} 학원, {dong} 수학학원, {dong} 영어학원, {si} 학원, {dong} 학원 추천, {d_s} {dong} 학원'
    elif level == 4:
        return f'{dong} {grade} 학원, {dong} {grade} 수학학원, {dong} {grade} 영어학원, {si} {grade} 학원, {dong} 학원, {grade} 학원 추천'
    else:
        return f'{dong} {kw}, {si} {kw}, {d_s} {kw}, {dong} 학원, {kw} 추천, {dong} {grade} 학원'


# ══════════════════════════════════════════════════════════════════════
# HTML 섹션 생성
# ══════════════════════════════════════════════════════════════════════

def first_slide_url(akw: str, level: int, kw: str = '') -> str:
    pid, alt_base = SLIDER_IMGS[0]
    text = f'{akw} {kw} {alt_base}' if level == 5 and kw else f'{akw} {alt_base}'
    return cld_url(pid, text, w=800, h=800, crop='fill', angle=90)


def make_hero(akw: str, level: int, kw: str, title: str) -> str:
    """히어로 섹션: 슬라이더(우측) + H1(좌측) 통합."""
    slides = []
    for i, (pid, alt_base) in enumerate(SLIDER_IMGS):
        text  = f'{akw} {kw} {alt_base}' if level == 5 and kw else f'{akw} {alt_base}'
        # 1번 이미지(학원정면)는 90도 회전 보정
        rot   = 90 if i == 0 else 0
        src   = cld_url(pid, text, w=800, h=800, crop='fill', angle=rot)
        if i == 0:
            attrs = 'loading="eager" fetchpriority="high" decoding="sync"'
        else:
            attrs = 'loading="lazy" decoding="async"'
        slides.append(
            f'          <div class="slide">'
            f'<img src="{src}" alt="{text}" {attrs} width="800" height="800">'
            f'</div>'
        )
    slides_html = '\n'.join(slides)
    n         = len(SLIDER_IMGS)
    dots_html = '\n'.join(
        f'          <span class="sl-dot{"  sl-dot-active" if i == 0 else ""}"></span>'
        for i in range(n)
    )

    badge   = f'{akw} 학원 정보'
    tagline = '영어·수학·국어 학원을<br>지역별로 쉽게 찾아보세요'

    return (
        '    <section class="hero">\n'
        '      <div class="hero-inner">\n'
        '        <div class="hero-img-wrap">\n'
        '          <div class="sl-track">\n'
        f'{slides_html}\n'
        '          </div>\n'
        '          <button class="sl-arrow sl-prev" aria-label="이전 사진">&#8249;</button>\n'
        '          <button class="sl-arrow sl-next" aria-label="다음 사진">&#8250;</button>\n'
        '          <div class="sl-dots">\n'
        f'{dots_html}\n'
        '          </div>\n'
        '        </div>\n'
        '        <div class="hero-text">\n'
        '          <h1 class="site-headline">\n'
        f'            <span class="headline-badge">{badge}</span>\n'
        f'            <span class="headline-main">{title}</span>\n'
        '            <span class="headline-sub">우리 동네 학원, 지금 바로 찾아보세요</span>\n'
        '          </h1>\n'
        f'          <p class="site-tagline">{tagline}</p>\n'
        '        </div>\n'
        '      </div>\n'
        '    </section>'
    )


def make_detail(akw: str, level: int, kw: str = '') -> str:
    imgs = []
    for pid, alt_base in DETAIL_IMGS:
        text = f'{akw} {kw} {alt_base}' if level == 5 and kw else f'{akw} {alt_base}'
        # 원본 680×1300 비율 그대로 (crop 없음) — w=680 자연 스케일
        src  = cld_url(pid, text, w=680)
        imgs.append(
            f'        <img src="{src}" alt="{text}" '
            f'loading="lazy" decoding="async" width="680" height="1300">'
        )
    return (
        '    <section class="detail-section">\n'
        '      <div class="container">\n'
        + '\n'.join(imgs) + '\n'
        '      </div>\n'
        '    </section>'
    )


def make_location(level: int, si: str, dong: str, dong_loc: dict,
                  loc_ids: dict, si_loc: dict, akw: str) -> str:
    if level == 1:
        return ''

    pids = []
    if level == 2:
        pids = si_loc.get(si, [])
    else:
        key = dong_loc.get(dong)
        if key:
            pid = loc_ids.get(key)
            if pid:
                pids = [pid]

    if not pids:
        return ''

    imgs = []
    for n, pid in enumerate(pids, 1):
        text = f'{akw} 위치사진{n}'
        src  = cld_url(pid, text, w=800, h=450, crop='fill')
        imgs.append(
            f'        <img src="{src}" alt="{akw} 위치사진{n}" '
            f'loading="lazy" decoding="async" width="800" height="450">'
        )

    return (
        '    <section class="section">\n'
        '      <div class="container">\n'
        '        <h2 class="section-title">학원 위치 사진</h2>\n'
        + '\n'.join(imgs) + '\n'
        '      </div>\n'
        '    </section>'
    )


def render_section1(s: dict) -> str:
    return (
        '    <section class="section">\n'
        '      <div class="container">\n'
        f'        <h2 class="section-title">{s.get("h2","")}</h2>\n'
        f'        <p class="section-desc">{s.get("p","")}</p>\n'
        '      </div>\n'
        '    </section>'
    )


def render_list_section(s: dict) -> str:
    li = ''.join(f'<li>{item}</li>' for item in s.get('list', []))
    return (
        '    <section class="section">\n'
        '      <div class="container">\n'
        f'        <h2 class="section-title">{s.get("h2","")}</h2>\n'
        f'        <p class="section-desc">{s.get("p","")}</p>\n'
        f'        <ul class="content-list">{li}</ul>\n'
        '      </div>\n'
        '    </section>'
    )


def render_section3(s: dict) -> str:
    li   = ''.join(f'<li>{item}</li>' for item in s.get('list', []))
    rows = ''.join(
        f'<tr><th scope="row">{r["항목"]}</th><td>{r["내용"]}</td></tr>'
        for r in s.get('table', [])
    )
    return (
        '    <section class="section">\n'
        '      <div class="container">\n'
        f'        <h2 class="section-title">{s.get("h2","")}</h2>\n'
        f'        <p class="section-desc">{s.get("p","")}</p>\n'
        f'        <ul class="content-list">{li}</ul>\n'
        f'        <table class="info-table"><tbody>{rows}</tbody></table>\n'
        '      </div>\n'
        '    </section>'
    )


def render_section4(s: dict) -> str:
    rows = ''.join(
        f'<tr><td>{r["구분"]}</td><td>{r["대상"]}</td><td>{r["내용"]}</td></tr>'
        for r in s.get('table', [])
    )
    return (
        '    <section class="section">\n'
        '      <div class="container">\n'
        f'        <h2 class="section-title">{s.get("h2","")}</h2>\n'
        f'        <p class="section-desc">{s.get("p","")}</p>\n'
        '        <table class="compare-table">\n'
        '          <thead><tr><th>구분</th><th>대상</th><th>내용</th></tr></thead>\n'
        f'          <tbody>{rows}</tbody>\n'
        '        </table>\n'
        '      </div>\n'
        '    </section>'
    )


def render_section8(s: dict) -> str:
    faq = ''.join(
        f'<dt class="faq-q">Q. {f["q"]}</dt><dd class="faq-a">{f["a"]}</dd>'
        for f in s.get('faq', [])
        if f.get('q') and f.get('a')
    )
    return (
        '    <section class="section">\n'
        '      <div class="container">\n'
        f'        <h2 class="section-title">{s.get("h2","")}</h2>\n'
        f'        <dl class="faq-list">{faq}</dl>\n'
        '      </div>\n'
        '    </section>'
    )


def make_region_list(level: int, do: str, si: str, dong: str, grade: str,
                     grade_kws: dict, si_dong_map: dict) -> str:
    if level == 5:
        return ''

    if level == 1:
        sis = sorted(si_dong_map.keys())
        items = '\n'.join(f'            <li><a href="/{do}/{s}/">{s} 학원</a></li>' for s in sis)
        h2 = f'{DO_SHORT.get(do, do)} 지역별 학원 안내'
    elif level == 2:
        dongs = si_dong_map.get(si, [])
        items = '\n'.join(f'            <li><a href="/{do}/{si}/{d}/">{d} 학원</a></li>' for d in sorted(dongs))
        h2 = f'{si} 지역별 학원 안내'
    elif level == 3:
        grades = ['초등', '중등', '고등', '메인학원']
        items = '\n'.join(f'            <li><a href="/{do}/{si}/{dong}/{g}/">{g} 학원</a></li>' for g in grades)
        h2 = f'{dong} 학년별 학원 안내'
    else:  # level 4
        kws = grade_kws.get(grade, [])
        items = '\n'.join(f'            <li><a href="/{do}/{si}/{dong}/{grade}/{k}/">{k}</a></li>' for k in kws)
        h2 = f'{dong} {grade} 학원 키워드별 안내'

    return (
        '    <section class="section">\n'
        '      <div class="container">\n'
        f'        <h2 class="section-title">{h2}</h2>\n'
        '        <ul class="region-list">\n'
        f'{items}\n'
        '        </ul>\n'
        '      </div>\n'
        '    </section>'
    )


def make_back_nav(level: int, do: str, si: str, dong: str, grade: str, kw: str) -> str:
    links = []
    if level == 5:
        links.append(f'<a href="/{do}/{si}/{dong}/{grade}/">{dong} {grade} 학원 목록</a>')
    if level >= 4:
        links.append(f'<a href="/{do}/{si}/{dong}/">{dong} 학원 목록</a>')
    if level >= 3:
        links.append(f'<a href="/{do}/{si}/">{si} 학원 목록</a>')
    if level >= 2:
        links.append(f'<a href="/{do}/">{do} 학원 목록</a>')
    links.append('<a href="/">전국학원 목록 보기</a>')

    links_html = '\n'.join(f'        {l}' for l in links)
    return (
        '    <section class="section">\n'
        '      <div class="container">\n'
        '        <h2 class="section-title">상위 지역 학원 목록</h2>\n'
        '        <nav class="back-nav" aria-label="상위 지역 탐색">\n'
        f'{links_html}\n'
        '        </nav>\n'
        '      </div>\n'
        '    </section>'
    )


# ══════════════════════════════════════════════════════════════════════
# JSON-LD
# ══════════════════════════════════════════════════════════════════════

def make_json_ld(level: int, do: str, si: str, dong: str, grade: str, kw: str,
                 title: str, desc: str, canon: str, og_img: str, data: dict) -> str:
    # BreadcrumbList
    crumbs = [{'@type': 'ListItem', 'position': 1, 'name': '홈', 'item': f'{SITE}/'}]
    if level >= 1:
        crumbs.append({'@type': 'ListItem', 'position': 2, 'name': do, 'item': f'{SITE}/{do}/'})
    if level >= 2:
        crumbs.append({'@type': 'ListItem', 'position': 3, 'name': si, 'item': f'{SITE}/{do}/{si}/'})
    if level >= 3:
        crumbs.append({'@type': 'ListItem', 'position': 4, 'name': dong, 'item': f'{SITE}/{do}/{si}/{dong}/'})
    if level >= 4:
        crumbs.append({'@type': 'ListItem', 'position': 5, 'name': grade, 'item': f'{SITE}/{do}/{si}/{dong}/{grade}/'})
    if level == 5:
        crumbs.append({'@type': 'ListItem', 'position': 6, 'name': kw, 'item': f'{SITE}/{do}/{si}/{dong}/{grade}/{kw}/'})

    # knowsAbout per level
    d_s = DO_SHORT.get(do, do)
    if level == 1:
        knows = [f'{d_s} 학원', f'{d_s} 수학학원', f'{d_s} 영어학원', '수능 대비', '내신 대비']
    elif level == 2:
        knows = [f'{si} 학원', f'{si} 수학학원', f'{si} 영어학원', '수능 대비', '내신 대비']
    elif level == 3:
        knows = [f'{dong} 학원', f'{dong} 수학학원', f'{dong} 영어학원', f'{si} 학원']
    elif level == 4:
        knows = [f'{dong} {grade} 학원', f'{dong} {grade} 수학학원', f'{dong} {grade} 영어학원', f'{si} 학원']
    else:
        knows = [f'{dong} {kw}', f'{dong} {grade} 학원', f'{si} {kw}', kw]

    # FAQPage (section8) — q/a 둘 다 있는 항목만
    faq_items = [
        {'@type': 'Question', 'name': f['q'], 'acceptedAnswer': {'@type': 'Answer', 'text': f['a']}}
        for f in data.get('section8', {}).get('faq', [])
        if f.get('q') and f.get('a')
    ]

    graph = [
        {
            '@type': 'Article',
            '@id': f'{canon}#article',
            'headline': title,
            'description': desc,
            'image': og_img,
            'datePublished': '2026-05-16',
            'dateModified': '2026-05-16',
            'author': {'@type': 'Organization', 'name': BRAND, 'url': f'{SITE}/'},
            'publisher': {
                '@type': 'Organization',
                'name': BRAND,
                'url': f'{SITE}/',
                'logo': {'@type': 'ImageObject', 'url': f'{SITE}/images/로고.jpg', 'width': 200, 'height': 200},
            },
            'mainEntityOfPage': {'@type': 'WebPage', '@id': canon},
            'inLanguage': 'ko-KR',
        },
        {'@type': 'BreadcrumbList', 'itemListElement': crumbs},
    ]
    if faq_items:
        graph.append({'@type': 'FAQPage', 'mainEntity': faq_items})
    graph += [
        {
            '@type': 'Person',
            '@id': f'{SITE}/#editor',
            'name': '전국학원팀 편집자',
            'jobTitle': '교육 콘텐츠 편집자',
            'worksFor': {'@id': f'{SITE}/#organization'},
            'knowsAbout': knows,
        },
        {
            '@type': 'Service',
            '@id': f'{SITE}/#service',
            'serviceType': 'TutoringService',
            'areaServed': {'@type': 'Country', 'name': 'South Korea'},
            'offers': {'@type': 'Offer', 'priceCurrency': 'KRW', 'priceRange': '100000-600000'},
        },
        {
            '@type': 'LocalBusiness',
            '@id': f'{SITE}/#localbusiness',
            'name': BRAND,
            'telephone': '+82-10-3952-5815',
            'address': {'@type': 'PostalAddress', 'addressLocality': '전국', 'addressCountry': 'KR'},
        },
    ]

    return json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=2)


# ══════════════════════════════════════════════════════════════════════
# HEAD 생성
# ══════════════════════════════════════════════════════════════════════

def make_head(title: str, desc: str, canon: str, og_img: str, kw_meta: str,
              jld: str, lcp_img: str = '') -> str:
    preload_lcp = (
        f'  <link rel="preload" as="image" href="{lcp_img}" fetchpriority="high">\n'
        if lcp_img else ''
    )
    return f'''\
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{kw_meta}">
  <meta name="author" content="{BRAND}">
  <meta name="robots" content="index, follow">
  <meta name="naver-site-verification" content="6c8552333b0e48ee6249eeecfdd0e6c5c62384eb">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canon}">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:locale" content="ko_KR">
  <meta property="og:image" content="{og_img}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{og_img}">
  <meta name="theme-color" content="#F97316">
  <link rel="canonical" href="{canon}">
  <link rel="icon" href="https://energyplus.kr/images/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="https://energyplus.kr/images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="https://energyplus.kr/images/favicon-16x16.png">
  <link rel="apple-touch-icon" href="https://energyplus.kr/images/로고.jpg">
  <link rel="preconnect" href="https://res.cloudinary.com" crossorigin>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{preload_lcp}  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@800&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@800&display=swap" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@800&display=swap"></noscript>
  <link rel="stylesheet" href="/css/style.css">
  <style>
  /* ── 슬라이더 (style.css hero-img-wrap 안에서 동작) ── */
  .hero-img-wrap{{position:relative;overflow:hidden}}
  .sl-track{{position:absolute;inset:0;display:flex;height:100%;transition:transform .45s cubic-bezier(.4,0,.2,1);will-change:transform}}
  .slide{{flex:0 0 100%;height:100%;overflow:hidden}}
  .slide img{{width:100%;height:100%;object-fit:cover;display:block}}
  /* 점(dots) */
  .sl-dots{{position:absolute;bottom:10px;left:50%;transform:translateX(-50%);display:flex;gap:6px;z-index:2}}
  .sl-dot{{width:7px;height:7px;border-radius:50%;background:rgba(255,255,255,.5);transition:background .3s,transform .3s;cursor:pointer}}
  .sl-dot-active{{background:#F97316;transform:scale(1.35)}}
  /* 화살표 */
  .sl-arrow{{position:absolute;top:50%;transform:translateY(-50%);background:rgba(255,255,255,.88);border:none;border-radius:50%;width:34px;height:34px;font-size:20px;line-height:1;cursor:pointer;z-index:3;display:flex;align-items:center;justify-content:center;color:#444;box-shadow:0 2px 8px rgba(0,0,0,.18);transition:opacity .2s}}
  .sl-arrow:hover{{opacity:.9}}
  .sl-prev{{left:8px}}
  .sl-next{{right:8px}}
  /* ── 상세 이미지 ─── */
  .detail-section .container{{display:flex;flex-direction:column;align-items:center;gap:0}}
  .detail-section img{{width:100%;max-width:680px;height:auto;display:block}}
  /* ── content-list 박스형 ─── */
  .content-list{{list-style:none;padding:0;margin:.8rem 0 0;display:grid;gap:.5rem}}
  .content-list li{{background:#fff8f3;border-left:3px solid #F97316;padding:.7rem 1rem;border-radius:0 8px 8px 0;font-size:.9rem;line-height:1.6;color:#333}}
  /* ── info-table ─── */
  .info-table{{width:100%;border-collapse:collapse;margin:.8rem 0 0;border-radius:8px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.08)}}
  .info-table th{{background:#F97316;color:#fff;padding:.6rem 1rem;text-align:left;font-size:.85rem;font-weight:600;white-space:nowrap;width:7em}}
  .info-table td{{padding:.65rem 1rem;font-size:.9rem;border-bottom:1px solid #f0f0f0;color:#333;word-break:keep-all}}
  .info-table tr:last-child td{{border-bottom:none}}
  /* ── compare-table ─── */
  .compare-table{{width:100%;border-collapse:collapse;margin:.8rem 0 0;border-radius:8px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.08);font-size:.85rem}}
  .compare-table thead th{{background:#F97316;color:#fff;padding:.65rem .8rem;text-align:center;font-weight:600}}
  .compare-table tbody td{{padding:.6rem .8rem;border-bottom:1px solid #f0f0f0;color:#333;text-align:center;vertical-align:top}}
  .compare-table tbody tr:nth-child(even){{background:#fafafa}}
  .compare-table tbody tr:last-child td{{border-bottom:none}}
  /* ── FAQ ─── */
  .faq-list{{margin:.8rem 0 0}}
  .faq-q{{font-weight:700;color:#F97316;padding:.8rem 1rem .4rem;background:#fff8f3;border-radius:8px 8px 0 0;margin-top:.8rem;font-size:.9rem;display:block}}
  .faq-a{{margin:0;padding:.5rem 1rem .8rem;background:#fff8f3;border-radius:0 0 8px 8px;font-size:.88rem;color:#555;line-height:1.65;display:block}}
  </style>
  <script type="application/ld+json">
{jld}
  </script>'''


# ══════════════════════════════════════════════════════════════════════
# 전체 HTML 조립
# ══════════════════════════════════════════════════════════════════════

def make_html(level: int, do: str, si: str, dong: str, grade: str, kw: str,
              data: dict, titles: list, dong_loc: dict, loc_ids: dict,
              si_loc: dict, grade_kws: dict, si_dong_map: dict) -> str:

    page_key = f'{do}/{si}/{dong}/{grade}/{kw}'
    tv       = pick_title(titles, page_key)
    title    = build_title(level, do, si, dong, grade, kw, tv)
    desc     = data.get('meta', '')
    kw_meta  = build_kw_meta(level, do, si, dong, grade, kw)
    akw      = get_area_kw(level, do, si, dong, grade)

    # canonical
    if level == 1: canon = f'{SITE}/{do}/'
    elif level == 2: canon = f'{SITE}/{do}/{si}/'
    elif level == 3: canon = f'{SITE}/{do}/{si}/{dong}/'
    elif level == 4: canon = f'{SITE}/{do}/{si}/{dong}/{grade}/'
    else: canon = f'{SITE}/{do}/{si}/{dong}/{grade}/{kw}/'

    og_img  = og_image(akw, level, kw)
    lcp_img = first_slide_url(akw, level, kw)
    jld     = make_json_ld(level, do, si, dong, grade, kw, title, desc, canon, og_img, data)
    head    = make_head(title, desc, canon, og_img, kw_meta, jld, lcp_img)

    # 학원카드 (NEIS API)
    code   = DO_CODE.get(do, 'B10')
    rows   = get_academies(
        level=level, code=code,
        si=si   or None,
        dong=dong or None,
        grade=grade or None,
    )
    area_name = dong or si or DO_SHORT.get(do, do)
    card_html = make_card_section(rows, area_name)

    # result.html 섹션별 렌더링
    s1 = render_section1(data.get('section1', {}))
    s2 = render_list_section(data.get('section2', {}))
    s3 = render_section3(data.get('section3', {}))
    s4 = render_section4(data.get('section4', {}))
    s5 = render_list_section(data.get('section5', {}))
    s6 = render_list_section(data.get('section6', {}))
    s7 = render_list_section(data.get('section7', {}))
    s8 = render_section8(data.get('section8', {}))

    # 기타 섹션
    hero     = make_hero(akw, level, kw, title)
    detail   = make_detail(akw, level, kw)
    location = make_location(level, si, dong, dong_loc, loc_ids, si_loc, akw)
    region   = make_region_list(level, do, si, dong, grade, grade_kws, si_dong_map)
    backnav  = make_back_nav(level, do, si, dong, grade, kw)

    # nav 링크
    nav_do  = f'<a href="/{do}/">지역별</a>' if level >= 2 else '<a href="/">지역별</a>'
    nav_si  = f'<a href="/{do}/{si}/">학원찾기</a>' if level >= 3 else ''

    sections = '\n\n'.join(filter(None, [
        hero,
        detail,
        s1,
        location,
        s2,
        s3,
        s4,
        s5,
        card_html,
        s6,
        s7,
        s8,
        region,
        backnav,
    ]))

    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
{head}
</head>
<body>

  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="logo-wrap">
        <picture>
          <source srcset="/images/로고.webp" type="image/webp">
          <img src="/images/로고.jpg" alt="{BRAND} 로고" class="logo-img" width="72" height="72">
        </picture>
        <span class="logo-text">{BRAND}</span>
      </a>
      <nav class="site-nav">
        <a href="/">전국</a>
        {nav_do}
        {nav_si}
      </nav>
    </div>
  </header>

  <main>
    <article>

{sections}

    </article>
  </main>

  <footer class="site-footer">
    <div class="container footer-inner">
      <h3 class="footer-slogan">아이들의 성장을 응원합니다</h3>
      <p class="footer-sub">전국 동네 학원 정보를 정성껏 모아드립니다</p>
      <div class="footer-divider"></div>
      <h4 class="footer-info">
        <span>대표번호 <a href="tel:010-3952-5815">010-3952-5815</a></span>
        <span class="sep"> | </span>
        <span>대표자명 에너지+</span>
        <span class="sep"> | </span>
        <span>이메일 <a href="mailto:info@energyplus.kr">info@energyplus.kr</a></span>
      </h4>
      <p class="footer-contact">학원 등록 문의는 이메일로 부탁드립니다.</p>
      <p class="footer-copy">&copy; 2026 {BRAND}. All rights reserved.</p>
    </div>
  </footer>

  <script>
  (function(){{
    var wrap=document.querySelector('.hero-img-wrap');
    var track=wrap&&wrap.querySelector('.sl-track');
    var dots=wrap?wrap.querySelectorAll('.sl-dot'):[];
    if(!track)return;
    var n=dots.length||1,idx=0;
    function go(i){{
      idx=(i+n)%n;
      track.style.transform='translateX(-'+idx*100+'%)';
      dots.forEach(function(d,j){{d.classList.toggle('sl-dot-active',j===idx);}});
    }}
    dots.forEach(function(d,i){{d.addEventListener('click',function(){{go(i);}});}});
    var prev=wrap.querySelector('.sl-prev'),next=wrap.querySelector('.sl-next');
    if(prev)prev.addEventListener('click',function(){{go(idx-1);}});
    if(next)next.addEventListener('click',function(){{go(idx+1);}});
    var timer=setInterval(function(){{go(idx+1);}},3500);
    wrap.addEventListener('mouseenter',function(){{clearInterval(timer);}});
    wrap.addEventListener('mouseleave',function(){{timer=setInterval(function(){{go(idx+1);}},3500);}});
    /* 터치 스와이프 */
    var tx=0;
    wrap.addEventListener('touchstart',function(e){{tx=e.touches[0].clientX;}},{{passive:true}});
    wrap.addEventListener('touchend',function(e){{
      var dx=e.changedTouches[0].clientX-tx;
      if(Math.abs(dx)>40)go(dx<0?idx+1:idx-1);
    }});
  }})();
  </script>
  <script type="text/javascript" src="//wcs.pstatic.net/wcslog.js" defer></script>
  <script type="text/javascript">
  if(!wcs_add) var wcs_add = {{}};
  wcs_add["wa"] = "1424ba4d85077d";
  if(window.wcs) {{ wcs_do(); }}
  </script>

</body>
</html>'''


# ══════════════════════════════════════════════════════════════════════
# 메인
# ══════════════════════════════════════════════════════════════════════

def main():
    print('데이터 로드 중...')
    titles      = load_titles()
    grade_kws   = load_grade_keywords()
    loc_ids     = load_location_ids()
    dong_loc    = load_dong_loc_map()
    si_loc      = load_si_loc_map(loc_ids)
    si_dong_map = load_si_dong_map()
    print(f'  타이틀: {len(titles)}개 / 위치사진 ID: {len(loc_ids)}개 / 시동 맵: {len(si_dong_map)}개 시')

    bodun_do = BODUN / TARGET_DO
    count = skip = 0

    for result_path in sorted(bodun_do.rglob('result.html')):
        # 경로 분해
        rel   = result_path.relative_to(bodun_do).parts[:-1]  # result.html 제외
        level = len(rel) + 1

        do    = TARGET_DO
        si    = rel[0] if len(rel) >= 1 else ''
        dong  = rel[1] if len(rel) >= 2 else ''
        grade = rel[2] if len(rel) >= 3 else ''
        kw    = rel[3] if len(rel) >= 4 else ''

        # JSON 로드
        try:
            with open(result_path, encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f'  [JSON 오류] {result_path.relative_to(BODUN)}: {e}')
            skip += 1
            continue

        # 출력 경로
        if rel:
            out_path = BASE / TARGET_DO / Path(*rel) / 'index.html'
        else:
            out_path = BASE / TARGET_DO / 'index.html'
        out_path.parent.mkdir(parents=True, exist_ok=True)

        # HTML 생성
        try:
            html = make_html(level, do, si, dong, grade, kw, data, titles,
                             dong_loc, loc_ids, si_loc, grade_kws, si_dong_map)
            out_path.write_text(html, encoding='utf-8')
            label = '/'.join(rel) if rel else do
            print(f'  lv{level} {label}')
            count += 1
        except Exception as e:
            import traceback
            print(f'  [생성 오류] {"/".join(rel)}: {e}')
            traceback.print_exc()
            skip += 1

    print(f'\n완료: {count}개 생성 / {skip}개 오류')


if __name__ == '__main__':
    main()
