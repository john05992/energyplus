import os
import urllib.parse

base = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
DO = '경상북도'
DO_SHORT = '경북'
CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
CLOUDINARY_IMG = '/v1778460866/1_fyhcx0.webp'

def cloudinary_url(text):
    encoded = urllib.parse.quote(text, safe='')
    return f'{CLOUDINARY_BASE}/l_text:NanumGothic_45_bold:{encoded},co_white,g_south_west,x_30,y_30,b_rgb:00000066{CLOUDINARY_IMG}'

gyeongbuk = {
    '포항시': {
        'subs': ['양덕동', '두호동', '두호', '남외', '남외동', '병영동'],
        'feature': '경상북도 포항시는 양덕동과 두호동을 중심으로 경북 최대 학원가가 형성된 지역입니다. 포항공과대학교(POSTECH) 인근 특성상 이공계 전문 강사 풀이 경북 내 최상위이며, POSCO 임직원 및 이공계 전문직 가정 비율이 높아 수학·과학 심화 학원 수요가 매우 강합니다. 양덕동은 포항 최대 주거지로 내신 기출 자료가 방대하게 축적된 검증된 학원들이 많으며, 두호동은 소수정예 관리형 학원들이 안정적으로 운영되고 있습니다.',
        'faq': [
            ('포항 양덕동 학원가의 특징은 무엇인가요?', '양덕동은 포항 최대 주거지로 포항고·포항제철고·동지고 내신 기출 자료가 방대하게 축적되어 있습니다. 개원 10년 이상 검증된 내신 전문 학원들이 시험 직전 집중 특강에서 높은 효율을 보이며, POSCO 임직원 가정의 높은 수요로 학원 커리큘럼 수준이 경북 내 최상위를 유지합니다.'),
            ('포항에서 포스텍 입시 준비가 가능한가요?', '지곡동과 양덕동에 포스텍 전문 입시 학원들이 운영됩니다. 수학 올림피아드 대비반부터 수능 이과 심화까지 경북 내에서 가장 다양한 선택지가 있으며, 중1부터 수학 심화와 과학 탐구를 병행하는 것이 효과적입니다.'),
            ('포항 두호동 학원은 양덕동과 어떻게 다른가요?', '두호동은 소수정예 관리형 학원들이 집중되어 있어 개별 지도 수준이 높습니다. 양덕동이 내신 대규모 집중 특강 강점이라면 두호동은 담당 강사 밀착 관리와 개별 오답 분석 중심으로 운영됩니다.'),
        ],
        'extra': [
            {'h2': '양덕·두호 학원가 분석', 'content': '양덕동 대단지 아파트와 두호동 주거지에 포항 최대 학원가가 형성되어 있습니다. 포항고·포항제철고 내신 기출을 방대하게 보유한 학원들이 내신 직전 집중 특강에서 높은 효율을 보이며, POSTECH·경북대 출신 이공계 강사들의 전문 학원들이 수능 이과 심화에서 강점을 보입니다. 남외동 지점들도 포항 북부 주거지 수요를 안정적으로 소화하고 있습니다.', 'tip': None},
            {'h2': '포스텍 인근 이공계 교육 환경', 'content': '포항공과대학교(POSTECH) 인근은 이공계 대학원생과 교수 출신 강사들이 풍부해 수능 이과 수업 수준이 경북 내 최상위입니다. 특히 수능 수학 미적분·기하와 물리·화학 심화 수업에서 포스텍 대학원생 강사들의 전문성이 두드러집니다. 포스텍·KAIST 진학을 목표로 하는 학생들에게 최적의 환경이며, 수학 올림피아드 대비반도 운영됩니다.', 'tip': '포스텍 진학 목표라면 중1부터 수학 올림피아드 대비와 과학탐구 심화를 병행하세요.'},
            {'h2': '이과 수능 심화 준비 전략', 'content': '포항 학원들은 이과 수능 준비를 체계적으로 설계합니다. 고1은 수학 수1·수2 기초를 완성하고, 고2 초반에 미적분·기하를 시작하며 물화생지 중 선택 과목을 결정합니다. 고2 2학기부터 수능 이과 체계를 완성하고, 고3 여름방학에 취약 과목 집중 보강을 넣는 일정이 포항 상위권 이과 학생들의 표준 전략입니다. 물리·화학 전담 강사를 보유한 학원 선택이 핵심입니다.', 'tip': None},
        ],
    },
    '구미시': {
        'subs': ['옥계동', '옥계'],
        'feature': '경상북도 구미시는 옥계동과 원평동을 중심으로 경북 제2 도시 학원가가 형성된 지역입니다. 삼성전자·LG전자·삼성SDI 구미 공장 등 전자·반도체 산업단지가 밀집해 이공계 전문직 가정 비율이 높으며, 수학·과학 심화 학원 수요가 매우 강합니다. 인동 신도시 개발로 젊은 가족 유입이 증가하며 소수정예 관리형 학원 수요도 빠르게 성장하고 있습니다.',
        'faq': [
            ('구미 옥계동 학원가는 어떤 특징이 있나요?', '옥계동은 구미 핵심 주거·상업 지역으로 내신 전문 학원들이 안정적으로 운영됩니다. 구미고·구미여고·사곡고 내신 기출 자료가 방대하게 축적되어 있으며, 전자산업 이공계 가정 수요를 바탕으로 수학·과학 심화 학원들이 강점을 보입니다.'),
            ('구미 인동 신도시 학원은 어떤가요?', '인동동은 2000년대 이후 개발 신도시로 소수정예 관리형 학원들이 빠르게 증가하고 있습니다. 삼성·LG 임직원 가정 수요로 학원 수준에 대한 눈높이가 높으며, 최신 커리큘럼과 AI 학습 도구를 도입한 학원들이 경쟁하고 있습니다.'),
            ('구미에서 대구 학원 병행 이용이 가능한가요?', '옥계동에서 대구 수성구까지 버스·전철로 약 40~50분 거리입니다. 내신은 구미 학원에서 관리하고, 수능 최상위 심화나 특목고 준비는 대구 수성구 학원을 방학 중 병행하는 방식이 구미 상위권 학생들이 선택하는 전략입니다.'),
        ],
        'extra': [
            {'h2': '옥계·원평 학원가 분석', 'content': '옥계동 상업지구와 원평동 주거지에 구미 최대 학원가가 형성되어 있습니다. 개원 10년 이상 검증된 내신 전문 학원들이 구미 지역 고교 기출을 방대하게 보유하고 있고, 삼성·LG 임직원 가정 수요에 맞춘 이공계 심화 학원들도 꾸준히 운영됩니다. 인동동 신도시 학원가와 함께 구미 전역의 학원 수준을 견인하고 있습니다.', 'tip': None},
            {'h2': '전자산업 가정 교육 특성', 'content': '삼성전자·LG전자 구미 공장 직원 가정은 전자·반도체 이공계 직군 특성상 수학·과학 심화 교육에 높은 관심을 보입니다. 수능 수학과 물리·화학 전담 강사를 보유한 학원을 우선 선택하고, 반도체·AI 관련 코딩 교육 수요도 빠르게 증가하고 있습니다. 대기업 임직원 가정 특성상 사교육 투자에 적극적이며, 이것이 구미 학원 수준 향상을 견인하는 핵심 동력입니다.', 'tip': '이공계 진학 목표 학생은 수학·물리 전담 강사 보유 여부를 첫 번째 선택 기준으로 삼으세요.'},
            {'h2': '수능 이과 집중 전략', 'content': '구미 학원들은 이과 수능 준비 커리큘럼이 잘 갖춰져 있습니다. 고1 수학 기초 완성 후 고2 초반 미적분·기하를 시작하고, 물리·화학 선택 과목을 고2 초반에 결정해 집중하는 것이 표준 일정입니다. 모의고사 직후 이과 오답 분석 수업을 즉시 진행하는 학원을 선택하고, 수능 직전 파이널 특강을 운영하는 학원을 미리 파악해 두는 것이 중요합니다.', 'tip': None},
        ],
    },
    '경산시': {
        'subs': ['경산사동', '사동'],
        'feature': '경상북도 경산시는 사동과 정평동을 중심으로 대구 인접 위성도시 특성의 학원가가 형성된 지역입니다. 영남대학교와 대구대학교 등 대학교 밀집 지역으로 대학 출신 전문 강사들이 풍부하며, 대구 수성구와 인접해 있어 대구 학원 병행 이용이 활발합니다. 경산 산업단지 개발로 수도권 이전 가정이 유입되며 교육 수요가 꾸준히 성장하고 있습니다.',
        'faq': [
            ('경산시 사동 학원가는 어떤 특징이 있나요?', '사동은 경산 핵심 주거지로 영남대 인근 특성상 대학 출신 강사들이 풍부합니다. 경산고·경산여고 내신 기출 자료를 보유한 학원들이 내신 직전 집중 특강에서 강점을 보이며, 소규모 학원 특성상 개별 밀착 지도가 잘 이루어집니다.'),
            ('경산에서 대구 학원 병행 이용이 가능한가요?', '사동에서 대구 수성구까지 버스·전철로 약 20~30분 거리입니다. 내신은 경산 학원에서 관리하고, 수능 심화나 특목고 준비는 대구 수성구·달서구 학원을 정기적으로 이용하는 방식이 현실적입니다. 대구도시철도 2호선으로 접근이 편리합니다.'),
            ('경산 정평동·옥산동 학원은 어떤가요?', '정평동과 옥산동은 경산 신규 주거지로 소수정예 관리형 학원들이 늘고 있습니다. 체험 수업을 운영하고 지역 학부모 커뮤니티에서 꾸준히 좋은 평가를 받는 학원을 우선 선택하는 것이 중요합니다.'),
        ],
        'extra': [
            {'h2': '사동·정평 학원가 분석', 'content': '사동 주거지와 정평동 아파트 단지에 경산 핵심 학원가가 형성되어 있습니다. 영남대·대구대 출신 강사들이 운영하는 전문 학원들이 수업 수준을 유지하고 있으며, 경산고·경산여고·하양고 내신 기출 자료를 보유한 학원들이 내신 대비에서 강점을 보입니다. 대구 인접 특성상 학부모들의 학원 눈높이가 높아 커리큘럼 수준도 꾸준히 향상되고 있습니다.', 'tip': None},
            {'h2': '대구 인접 지역 교육 환경', 'content': '경산시는 대구도시철도 2호선으로 대구 수성구·달서구 학원가에 20~30분 내 접근이 가능합니다. 내신은 경산 학원에서 효율적으로 관리하고, 수능 최상위 심화나 의약학·특목고 입시 전문 컨설팅은 대구 수성구 학원을 주기적으로 이용하는 분리 전략이 경산 상위권 학생들의 일반적인 방식입니다. 이동 거리가 짧아 주중 정기 통학도 가능합니다.', 'tip': '대구 학원 통학 시 도시철도 2호선 이용이 가장 효율적입니다.'},
            {'h2': '중등 내신 완성 전략', 'content': '경산 중등 학원들은 지역 중학교 내신 기출을 분석해 시험 2~3주 전 집중 특강을 운영합니다. 같은 학교 재원생이 15명 이상인 학원은 기출 분석 정확도가 높아 내신 직전 효율이 크게 올라갑니다. 수학은 단원별 기출 유형 반복, 영어는 교과서 본문 암기와 서술형 대비, 국어는 출제 교사별 경향 파악이 핵심이며, 대구 인접 도시 특성상 경산 중학교 졸업 후 대구 고교 진학을 목표로 하는 학생들을 위한 별도 커리큘럼을 운영하는 학원도 있습니다.', 'tip': None},
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
for si, data in gyeongbuk.items():
    path = os.path.join(base, DO, si, 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(make_html(si, data))
    count += 1
    print(f'생성: {DO}/{si}')

print(f'\n완료: {count}개 페이지')
