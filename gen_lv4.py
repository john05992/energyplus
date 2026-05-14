"""
gen_lv4.py
==========
레벨4 index.html 생성기 (학년 페이지)
경로: /{도}/{시}/{동}/{학년}/index.html
학년 4종: 초등 / 중등 / 고등 / 메인학원

TEST_ONLY = True  → TEST_TARGET 에 지정한 동만 생성
TEST_ONLY = False → 학원목록.txt 전체 동 생성
"""

import os
import urllib.parse
from collections import defaultdict

BASE      = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
LIST_FILE = os.path.join(BASE, '학원목록.txt')
KW_FILE   = os.path.join(BASE, '학년학원키워드.txt')

# ── 테스트 모드 ──────────────────────────────────────────────────
TEST_ONLY   = True
TEST_TARGET = [('강원도', '강릉시', '강릉교동')]  # 여러 개 추가 가능

CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
CLOUDINARY_IMG  = '/v1778460866/1_fyhcx0.webp'

DO_SHORT = {
    '서울특별시':     '서울',
    '경기도':         '경기',
    '인천광역시':     '인천',
    '부산광역시':     '부산',
    '대구광역시':     '대구',
    '대전광역시':     '대전',
    '광주광역시':     '광주',
    '울산광역시':     '울산',
    '강원도':         '강원',
    '충청남도':       '충남',
    '충청북도':       '충북',
    '전북특별자치도': '전북',
    '경상북도':       '경북',
    '경상남도':       '경남',
    '세종시':         '세종',
    '제주도':         '제주',
}

# 메인학원 전용 키워드 (학년학원키워드.txt에 없으므로 여기서 정의)
MAIN_KEYWORDS = [
    '수학학원',
    '영어학원',
    '국어학원',
    '영수학원',
    '수능 수학학원',
    '수능 영어학원',
    '내신 수학학원',
    '내신 영어학원',
]

GRADE_LIST = ['초등', '중등', '고등', '메인학원']


def cloudinary_url(text):
    encoded = urllib.parse.quote(text, safe='')
    return (
        f'{CLOUDINARY_BASE}/w_800,q_auto,f_auto'
        f'/l_text:NanumGothic_45_bold:{encoded}'
        f',co_white,g_south_west,x_30,y_30,b_rgb:00000066'
        f'{CLOUDINARY_IMG}'
    )


def load_keywords():
    """학년학원키워드.txt → {학년: [키워드, ...]}"""
    grade_kw = defaultdict(list)
    with open(KW_FILE, encoding='utf-8') as f:
        for line in f:
            parts = line.rstrip('\n').split('\t')
            if len(parts) >= 2:
                kw    = parts[0].strip()
                grade = parts[1].strip()
                if kw and grade:
                    grade_kw[grade].append(kw)
    grade_kw['메인학원'] = MAIN_KEYWORDS
    return dict(grade_kw)


def is_dong_kw(kw):
    for e in ('특별시', '광역시', '특별자치도', '자치도', '자치시'):
        if kw.endswith(e):
            return False
    if kw.endswith('구') and not kw.endswith('지구'):
        return False
    if kw.endswith('시'):
        return False
    return True


def load_dong_list():
    """학원목록.txt → [(도, 시, 동), ...] 순서 보존 중복 제거"""
    items = []
    seen  = set()
    cur_do = cur_si = None
    with open(LIST_FILE, encoding='utf-8') as f:
        for line in f:
            cols = line.rstrip('\n').split('\t')
            if len(cols) < 4:
                continue
            do   = cols[0].strip()
            si   = cols[1].strip()
            dong = cols[3].strip()
            if do: cur_do = do
            if si: cur_si = si
            if not (cur_do and cur_si and dong):
                continue
            if not is_dong_kw(dong):
                continue
            k = (cur_do, cur_si, dong)
            if k not in seen:
                seen.add(k)
                items.append(k)
    return items


def make_html(do, si, dong, grade, keywords):
    do_s = DO_SHORT.get(do, do)

    # Cloudinary 이미지 텍스트 (레벨4: [동명] [학년] 학원 실제내부)
    cld_text = f'{dong} 학원 실제내부' if grade == '메인학원' else f'{dong} {grade} 학원 실제내부'
    cld      = cloudinary_url(cld_text)
    canon    = f'https://energyplus.kr/{do}/{si}/{dong}/{grade}/'

    # 학년별 텍스트 변수
    if grade == '메인학원':
        title      = f'{dong} 학원 모음집 | 동네학원 모여라'
        headline   = f'{dong} 학원 모음집'
        desc       = (f'{dong} 수학학원·영어학원·국어학원 정보를 안내합니다. '
                      f'{si} {dong} 대표 학원을 한눈에 찾아보세요. '
                      f'수능 대비 학원부터 내신 학원까지 {dong} 전체 학원 정보 모음집.')
        kw_meta    = (f'{dong} 학원, {dong} 수학학원, {dong} 영어학원, '
                      f'{si} 학원, {dong} 학원 추천, {do_s} {dong} 학원')
        badge      = f'{do} {si} {dong} 학원 정보'
        h1_main    = f'{dong} 학원<br>모음집'
        tagline    = '수학·영어·국어 학원을<br>키워드별로 쉽게 찾아보세요'
        h2_list    = f'{dong} 학원 키워드별 안내'
        h2_desc    = f'키워드를 선택하시면 해당 키워드의 {dong} 학원 정보를 확인하실 수 있습니다.'
        acad_h2    = f'{dong} 인기학원 모음'
        acad_p     = f'{dong} 수학·영어·국어 학원 16곳을 모았습니다.'
        knows      = f'"{dong} 학원", "{dong} 수학학원", "{dong} 영어학원", "{si} 학원"'
        tags       = [f'#{dong}', f'#{dong}학원', '#수학학원', '#영어학원', '#영수학원', f'#{si}학원']
    else:
        title      = f'{dong} {grade} 학원 모음집 | 동네학원 모여라'
        headline   = f'{dong} {grade} 학원 모음집'
        desc       = (f'{dong} {grade} 수학학원·영어학원 정보를 안내합니다. '
                      f'{si} {dong} {grade} 학원을 한눈에 찾아보세요. '
                      f'{grade} 수학·영어·국어 내신 학원부터 {grade} 영수학원까지 '
                      f'{dong} {grade} 전체 학원 정보 모음집.')
        kw_meta    = (f'{dong} {grade} 학원, {dong} {grade} 수학학원, '
                      f'{dong} {grade} 영어학원, {si} {grade} 학원, '
                      f'{dong} {grade} 학원 추천, {do_s} {dong} {grade}')
        badge      = f'{do} {si} {dong} {grade} 학원 정보'
        h1_main    = f'{dong} {grade} 학원<br>모음집'
        tagline    = f'{grade} 수학·영어·국어 학원을<br>키워드별로 쉽게 찾아보세요'
        h2_list    = f'{dong} {grade} 학원 키워드별 안내'
        h2_desc    = f'키워드를 선택하시면 해당 키워드의 {dong} {grade} 학원 정보를 확인하실 수 있습니다.'
        acad_h2    = f'{dong} {grade} 인기학원 모음'
        acad_p     = f'{dong} {grade} 수학·영어·국어 학원 16곳을 모았습니다.'
        knows      = f'"{dong} {grade} 학원", "{dong} {grade} 수학학원", "{dong} {grade} 영어학원", "{si} 학원"'
        tags       = [
            f'#{dong}{grade}', f'#{grade}수학학원', f'#{grade}영어학원',
            f'#{grade}영수학원', f'#{dong}학원', f'#{si}{grade}학원',
        ]

    li_items = '\n'.join(
        f'            <li><a href="/{do}/{si}/{dong}/{grade}/{kw}/">{kw}</a></li>'
        for kw in keywords
    )

    tag_html = '\n'.join(
        f'            <span style="background:#fff7ed;color:#ea580c;border:1.5px solid #fdba74;'
        f'border-radius:999px;padding:6px 16px;font-size:0.97rem;font-weight:700;">{t}</span>'
        for t in tags
    )

    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{kw_meta}">
  <meta name="author" content="동네학원 모여라">
  <meta name="robots" content="index, follow">
  <meta name="naver-site-verification" content="6c8552333b0e48ee6249eeecfdd0e6c5c62384eb">

  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canon}">
  <meta property="og:site_name" content="동네학원 모여라">
  <meta property="og:locale" content="ko_KR">
  <meta property="og:image" content="{cld}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{cld}">
  <meta name="theme-color" content="#F97316">
  <link rel="canonical" href="{canon}">

  <link rel="icon" href="/images/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16x16.png">
  <link rel="apple-touch-icon" href="/images/로고.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@800&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@800&display=swap" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@800&display=swap"></noscript>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Article",
        "@id": "{canon}#article",
        "headline": "{headline}",
        "description": "{desc}",
        "image": "{cld}",
        "datePublished": "2026-05-13",
        "dateModified": "2026-05-13",
        "author": {{"@type": "Organization", "name": "동네학원 모여라", "url": "https://energyplus.kr/"}},
        "publisher": {{
          "@type": "Organization",
          "name": "동네학원 모여라",
          "url": "https://energyplus.kr/",
          "logo": {{"@type": "ImageObject", "url": "https://energyplus.kr/images/로고.jpg", "width": 200, "height": 200}}
        }},
        "mainEntityOfPage": {{"@type": "WebPage", "@id": "{canon}"}},
        "inLanguage": "ko-KR"
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type": "ListItem", "position": 1, "name": "홈", "item": "https://energyplus.kr/"}},
          {{"@type": "ListItem", "position": 2, "name": "{do}", "item": "https://energyplus.kr/{do}/"}},
          {{"@type": "ListItem", "position": 3, "name": "{si}", "item": "https://energyplus.kr/{do}/{si}/"}},
          {{"@type": "ListItem", "position": 4, "name": "{dong}", "item": "https://energyplus.kr/{do}/{si}/{dong}/"}},
          {{"@type": "ListItem", "position": 5, "name": "{grade}", "item": "{canon}"}}
        ]
      }},
      {{
        "@type": "Person",
        "@id": "https://energyplus.kr/#editor",
        "name": "전국학원팀 편집자",
        "jobTitle": "교육 콘텐츠 편집자",
        "worksFor": {{"@id": "https://energyplus.kr/#organization"}},
        "knowsAbout": [{knows}]
      }},
      {{
        "@type": "Service",
        "@id": "https://energyplus.kr/#service",
        "serviceType": "TutoringService",
        "areaServed": {{"@type": "Country", "name": "South Korea"}},
        "offers": {{"@type": "Offer", "priceCurrency": "KRW", "priceRange": "100000-600000"}}
      }},
      {{
        "@type": "LocalBusiness",
        "@id": "https://energyplus.kr/#localbusiness",
        "name": "동네학원 모여라",
        "telephone": "+82-10-3952-5815",
        "address": {{"@type": "PostalAddress", "addressLocality": "전국", "addressCountry": "KR"}}
      }}
    ]
  }}
  </script>

  <link rel="preload" href="/css/style.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="/css/style.css"></noscript>
</head>
<body>

  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="logo-wrap">
        <picture>
          <source srcset="/images/로고.webp" type="image/webp">
          <img src="/images/로고.jpg" alt="동네학원 모여라 로고" class="logo-img" width="72" height="72">
        </picture>
        <span class="logo-text">동네학원 모여라</span>
      </a>
      <nav class="site-nav">
        <a href="/학원정보/">학원정보</a>
      </nav>
    </div>
  </header>

  <section class="hero">
    <div class="hero-inner">
      <div class="hero-img-wrap">
        <img src="{cld}" alt="{cld_text}" class="hero-img" fetchpriority="high">
      </div>
      <div class="hero-text">
        <div class="site-headline">
          <p class="headline-badge">{badge}</p>
          <h1 class="headline-main">{h1_main}</h1>
          <p class="headline-sub">우리 동네 학원, 지금 바로 찾아보세요</p>
        </div>
        <p class="site-tagline">{tagline}</p>
      </div>
    </div>
  </section>

  <main>
    <article>

      <section class="section">
        <div class="container">
          <h2 class="section-title">{h2_list}</h2>
          <p class="section-desc">{h2_desc}</p>
          <ul class="region-list">
{li_items}
          </ul>
        </div>
      </section>

      <!-- ACADEMY_SECTION_START -->
      <section class="section">
        <div class="container">
          <h2 class="section-title">{acad_h2}</h2>
          <p class="section-desc">{acad_p}</p>
          <div class="academy-grid">
          </div>
        </div>
      </section>
      <!-- ACADEMY_SECTION_END -->

      <section class="section">
        <div class="container">
          <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">
{tag_html}
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <h2 class="section-title">상위 지역 학원 목록</h2>
          <p class="section-desc">더 넓은 지역의 학원 정보를 확인하세요.</p>
          <nav class="back-nav" aria-label="상위 지역 탐색">
            <a href="/{do}/{si}/{dong}/">{dong} 학원 목록</a>
            <a href="/{do}/{si}/">{si} 학원 목록</a>
            <a href="/{do}/">{do} 학원 목록</a>
            <a href="/">전국학원 목록 보기</a>
          </nav>
        </div>
      </section>

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
        <span>대표자명 이나현</span>
        <span class="sep"> | </span>
        <span>이메일 <a href="mailto:info@energyplus.kr">info@energyplus.kr</a></span>
      </h4>
      <p class="footer-contact">학원 등록 문의는 이메일로 부탁드립니다.</p>
      <p class="footer-copy">&copy; 2026 동네학원 모여라. All rights reserved.</p>
    </div>
  </footer>

  <script type="text/javascript" src="//wcs.pstatic.net/wcslog.js"></script>
  <script type="text/javascript">
  if(!wcs_add) var wcs_add = {{}};
  wcs_add["wa"] = "1424ba4d85077d";
  if(window.wcs) {{
    wcs_do();
  }}
  </script>

</body>
</html>
'''


# ── 실행 ──────────────────────────────────────────────────────────
if __name__ == '__main__':
    grade_keywords = load_keywords()

    if TEST_ONLY:
        dong_list = TEST_TARGET
        print(f'[테스트 모드] 대상: {TEST_TARGET}')
    else:
        dong_list = load_dong_list()
        print(f'[전체 모드] 총 {len(dong_list)}개 동 처리 예정')

    count = 0
    for (do, si, dong) in dong_list:
        for grade in GRADE_LIST:
            keywords = grade_keywords.get(grade, [])
            path = os.path.join(BASE, do, si, dong, grade, 'index.html')
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(make_html(do, si, dong, grade, keywords))
            count += 1
            print(f'생성: {do}/{si}/{dong}/{grade}')

    print(f'\n완료: {count}개 페이지')
