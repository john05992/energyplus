import os
import urllib.parse

base = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
DO = '전북특별자치도'
DO_SHORT = '전북'
CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
CLOUDINARY_IMG = '/v1778460866/1_fyhcx0.webp'

def cloudinary_url(text):
    encoded = urllib.parse.quote(text, safe='')
    return f'{CLOUDINARY_BASE}/l_text:NanumGothic_45_bold:{encoded},co_white,g_south_west,x_30,y_30,b_rgb:00000066{CLOUDINARY_IMG}'

jeonbuk = {
    '전주시': {
        'subs': ['서신동', '서신', '중화산동', '송천동', '전주장동', '혁신동'],
        'feature': '전북특별자치도 전주시는 서신동과 송천동을 중심으로 전북 최대 학원가가 형성된 지역입니다. 전북대학교와 전주교육대학교가 위치한 교육도시 특성상 대학 출신 전문 강사들이 풍부하며, 전북특별자치도청 소재지로 공무원·전문직 가정 비율이 높아 내신 전문 학원부터 수능 심화 학원까지 전북 내 가장 다양한 학원들이 운영되고 있습니다. 혁신도시 개발로 수도권 공공기관 이전 가정이 늘어나며 소수정예 관리형 학원 수요도 빠르게 성장하고 있습니다.',
        'faq': [
            ('전주 서신동 학원가의 특징은 무엇인가요?', '서신동은 전주 핵심 주거지로 소수정예 관리형 학원들이 집중되어 있습니다. 전북대·전주교대 출신 강사들이 운영하는 전문 학원들이 많으며, 전주 지역 주요 고교 내신 기출 자료를 보유한 학원들이 내신 대비에서 강점을 보입니다. 중화산동과 함께 전주 서부 최대 학원가를 형성하고 있습니다.'),
            ('전주 송천동과 혁신동 학원은 어떤가요?', '송천동은 전주 북부 주거지로 내신 전문 학원들이 안정적으로 운영됩니다. 혁신동은 수도권 공공기관 이전 가정이 밀집한 지역으로 소수정예 관리형 학원 수요가 높으며, 최신 커리큘럼을 갖춘 학원들에 대한 선호도가 강합니다.'),
            ('전주에서 수능 심화 준비가 가능한가요?', '서신동과 효자동에 수능 종합 학원들이 운영됩니다. 전북대 이공계 출신 강사들의 수학·과학 심화 수업이 강점이며, 부족한 심화 과목은 EBS 인강과 병행하는 방식이 효과적입니다.'),
        ],
        'extra': [
            {'h2': '서신·송천 학원가 분석', 'content': '서신동·중화산동 주거지와 송천동 아파트 단지에 전주 최대 학원가가 형성되어 있습니다. 전주고·전주여고·완산고 등 주요 고교 내신 기출 자료를 방대하게 보유한 학원들이 내신 직전 집중 특강에서 높은 효율을 보이며, 전북대·전주교대 출신 강사들의 전문 학원들이 수업 수준을 끌어올리고 있습니다. 혁신동은 공공기관 이전 가정의 안정적인 수요를 바탕으로 신규 학원들이 빠르게 성장 중입니다.', 'tip': None},
            {'h2': '전북대 인근 교육 환경', 'content': '전북대학교와 전주교대가 위치한 전주는 전라권 내에서 가장 우수한 강사 풀을 보유하고 있습니다. 이공계 대학원생 출신 강사들의 수능 수학·과학 심화 수업과 교대 출신 강사들의 국어·영어 수업이 강점입니다. 전북대 의대·사범대 진학을 목표로 하는 학생들을 위한 전문 입시 컨설팅 학원도 서신동과 효자동 일대에 운영됩니다.', 'tip': '전북대 의대 진학 목표 학생은 중1부터 수학 심화 + 과학탐구 병행 학원을 선택하세요.'},
            {'h2': '수능 전략별 학원 선택법', 'content': '전주 학원들은 수능 준비 유형별로 특화된 곳을 선택하는 것이 중요합니다. 문과는 국어·영어 독해 전문 학원과 사회탐구 단과를 조합하고, 이과는 수학 심화와 물화생지 전담 강사 학원을 우선 선택하세요. 수시 학생부 종합 전형을 목표로 한다면 고1부터 세특 관리와 독서 활동을 함께 설계하는 학원이 유리하며, 논술은 전북대 기출 논술 분석과 첨삭을 반복하는 학원을 고2부터 시작하는 것이 효과적입니다.', 'tip': None},
        ],
    },
}


def make_region_list(si, subs):
    links = '\n          '.join(
        f'<li><a href="/{DO}/{si}/{s}/">{s}</a></li>' for s in subs
    )
    return f'<ul class="region-list">\n          {links}\n          </ul>'


def make_extra_sections(extra):
    html = ''
    for item in extra:
        tip_html = f'\n          <p class="tip-box">{item["tip"]}</p>' if item.get('tip') else ''
        html += f'''
      <section class="section">
        <div class="container">
          <h2 class="section-title">{item["h2"]}</h2>
          <p class="section-desc">{item["content"]}</p>{tip_html}
        </div>
      </section>
'''
    return html


def make_html(si, data):
    subs = data['subs']
    feature = data['feature']
    faqs = data['faq']
    extra = data['extra']

    cld = cloudinary_url(f'{DO_SHORT} {si} 학원 실제내부')
    desc = f'{si} 영어학원·수학학원 정보를 동별로 안내합니다. {", ".join(subs[:3])} 등 {si} 전 지역 학원을 한눈에 찾아보세요. 내신 전문 학원부터 수능 대비 학원까지 지역별로 확인하실 수 있습니다.'
    keywords = f'{si} 수학학원, {si} 영어학원, {DO_SHORT} {si} 학원, {si} 학원 추천, {si} 내신 학원, {si} 학원 정보'

    region_list_html = make_region_list(si, subs)
    extra_html = make_extra_sections(extra)

    faq_items = '\n          '.join(
        f'<div class="faq-item"><p class="faq-q">Q. {q}</p><p class="faq-a">{a}</p></div>'
        for q, a in faqs
    )
    faq_schema = ',\n        '.join(
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in faqs
    )

    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>{si} 수학학원 영어학원 모음집 | 동네학원 모여라</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="동네학원 모여라">
  <meta name="robots" content="index, follow">
  <meta name="naver-site-verification" content="6c8552333b0e48ee6249eeecfdd0e6c5c62384eb">

  <meta property="og:type" content="article">
  <meta property="og:title" content="{si} 수학학원 영어학원 모음집 | 동네학원 모여라">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://energyplus.kr/{DO}/{si}/">
  <meta property="og:site_name" content="동네학원 모여라">
  <meta property="og:locale" content="ko_KR">
  <meta property="og:image" content="{cld}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{si} 수학학원 영어학원 모음집 | 동네학원 모여라">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{cld}">
  <meta name="theme-color" content="#F97316">
  <link rel="canonical" href="https://energyplus.kr/{DO}/{si}/">

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
        "@id": "https://energyplus.kr/{DO}/{si}/#article",
        "headline": "{si} 수학학원 영어학원 모음집",
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
        "mainEntityOfPage": {{"@type": "WebPage", "@id": "https://energyplus.kr/{DO}/{si}/"}},
        "inLanguage": "ko-KR"
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type": "ListItem", "position": 1, "name": "홈", "item": "https://energyplus.kr/"}},
          {{"@type": "ListItem", "position": 2, "name": "{DO}", "item": "https://energyplus.kr/{DO}/"}},
          {{"@type": "ListItem", "position": 3, "name": "{si}", "item": "https://energyplus.kr/{DO}/{si}/"}}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {faq_schema}
        ]
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
        <a href="/학원정보/">학원정보</a>
      </nav>
    </div>
  </header>

  <section class="hero">
    <div class="hero-inner">
      <div class="hero-img-wrap">
        <img src="{cld}" alt="{si} 학원 실제 내부" class="hero-img">
      </div>
      <div class="hero-text">
        <div class="site-headline">
          <p class="headline-badge">{DO} {si} 학원 정보</p>
          <h1 class="headline-main">{si}<br>수학학원 영어학원 모음집</h1>
          <p class="headline-sub">우리 동네 학원, 지금 바로 찾아보세요</p>
        </div>
        <p class="site-tagline">초등·중등·고등 학원을<br>동별로 쉽게 찾아보세요</p>
      </div>
    </div>
  </section>

  <main>
    <article>

      <section class="section">
        <div class="container">
          <h2 class="section-title">{si} 영어학원 수학학원 지역별 안내</h2>
          <p class="section-desc">동을 선택하시면 해당 지역의 학원 정보를 확인하실 수 있습니다.</p>
          {region_list_html}
        </div>
      </section>

      <section class="section">
        <div class="container">
          <h2 class="section-title">학원 특징</h2>
          <p class="section-desc">{feature}</p>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <h2 class="section-title">자주 묻는 질문</h2>
          <p class="section-desc">학원 선택에 고민이 있으신가요? 자주 묻는 질문을 정리했습니다.</p>
          <div class="faq-list">
          {faq_items}
          </div>
        </div>
      </section>

{extra_html}
      <section class="section">
        <div class="container">
          <h2 class="section-title">상위 지역 학원 목록</h2>
          <p class="section-desc">더 넓은 지역의 학원 정보를 확인하세요.</p>
          <nav class="back-nav" aria-label="상위 지역 탐색">
            <a href="/{DO}/">{DO} 학원 목록</a>
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


count = 0
for si, data in jeonbuk.items():
    path = os.path.join(base, DO, si, 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(make_html(si, data))
    count += 1
    print(f'생성: {DO}/{si}')

print(f'\n완료: {count}개 페이지')
