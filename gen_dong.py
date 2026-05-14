"""
gen_dong.py
===========
학원목록.txt 를 읽어 모든 동 단위 레벨3 index.html 을 생성합니다.
경로: /{도}/{시}/{동}/index.html
"""

import os
import urllib.parse
from collections import defaultdict

BASE     = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
LIST_FILE = os.path.join(BASE, '학원목록.txt')

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


def cloudinary_url(text):
    encoded = urllib.parse.quote(text, safe='')
    return f'{CLOUDINARY_BASE}/l_text:NanumGothic_45_bold:{encoded},co_white,g_south_west,x_30,y_30,b_rgb:00000066{CLOUDINARY_IMG}'


def is_dong_kw(kw):
    for e in ('특별시', '광역시', '특별자치도', '자치도', '자치시'):
        if kw.endswith(e):
            return False
    if kw.endswith('구') and not kw.endswith('지구'):
        return False
    if kw.endswith('시'):
        return False
    return True


# ── 학원목록.txt 파싱 ────────────────────────────────────────────────
# dong_map: {(도, 시): [동키워드, ...]}  순서 보존, 중복 제거
dong_map  = defaultdict(list)
dong_seen = set()
cur_do = cur_si = None

with open(LIST_FILE, encoding='utf-8') as f:
    for line in f:
        cols = line.rstrip('\n').split('\t')
        if len(cols) < 4:
            continue
        do   = cols[0].strip()
        si   = cols[1].strip()
        dong = cols[3].strip()

        if do:  cur_do = do
        if si:  cur_si = si
        if not (cur_do and cur_si):
            continue

        if dong and is_dong_kw(dong):
            k = (cur_do, cur_si, dong)
            if k not in dong_seen:
                dong_seen.add(k)
                dong_map[(cur_do, cur_si)].append(dong)


def make_html(do, si, dong):
    do_s  = DO_SHORT.get(do, do)
    cld   = cloudinary_url(f'{do_s} {si} {dong} 학원')
    canon = f'https://energyplus.kr/{do}/{si}/{dong}/'
    desc  = f'{dong} 수학학원·영어학원 정보를 안내합니다. {si} {dong} 학원을 한눈에 찾아보세요. 초등·중등·고등 내신 학원부터 수능 대비 학원까지 {dong} 전체 학원 정보 모음집.'
    kw    = f'{dong} 학원, {dong} 수학학원, {dong} 영어학원, {si} {dong} 학원, {dong} 학원 추천, {do_s} {dong} 학원'

    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>{dong} 학원 모음집 | 동네학원 모여라</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{kw}">
  <meta name="author" content="동네학원 모여라">
  <meta name="robots" content="index, follow">
  <meta name="naver-site-verification" content="6c8552333b0e48ee6249eeecfdd0e6c5c62384eb">

  <meta property="og:type" content="article">
  <meta property="og:title" content="{dong} 학원 모음집 | 동네학원 모여라">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canon}">
  <meta property="og:site_name" content="동네학원 모여라">
  <meta property="og:locale" content="ko_KR">
  <meta property="og:image" content="{cld}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{dong} 학원 모음집 | 동네학원 모여라">
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
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@800&display=swap" rel="stylesheet">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Article",
        "@id": "{canon}#article",
        "headline": "{dong} 학원 모음집",
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
          {{"@type": "ListItem", "position": 4, "name": "{dong}", "item": "{canon}"}}
        ]
      }},
      {{
        "@type": "Person",
        "@id": "https://energyplus.kr/#editor",
        "name": "전국학원팀 편집자",
        "jobTitle": "교육 콘텐츠 편집자",
        "worksFor": {{"@id": "https://energyplus.kr/#organization"}},
        "knowsAbout": ["{dong} 학원", "{dong} 수학학원", "{dong} 영어학원", "{si} 학원"]
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

  <link rel="stylesheet" href="/css/style.css">
</head>
<body>

  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="logo-wrap">
        <picture>
          <source srcset="/images/로고.webp" type="image/webp">
          <img src="/images/로고.jpg" alt="동네학원 모여라 로고" class="logo-img">
        </picture>
        <span class="logo-text">동네학원 모여라</span>
      </a>
      <nav class="site-nav">
        
      </nav>
    </div>
  </header>

  <section class="hero">
    <div class="hero-inner">
      <div class="hero-img-wrap">
        <img src="{cld}" alt="{dong} 학원 실제 내부" class="hero-img">
      </div>
      <div class="hero-text">
        <div class="site-headline">
          <p class="headline-badge">{do} {si} {dong} 학원 정보</p>
          <h1 class="headline-main">{dong} 학원<br>모음집</h1>
          <p class="headline-sub">우리 동네 학원, 지금 바로 찾아보세요</p>
        </div>
        <p class="site-tagline">초등·중등·고등 학원을<br>학년별로 쉽게 찾아보세요</p>
      </div>
    </div>
  </section>

  <main>
    <article>

      <section class="section">
        <div class="container">
          <h2 class="section-title">{dong} 학원 학년별 안내</h2>
          <p class="section-desc">학년을 선택하시면 해당 학년의 {dong} 학원 정보를 확인하실 수 있습니다.</p>
          <ul class="region-list">
            <li><a href="/{do}/{si}/{dong}/초등/">초등</a></li>
            <li><a href="/{do}/{si}/{dong}/중등/">중등</a></li>
            <li><a href="/{do}/{si}/{dong}/고등/">고등</a></li>
            <li><a href="/{do}/{si}/{dong}/메인학원/">메인학원</a></li>
          </ul>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">
            <span style="background:#fff7ed;color:#ea580c;border:1.5px solid #fdba74;border-radius:999px;padding:6px 16px;font-size:0.97rem;font-weight:700;">#{dong}</span>
            <span style="background:#fff7ed;color:#ea580c;border:1.5px solid #fdba74;border-radius:999px;padding:6px 16px;font-size:0.97rem;font-weight:700;">#{dong}학원</span>
            <span style="background:#fff7ed;color:#ea580c;border:1.5px solid #fdba74;border-radius:999px;padding:6px 16px;font-size:0.97rem;font-weight:700;">#수학학원</span>
            <span style="background:#fff7ed;color:#ea580c;border:1.5px solid #fdba74;border-radius:999px;padding:6px 16px;font-size:0.97rem;font-weight:700;">#영어학원</span>
            <span style="background:#fff7ed;color:#ea580c;border:1.5px solid #fdba74;border-radius:999px;padding:6px 16px;font-size:0.97rem;font-weight:700;">#영수학원</span>
            <span style="background:#fff7ed;color:#ea580c;border:1.5px solid #fdba74;border-radius:999px;padding:6px 16px;font-size:0.97rem;font-weight:700;">#{si}학원</span>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <h2 class="section-title">상위 지역 학원 목록</h2>
          <p class="section-desc">더 넓은 지역의 학원 정보를 확인하세요.</p>
          <nav class="back-nav" aria-label="상위 지역 탐색">
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


# ── 생성 ──────────────────────────────────────────────────────────────
count = 0
for (do, si), dongs in sorted(dong_map.items()):
    for dong in dongs:
        path = os.path.join(BASE, do, si, dong, 'index.html')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(make_html(do, si, dong))
        count += 1
        print(f'생성: {do}/{si}/{dong}')

print(f'\n완료: {count}개 페이지')
