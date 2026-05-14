import os
import urllib.parse

base = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
DO = '충청북도'
DO_SHORT = '충북'
CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
CLOUDINARY_IMG = '/v1778460866/1_fyhcx0.webp'

def cloudinary_url(text):
    encoded = urllib.parse.quote(text, safe='')
    return f'{CLOUDINARY_BASE}/l_text:NanumGothic_45_bold:{encoded},co_white,g_south_west,x_30,y_30,b_rgb:00000066{CLOUDINARY_IMG}'

chungbuk = {
    '청주시': {
        'subs': ['복대동', '하복대', '비하동', '복대', '가경동', '청주가경', '강서동', '개신동'],
        'feature': '충청북도 청주시는 복대동과 가경동을 중심으로 충북 최대 학원가가 형성된 지역입니다. 충북대학교와 청주교육대학교가 위치한 교육도시 특성상 대학 출신 전문 강사들이 풍부하며, 오창·오송 산업단지 개발로 수도권 이전 가정이 대거 유입되면서 학원 수준에 대한 눈높이가 빠르게 높아졌습니다. 복대동 전통 학원가와 가경동 신도시 학원가가 충북 최대 규모를 형성하며 경쟁하고 있습니다.',
        'faq': [
            ('청주 복대동 학원가의 특징은 무엇인가요?', '복대동은 청주 전통 핵심 학원가로 개원 10년 이상 검증된 학원들이 많습니다. 충북고·청주고·세광고 등 주요 고교 내신 기출 자료가 방대하게 축적되어 있으며, 내신 시험 직전 집중 특강 효율이 청주 내 최상위입니다.'),
            ('청주 가경동 학원은 복대동과 어떻게 다른가요?', '가경동은 청주 최대 신도시 주거지로 소수정예 관리형 학원들이 집중되어 있습니다. 오송·오창 이전 가정과 공무원 가정의 안정적인 수요를 바탕으로 최신 커리큘럼을 앞세운 학원들이 경쟁하며 수준이 빠르게 향상되고 있습니다.'),
            ('청주에서 수능 심화 준비가 가능한가요?', '복대동과 개신동에 수능 종합 학원들이 운영됩니다. 충북대 이공계 출신 강사들의 수학·과학 심화 수업이 강점이며, 부족한 심화 과목은 EBS 인강과 병행하는 방식이 효과적입니다.'),
        ],
        'extra': [
            {'h2': '복대·가경 학원가 분석', 'content': '복대동 전통 학원가와 가경동 신도시 학원가가 청주 최대 학원 시장을 양분하고 있습니다. 복대동은 개원 10년 이상 검증된 내신 전문 학원들이 충북 주요 고교 기출을 방대하게 보유하고 있고, 가경동은 오송·오창 이전 가정 수요에 맞춘 소수정예 학원들이 빠르게 성장하고 있습니다. 개신동과 산남동에도 소규모 관리형 학원들이 안정적으로 운영됩니다.', 'tip': None},
            {'h2': '충북대 인근 교육 환경', 'content': '충북대학교와 청주교대가 위치한 청주는 충청권 내에서 가장 우수한 강사 풀을 보유하고 있습니다. 이공계 대학원생 출신 강사들의 수능 수학·과학 심화 수업과 교대 출신 강사들의 국어·영어 수업이 강점입니다. 충북대 의대·사범대 진학을 목표로 하는 학생들을 위한 전문 입시 컨설팅 학원도 운영됩니다.', 'tip': '대학 인근 학원은 강사의 전공과 출신 학교를 미리 확인하면 수업 수준 판단에 도움이 됩니다.'},
            {'h2': '수능·내신 균형 전략', 'content': '청주 학원들은 고1·2 내신과 수능 병행 관리 커리큘럼을 표준으로 운영합니다. 고1은 내신 70%, 수능 기초 30% 비율로 균형을 잡고, 고2 2학기부터 수능 비중을 50%로 높이는 것이 일반적입니다. 고3 초반 수능 전 과목 체계를 완성하고, 내신 시험 2주 전만 집중 내신 모드로 전환하는 전략이 청주 상위권 학생들이 주로 사용하는 방식입니다.', 'tip': None},
        ],
    },
    '충주시': {
        'subs': ['칠금동', '칠금', '봉방동', '호암동'],
        'feature': '충청북도 충주시는 칠금동과 봉방동을 중심으로 충북 제2 도시 학원가가 형성된 지역입니다. 충주기업도시 개발로 수도권 이전 기업 직원 가정이 유입되면서 학원 수준에 대한 수요가 높아지고 있습니다. 칠금동 상업지구와 호암동 주거지를 중심으로 내신 기출 자료가 축적된 검증된 학원들이 안정적으로 운영되고 있으며, 충북 동부 지역 학생들의 교육 거점 역할을 하고 있습니다.',
        'faq': [
            ('충주시 칠금동 학원가는 어떤 특징이 있나요?', '칠금동은 충주 핵심 상업·주거지로 내신 전문 학원들이 안정적으로 운영됩니다. 충주고·충주여고 내신 기출 자료를 보유한 학원들이 시험 직전 집중 특강에서 강점을 보이며, 학부모 커뮤니티를 통한 정보 공유가 활발합니다.'),
            ('충주기업도시 이전 가정은 어떤 학원을 이용하나요?', '기업도시 이전 가정은 수도권 수준의 학원 품질을 요구하며, 충주 칠금동·호암동 학원들을 주로 이용합니다. 부족한 심화 과목은 EBS 인강과 병행하는 하이브리드 방식이 일반적이며, 방학 중 청주 단기 특강을 이용하는 경우도 있습니다.'),
            ('충주에서 고등 수능 준비는 어떻게 하나요?', '칠금동과 연수동에 수능 종합 학원들이 운영됩니다. 충주 학원에서 내신과 기초 수능 개념을 다루고, 심화 수능은 EBS 인강과 병행하는 방식이 현실적입니다. 모의고사 직후 오답 분석을 즉시 진행하는 학원을 선택하면 성적 향상이 빠릅니다.'),
        ],
        'extra': [
            {'h2': '칠금·봉방 학원가 분석', 'content': '칠금동 상업지구와 봉방동·호암동 주거지를 중심으로 충주 최대 학원가가 형성되어 있습니다. 개원 7년 이상 검증된 학원들이 충주고·충주여고 내신 기출 자료를 보유하고 있으며, 기출 분석 정확도가 높아 내신 직전 효율이 검증되어 있습니다. 충주기업도시 개발 이후 신규 학원들도 경쟁에 합류하며 전반적인 수업 수준이 향상되고 있습니다.', 'tip': None},
            {'h2': '기업도시 교육 환경', 'content': '충주기업도시에는 수도권 대기업 및 제조업체 직원 가정이 유입되어 있습니다. 이들 가정은 수도권 교육 수준을 충주에서 유지하려는 수요가 강하며, 온라인 강의 병행과 방학 타 지역 단기 특강 참여가 활발합니다. 충주 학원은 내신 관리와 기초 수능 개념 완성에 집중하고, 심화 내용은 EBS 인강으로 보완하는 방식이 가장 효과적인 전략입니다.', 'tip': '기업도시 이전 가정은 충주 학원과 온라인 강의를 병행하는 전략을 많이 사용합니다.'},
            {'h2': '중등 내신 완성 전략', 'content': '충주 중등 학원들은 지역 중학교 내신 기출을 분석해 시험 2~3주 전 집중 특강을 운영합니다. 같은 학교 재원생이 15명 이상인 학원은 기출 분석 정확도가 높아 내신 직전 효율이 크게 올라갑니다. 수학은 단원별 기출 유형 반복, 영어는 교과서 본문 암기와 서술형 대비, 국어는 출제 교사별 경향 파악이 충주 중등 내신의 핵심 전략입니다.', 'tip': None},
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
for si, data in chungbuk.items():
    path = os.path.join(base, DO, si, 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(make_html(si, data))
    count += 1
    print(f'생성: {DO}/{si}')

print(f'\n완료: {count}개 페이지')
