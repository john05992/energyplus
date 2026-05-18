"""
과외.py
=======
새로운학원/과외/ 아래 index.html 전체 생성.
본문뽑기/과외/...에 result.html 있는 경로만 처리 (레벨1~4).

실행: python 과외.py
"""

import json
import sys
import hashlib
import urllib.parse
from pathlib import Path
from datetime import date

sys.stdout.reconfigure(encoding='utf-8')

from all_card import get_academies, make_section as make_card_section

# ── 경로 상수 ──────────────────────────────────────────────────────────
BASE_OUT  = Path(r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원\과외')
BASE_DATA = Path(r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원')
BODUN     = Path(r'C:\Users\tlsdy\OneDrive\바탕 화면\본문뽑기\과외')
SITE      = 'https://energyplus.kr'
BRAND     = '동네과외 찾기 - 에너지+'
CLOUD     = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'

# ── 도 코드 / 도 축약 ───────────────────────────────────────────────────
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

# ── 슬라이더 / 상세페이지 이미지 목록 ─────────────────────────────────
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
    with open(BASE_DATA / '타이틀.txt', encoding='utf-8') as f:
        return [l.strip() for l in f if l.strip()]


def load_gwae_keywords():
    with open(BASE_DATA / '과외키워드.txt', encoding='utf-8') as f:
        return [l.strip() for l in f if l.strip()]


def load_gwae_regions():
    """과외지역.txt → [(loc_kw, do, sigu), ...]"""
    result = []
    with open(BASE_DATA / '과외지역.txt', encoding='utf-8') as f:
        for line in f:
            parts = line.rstrip('\n').split('\t')
            if len(parts) >= 3:
                loc_kw = parts[0].strip()
                do     = parts[1].strip()
                sigu   = parts[2].strip()
                if loc_kw and do and sigu:
                    result.append((loc_kw, do, sigu))
    return result


def build_hierarchy(regions: list):
    """regions → {do: {sigu: [loc_kw, ...]}}"""
    h: dict[str, dict[str, list]] = {}
    for loc_kw, do, sigu in regions:
        h.setdefault(do, {}).setdefault(sigu, [])
        if loc_kw not in h[do][sigu]:
            h[do][sigu].append(loc_kw)
    return h


def load_location_ids():
    result = {}
    with open(BASE_DATA / 'location_ids.txt', encoding='utf-8') as f:
        for line in f:
            parts = line.rstrip('\n').split('\t')
            if len(parts) >= 2:
                key, pid = parts[0].strip(), parts[1].strip()
                if key:
                    result[key] = pid
    return result


def load_dong_loc_map():
    result = {}
    last_loc = ''
    with open(BASE_DATA / '학원목록.txt', encoding='utf-8') as f:
        for line in f:
            cols = line.rstrip('\n').split('\t')
            if len(cols) < 4:
                continue
            dong = cols[3].strip()
            loc  = cols[4].strip() if len(cols) >= 5 else ''
            if loc:
                last_loc = loc
            if dong and last_loc:
                result[dong] = last_loc
    return result


# ══════════════════════════════════════════════════════════════════════
# Cloudinary URL
# ══════════════════════════════════════════════════════════════════════

def cld_url(public_id: str, text: str, w: int = 800, h: int = 0,
            crop: str = '', angle: int = 0) -> str:
    enc   = urllib.parse.quote(text, safe='')
    size  = f'w_{w}'
    if h:    size += f',h_{h}'
    if crop: size += f',c_{crop}'
    prefix = f'a_{angle}/' if angle else ''
    return (
        f'{CLOUD}/{prefix}{size},q_auto,f_auto'
        f'/l_text:NanumGothic_10:{enc},'
        f'co_white,o_25,g_south_west,x_10,y_6'
        f'/{public_id}.webp'
    )


def og_image(akw: str, level: int, kw: str = '') -> str:
    text = f'{akw} {kw} 과외 실제내부' if level == 4 and kw else f'{akw} 과외 실제내부'
    return cld_url('academy/2일대일수업', text, w=1200, h=630, crop='fill')


def first_slide_url(akw: str, level: int, kw: str = '') -> str:
    pid, alt_base = SLIDER_IMGS[0]
    text = f'{akw} {kw} {alt_base}' if level == 4 and kw else f'{akw} {alt_base}'
    return cld_url(pid, text, w=600, h=600, crop='fill', angle=90)


# ══════════════════════════════════════════════════════════════════════
# 타이틀 / 메타
# ══════════════════════════════════════════════════════════════════════

def get_akw(level: int, do: str, sigu: str, loc_kw: str) -> str:
    if level == 1: return DO_SHORT.get(do, do)
    if level == 2: return sigu
    return loc_kw


def pick_title(titles: list, page_key: str) -> str:
    h = int(hashlib.md5(page_key.encode()).hexdigest(), 16)
    return titles[h % len(titles)]


def build_title(level: int, do: str, sigu: str, loc_kw: str, kw: str, tv: str) -> str:
    d_s = DO_SHORT.get(do, do)
    if level == 1: return f'{d_s} 과외 {tv}'
    if level == 2: return f'{sigu} 과외 {tv}'
    if level == 3: return f'{loc_kw} 과외 {tv}'
    return f'{loc_kw} {kw} {tv}'


def build_kw_meta(level: int, do: str, sigu: str, loc_kw: str, kw: str) -> str:
    d_s = DO_SHORT.get(do, do)
    if level == 1:
        return f'{d_s} 과외, {d_s} 수학과외, {d_s} 영어과외, {d_s} 과외 추천, {do} 과외, {d_s} 과외 모음'
    if level == 2:
        return f'{sigu} 과외, {sigu} 수학과외, {sigu} 영어과외, {d_s} {sigu} 과외, {sigu} 과외 추천, {sigu} 과외 모음'
    if level == 3:
        return f'{loc_kw} 과외, {loc_kw} 수학과외, {loc_kw} 영어과외, {sigu} 과외, {loc_kw} 과외 추천, {d_s} {loc_kw} 과외'
    return f'{loc_kw} {kw}, {sigu} {kw}, {d_s} {kw}, {loc_kw} 과외, {kw} 추천, {loc_kw} 과외 추천'


# ══════════════════════════════════════════════════════════════════════
# HTML 섹션
# ══════════════════════════════════════════════════════════════════════

def make_hero(akw: str, level: int, kw: str, title: str) -> str:
    slides = []
    for i, (pid, alt_base) in enumerate(SLIDER_IMGS):
        text = f'{akw} {kw} {alt_base}' if level == 4 and kw else f'{akw} {alt_base}'
        rot  = 90 if i == 0 else 0
        src  = cld_url(pid, text, w=600, h=600, crop='fill', angle=rot)
        attrs = ('loading="eager" fetchpriority="high" decoding="sync"'
                 if i == 0 else 'loading="lazy" decoding="async"')
        slides.append(
            f'          <div class="slide">'
            f'<img src="{src}" alt="{text}" {attrs} width="600" height="600">'
            f'</div>'
        )
    slides_html = '\n'.join(slides)
    n         = len(SLIDER_IMGS)
    dots_html = '\n'.join(
        f'          <span class="sl-dot{"  sl-dot-active" if i == 0 else ""}"></span>'
        for i in range(n)
    )
    badge   = f'{akw} 과외 정보'
    tagline = '수학·영어·국어 과외를<br>지역별로 쉽게 찾아보세요'
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
        '          <div class="site-headline">\n'
        f'            <p class="headline-badge">{badge}</p>\n'
        f'            <h1 class="headline-main">{title}</h1>\n'
        '            <p class="headline-sub">우리 동네 과외, 지금 바로 찾아보세요</p>\n'
        '          </div>\n'
        f'          <p class="site-tagline">{tagline}</p>\n'
        '        </div>\n'
        '      </div>\n'
        '    </section>'
    )


def make_detail(akw: str, level: int, kw: str = '') -> str:
    imgs = []
    for pid, alt_base in DETAIL_IMGS:
        text = f'{akw} {kw} {alt_base}' if level == 4 and kw else f'{akw} {alt_base}'
        src  = cld_url(pid, text, w=480)
        imgs.append(
            f'        <img src="{src}" alt="{text}" '
            f'loading="lazy" decoding="async" width="480" height="918">'
        )
    imgs[0] = imgs[0].replace('loading="lazy"', 'loading="eager"')
    return (
        '    <section class="detail-section">\n'
        '      <div class="container">\n'
        + '\n'.join(imgs) + '\n'
        '      </div>\n'
        '    </section>'
    )


def make_location(level: int, loc_kw: str, dong_loc: dict, loc_ids: dict, akw: str) -> str:
    if level == 1:
        return ''
    key = dong_loc.get(loc_kw)
    if not key:
        return ''
    pid = loc_ids.get(key)
    if not pid:
        return ''
    text = f'{akw} 위치사진1'
    src  = cld_url(pid, text, w=500, h=281, crop='fill')
    return (
        '    <section class="section">\n'
        '      <div class="container">\n'
        f'        <img src="{src}" alt="{akw} 위치사진1" '
        f'loading="lazy" decoding="async" width="500" height="281">\n'
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


def make_region_list(level: int, do: str, sigu: str, loc_kw: str,
                     hierarchy: dict, gwae_kws: list) -> str:
    if level == 4:
        return ''

    if level == 1:
        sigus = sorted(hierarchy.get(do, {}).keys())
        items = '\n'.join(
            f'            <li><a href="/과외/{do}/{s}/">{s} 과외</a></li>' for s in sigus
        )
        h2 = f'{DO_SHORT.get(do, do)} 지역별 과외 안내'
    elif level == 2:
        loc_kws = hierarchy.get(do, {}).get(sigu, [])
        items = '\n'.join(
            f'            <li><a href="/과외/{do}/{sigu}/{lk}/">{lk} 과외</a></li>'
            for lk in sorted(loc_kws)
        )
        h2 = f'{sigu} 지역별 과외 안내'
    else:  # level 3
        items = '\n'.join(
            f'            <li><a href="/과외/{do}/{sigu}/{loc_kw}/{k}/">{k}</a></li>'
            for k in gwae_kws
        )
        h2 = f'{loc_kw} 과외 키워드별 안내'

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


def make_back_nav(level: int, do: str, sigu: str, loc_kw: str, kw: str) -> str:
    links = []
    if level == 4:
        links.append(f'<a href="/과외/{do}/{sigu}/{loc_kw}/">{loc_kw} 과외 목록</a>')
    if level >= 3:
        links.append(f'<a href="/과외/{do}/{sigu}/">{sigu} 과외 목록</a>')
    if level >= 2:
        links.append(f'<a href="/과외/{do}/">{do} 과외 목록</a>')
    links.append('<a href="/과외/">전국 과외 목록</a>')

    links_html = '\n'.join(f'        {l}' for l in links)
    return (
        '    <section class="section">\n'
        '      <div class="container">\n'
        '        <h2 class="section-title">상위 지역 과외 목록</h2>\n'
        '        <nav class="back-nav" aria-label="상위 지역 탐색">\n'
        f'{links_html}\n'
        '        </nav>\n'
        '      </div>\n'
        '    </section>'
    )


# ══════════════════════════════════════════════════════════════════════
# JSON-LD
# ══════════════════════════════════════════════════════════════════════

def make_json_ld(level: int, do: str, sigu: str, loc_kw: str, kw: str,
                 title: str, desc: str, canon: str, og_img: str, data: dict) -> str:
    crumbs = [
        {'@type': 'ListItem', 'position': 1, 'name': '홈', 'item': f'{SITE}/'},
        {'@type': 'ListItem', 'position': 2, 'name': '과외', 'item': f'{SITE}/과외/'},
    ]
    if level >= 1:
        crumbs.append({'@type': 'ListItem', 'position': 3, 'name': do, 'item': f'{SITE}/과외/{do}/'})
    if level >= 2:
        crumbs.append({'@type': 'ListItem', 'position': 4, 'name': sigu, 'item': f'{SITE}/과외/{do}/{sigu}/'})
    if level >= 3:
        crumbs.append({'@type': 'ListItem', 'position': 5, 'name': loc_kw, 'item': f'{SITE}/과외/{do}/{sigu}/{loc_kw}/'})
    if level == 4:
        crumbs.append({'@type': 'ListItem', 'position': 6, 'name': kw, 'item': f'{SITE}/과외/{do}/{sigu}/{loc_kw}/{kw}/'})

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
            'datePublished': date.today().isoformat(),
            'dateModified': date.today().isoformat(),
            'author': {'@type': 'Organization', 'name': BRAND, 'url': f'{SITE}/'},
            'publisher': {
                '@type': 'Organization',
                'name': BRAND,
                'url': f'{SITE}/',
                'logo': {'@type': 'ImageObject', 'url': f'{SITE}/images/로고.jpg', 'width': 200, 'height': 200},
            },
            'mainEntityOfPage': {'@type': 'WebPage', '@id': canon},
            'isPartOf': {'@type': 'WebSite', '@id': f'{SITE}/#website'},
            'inLanguage': 'ko-KR',
        },
        {'@type': 'WebSite', '@id': f'{SITE}/#website', 'url': f'{SITE}/', 'name': BRAND, 'inLanguage': 'ko-KR'},
        {'@type': 'BreadcrumbList', 'itemListElement': crumbs},
    ]
    if faq_items:
        graph.append({'@type': 'FAQPage', 'mainEntity': faq_items})

    return json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=2)


# ══════════════════════════════════════════════════════════════════════
# HEAD
# ══════════════════════════════════════════════════════════════════════

def make_head(title: str, desc: str, canon: str, og_img: str,
              kw_meta: str, jld: str, lcp_img: str = '') -> str:
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
  <meta name="google-site-verification" content="E5MOZUCWsEWJ8-gXXLa_GiL1vDgL6m5hjGJCYpn-U9M">
  <meta name="naver-site-verification" content="6dbb42d9ed3cf3f460292fa31f398e73b2689eb4">
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
  <link rel="preconnect" href="https://nam.veta.naver.com">
{preload_lcp}  <link rel="stylesheet" href="/css/style.css">
  <style>
  .hero-img-wrap{{position:relative;overflow:hidden;aspect-ratio:1/1;border-radius:20px;box-shadow:0 8px 32px rgba(0,0,0,.12)}}
  .sl-track{{position:absolute;inset:0;display:flex;height:100%;transition:transform .45s cubic-bezier(.4,0,.2,1);will-change:transform}}
  .slide{{flex:0 0 100%;height:100%;overflow:hidden}}
  .slide img{{width:100%;height:100%;object-fit:cover;display:block}}
  .sl-dots{{position:absolute;bottom:10px;left:50%;transform:translateX(-50%);display:flex;gap:6px;z-index:2}}
  .sl-dot{{width:7px;height:7px;border-radius:50%;background:rgba(255,255,255,.5);transition:background .3s,transform .3s;cursor:pointer}}
  .sl-dot-active{{background:#F97316;transform:scale(1.35)}}
  .sl-arrow{{position:absolute;top:50%;transform:translateY(-50%);background:rgba(255,255,255,.88);border:none;border-radius:50%;width:34px;height:34px;font-size:20px;line-height:1;cursor:pointer;z-index:3;display:flex;align-items:center;justify-content:center;color:#444;box-shadow:0 2px 8px rgba(0,0,0,.18);transition:opacity .2s}}
  .sl-arrow:hover{{opacity:.9}}
  .sl-prev{{left:8px}}
  .sl-next{{right:8px}}
  .detail-section .container{{display:flex;flex-direction:column;align-items:center;gap:0}}
  .detail-section img{{width:100%;max-width:680px;height:auto;display:block}}
  .content-list{{list-style:none;padding:0;margin:.8rem 0 0;display:grid;gap:.5rem}}
  .content-list li{{background:#fff8f3;border-left:3px solid #F97316;padding:.7rem 1rem;border-radius:0 8px 8px 0;font-size:.9rem;line-height:1.6;color:#333}}
  .info-table{{width:100%;border-collapse:collapse;margin:.8rem 0 0;border-radius:8px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.08)}}
  .info-table th{{background:#F97316;color:#fff;padding:.6rem 1rem;text-align:left;font-size:.85rem;font-weight:600;white-space:nowrap;width:7em}}
  .info-table td{{padding:.65rem 1rem;font-size:.9rem;border-bottom:1px solid #f0f0f0;color:#333;word-break:keep-all}}
  .info-table tr:last-child td{{border-bottom:none}}
  .compare-table{{width:100%;border-collapse:collapse;margin:.8rem 0 0;border-radius:8px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.08);font-size:.85rem}}
  .compare-table thead th{{background:#F97316;color:#fff;padding:.65rem .8rem;text-align:center;font-weight:600}}
  .compare-table tbody td{{padding:.6rem .8rem;border-bottom:1px solid #f0f0f0;color:#333;text-align:center;vertical-align:top}}
  .compare-table tbody tr:nth-child(even){{background:#fafafa}}
  .compare-table tbody tr:last-child td{{border-bottom:none}}
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

def make_html(level: int, do: str, sigu: str, loc_kw: str, kw: str,
              data: dict, titles: list, hierarchy: dict, gwae_kws: list,
              dong_loc: dict, loc_ids: dict) -> str:

    page_key = f'과외/{do}/{sigu}/{loc_kw}/{kw}'
    tv       = pick_title(titles, page_key)
    title    = build_title(level, do, sigu, loc_kw, kw, tv)
    desc     = data.get('meta', '')
    kw_meta  = build_kw_meta(level, do, sigu, loc_kw, kw)
    akw      = get_akw(level, do, sigu, loc_kw)

    if level == 1: canon = f'{SITE}/과외/{do}/'
    elif level == 2: canon = f'{SITE}/과외/{do}/{sigu}/'
    elif level == 3: canon = f'{SITE}/과외/{do}/{sigu}/{loc_kw}/'
    else:            canon = f'{SITE}/과외/{do}/{sigu}/{loc_kw}/{kw}/'

    og_img  = og_image(akw, level, kw)
    lcp_img = first_slide_url(akw, level, kw)
    jld     = make_json_ld(level, do, sigu, loc_kw, kw, title, desc, canon, og_img, data)
    head    = make_head(title, desc, canon, og_img, kw_meta, jld, lcp_img)

    code      = DO_CODE.get(do, 'B10')
    rows      = get_academies(level=level, code=code, si=sigu or None, dong=loc_kw or None, grade=None)
    area_name = loc_kw or sigu or DO_SHORT.get(do, do)
    card_html = make_card_section(rows, area_name)

    h2_s1 = f'{loc_kw} {kw}' if level == 4 else f'{akw} 과외'
    h2_s5 = f'{loc_kw} {kw} 커리큘럼' if level == 4 else f'{akw} 과외 커리큘럼'

    s1 = render_section1({**data.get('section1', {}), 'h2': h2_s1})
    s2 = render_list_section(data.get('section2', {}))
    s3 = render_section3(data.get('section3', {}))
    s4 = render_section4(data.get('section4', {}))
    s5 = render_list_section({**data.get('section5', {}), 'h2': h2_s5})
    s6 = render_list_section(data.get('section6', {}))
    s7 = render_list_section(data.get('section7', {}))
    s8 = render_section8(data.get('section8', {}))

    hero     = make_hero(akw, level, kw, title)
    detail   = make_detail(akw, level, kw)
    location = make_location(level, loc_kw, dong_loc, loc_ids, akw)
    region   = make_region_list(level, do, sigu, loc_kw, hierarchy, gwae_kws)
    backnav  = make_back_nav(level, do, sigu, loc_kw, kw)

    sections = '\n\n'.join(filter(None, [
        hero, detail, location, s1, s2, s3, s4, s5,
        card_html, s6, s7, s8, region, backnav,
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
    </div>
  </header>

  <main>
    <article>

{sections}

    </article>
  </main>

  <footer class="site-footer">
    <div class="container footer-inner">
      <p class="footer-slogan">아이들의 성장을 응원합니다</p>
      <p class="footer-sub">전국 동네 과외 정보를 정성껏 모아드립니다</p>
      <div class="footer-divider"></div>
      <p class="footer-info">
        <span>대표번호 <a href="tel:010-3952-5815">010-3952-5815</a></span>
        <span class="sep"> | </span>
        <span>대표자명 에너지+</span>
        <span class="sep"> | </span>
        <span>이메일 <a href="mailto:info@energyplus.kr">info@energyplus.kr</a></span>
      </p>
      <p class="footer-contact">과외 등록 문의는 이메일로 부탁드립니다.</p>
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
    var tx=0;
    wrap.addEventListener('touchstart',function(e){{tx=e.touches[0].clientX;}},{{passive:true}});
    wrap.addEventListener('touchend',function(e){{
      var dx=e.changedTouches[0].clientX-tx;
      if(Math.abs(dx)>40)go(dx<0?idx+1:idx-1);
    }});
  }})();
  </script>
  <script type="text/javascript" src="//wcs.pstatic.net/wcslog.js" async></script>
  <script type="text/javascript">
  if(!wcs_add) var wcs_add = {{}};
  wcs_add["wa"] = "143ec0f7d1fa77";
  if(window.wcs) {{
    wcs_do();
  }}
  </script>

</body>
</html>'''


# ══════════════════════════════════════════════════════════════════════
# 메인
# ══════════════════════════════════════════════════════════════════════

def main():
    print('데이터 로드 중...')
    titles    = load_titles()
    gwae_kws  = load_gwae_keywords()
    regions   = load_gwae_regions()
    hierarchy = build_hierarchy(regions)
    loc_ids   = load_location_ids()
    dong_loc  = load_dong_loc_map()
    print(f'  타이틀: {len(titles)}개 / 지역: {len(regions)}개 / 키워드: {len(gwae_kws)}개')

    count = skip = 0

    for result_path in sorted(BODUN.rglob('result.html')):
        rel   = result_path.relative_to(BODUN).parts[:-1]
        level = len(rel)

        do     = rel[0] if len(rel) >= 1 else ''
        sigu   = rel[1] if len(rel) >= 2 else ''
        loc_kw = rel[2] if len(rel) >= 3 else ''
        kw     = rel[3] if len(rel) >= 4 else ''

        try:
            with open(result_path, encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f'  [JSON 오류] {result_path.relative_to(BODUN)}: {e}')
            skip += 1
            continue

        if rel:
            out_path = BASE_OUT / Path(*rel) / 'index.html'
        else:
            out_path = BASE_OUT / 'index.html'
        out_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            html = make_html(level, do, sigu, loc_kw, kw, data, titles,
                             hierarchy, gwae_kws, dong_loc, loc_ids)
            out_path.write_text(html, encoding='utf-8')
            label = '/'.join(rel) if rel else '루트'
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
