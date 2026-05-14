import os
import urllib.parse

base = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
DO = '충청남도'
DO_SHORT = '충남'
CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
CLOUDINARY_IMG = '/v1778460866/1_fyhcx0.webp'

def cloudinary_url(text):
    encoded = urllib.parse.quote(text, safe='')
    return f'{CLOUDINARY_BASE}/l_text:NanumGothic_45_bold:{encoded},co_white,g_south_west,x_30,y_30,b_rgb:00000066{CLOUDINARY_IMG}'

chungnam = {
    '천안시': {
        'subs': ['신방동', '용곡동', '신방', '쌍용동', '쌍용', '불당동', '불당', '신불당', '구불당', '두정동', '두정'],
        'feature': '충청남도 천안시는 불당동과 두정동을 중심으로 충남 최대 학원가가 형성된 지역입니다. 수도권 접경 도시 특성상 삼성·현대 계열사 임직원 가정과 수도권 이전 전문직 가정이 밀집해 있어 학원 수준에 대한 눈높이가 충남 내 최상위입니다. 천안아산역 KTX 개통 이후 수도권 교육 접근성이 높아졌으며, 불당신도시 개발로 소수정예 관리형 학원 수요가 빠르게 증가하고 있습니다.',
        'faq': [
            ('천안 불당동 학원가의 특징은 무엇인가요?', '불당동은 천안 최대 신도시로 수도권 이전 전문직·대기업 임직원 가정이 밀집해 있습니다. 소수정예 관리형 학원들이 집중되어 있으며, 최신 커리큘럼과 AI 학습 도구를 도입한 학원들이 경쟁하며 수준이 빠르게 향상되고 있습니다. 방학 전 조기 마감 학원이 많아 미리 문의하는 것이 좋습니다.'),
            ('천안에서 특목고 입시 준비가 가능한가요?', '불당동과 두정동에 충남삼성고·한국디지털미디어고 등 특목고 전문 입시 학원들이 운영됩니다. 중1부터 수학 심화와 영어 고급 과정을 시작하고 중2 때 자기소개서와 면접 대비를 추가하는 것이 일반적인 준비 일정입니다.'),
            ('천안 두정동 학원은 불당동과 어떻게 다른가요?', '두정동은 천안 전통 주거지로 내신 기출 자료가 방대하게 축적된 검증된 학원들이 많습니다. 불당동이 신도시 소수정예 학원 중심이라면 두정동은 같은 학교 재원생 비율이 높은 내신 전문 학원들이 강점입니다.'),
        ],
        'extra': [
            {'h2': '불당·두정 학원가 분석', 'content': '불당동 신도시 아파트 단지와 두정동 주거지에 천안 최대 학원가가 형성되어 있습니다. 불당동은 수도권 이전 가정 수요를 바탕으로 소수정예 관리형 학원들이 경쟁하며 수준이 빠르게 향상되고 있고, 두정동은 개원 10년 이상 검증된 내신 전문 학원들이 천안북일고·천안쌍용고 등 주요 고교 기출 자료를 방대하게 보유하고 있습니다.', 'tip': '불당동 인기 학원은 방학 2개월 전 사전 문의가 필요합니다.'},
            {'h2': '수도권 접경 지역 교육 환경', 'content': '천안은 KTX 천안아산역으로 서울 강남까지 40분대 이동이 가능해 수도권 교육과의 연계가 활발합니다. 천안 학원에서 내신 관리와 기초 수능 준비를 하고, 수능 최상위 심화 과목은 서울 대치동 단기 특강을 방학마다 이용하는 방식이 천안 상위권 학생들의 일반적인 전략입니다. 온라인 유명 강의 구독과 병행하면 서울 학원을 자주 가지 않아도 수준을 유지할 수 있습니다.', 'tip': None},
            {'h2': '특목고 입시 준비 전략', 'content': '천안에는 충남삼성고 등 전국 단위 특목고를 목표로 하는 학생 비율이 충남 내에서 가장 높습니다. 중1부터 수학 선행과 영어 심화를 시작하고, 중2에 학교생활기록부 세부 특기사항 관리와 독서 활동 설계를 추가하는 것이 효과적입니다. 자기소개서와 면접 대비는 전문 입시 컨설팅 학원을 이용하되, 불당동에 특목고 전문 학원들이 집중되어 있습니다.', 'tip': None},
        ],
    },
    '아산시': {
        'subs': ['탕정', '탕정면'],
        'feature': '충청남도 아산시는 온양동 전통 학원가와 배방읍·탕정면 신도시 학원가가 공존하는 지역입니다. 삼성디스플레이와 현대자동차 아산 공장을 중심으로 대기업 임직원 가정이 대거 유입되면서 학원 수준에 대한 수요가 빠르게 높아졌습니다. 배방읍 신도시 개발로 수도권 이전 가정이 증가하며 소수정예 관리형 학원 수요가 강해졌으며, 천안아산역 인근 교통 편의로 천안 학원 병행 이용도 활발합니다.',
        'faq': [
            ('아산시 온양동 학원가는 어떤 특징이 있나요?', '온양동은 아산 전통 중심가로 오래된 검증된 학원들이 많습니다. 아산 지역 중고교 내신 기출 자료가 방대하게 축적되어 있으며, 내신 시험 직전 집중 특강 효율이 높은 학원들이 학부모 신뢰를 얻고 있습니다.'),
            ('배방읍 신도시 학원 수준은 어떤가요?', '배방읍은 2010년대 이후 개발 신도시로 삼성·현대 임직원 가정이 밀집해 있습니다. 소수정예 관리형 학원들이 증가 중이며, 학부모 눈높이가 높아 최신 커리큘럼을 갖춘 학원들이 선호됩니다. 신규 학원은 개원 1년 이상, 체험 수업 운영 여부를 확인하고 선택하세요.'),
            ('아산에서 천안 학원 병행 이용이 가능한가요?', '배방읍에서 천안 불당동까지 차량으로 15~20분 거리입니다. 아산 학원에서 내신을 관리하고 수능 심화나 특목고 준비는 천안 불당동 학원을 병행하는 방식이 아산 상위권 학생들이 많이 선택하는 전략입니다.'),
        ],
        'extra': [
            {'h2': '온양·배방 학원가 분석', 'content': '온양동 전통 학원가와 배방읍 신도시 학원가가 아산 학원 시장을 양분하고 있습니다. 온양동은 개원 10년 이상 학원들이 아산고·온양여고 등 지역 고교 내신 기출을 방대하게 보유하고 있으며, 배방읍은 삼성·현대 임직원 가정 수요에 맞춘 소수정예 학원들이 빠르게 성장하고 있습니다. 두 지역을 비교해 자녀에게 맞는 방식을 선택하는 것이 중요합니다.', 'tip': None},
            {'h2': '산업단지 가정 교육 특성', 'content': '삼성디스플레이·현대차 아산 공장 직원 가정은 이공계 직군 특성상 수학·과학 심화 교육에 관심이 높습니다. 수능 수학과 과학탐구 전담 강사를 보유한 학원을 우선 선택하고, 코딩·AI 관련 교육 수요도 빠르게 증가하고 있습니다. 직업 안정성이 높은 대기업 가정 특성상 사교육 투자에 적극적이며, 이에 따라 배방읍 학원 수준이 빠르게 향상되고 있습니다.', 'tip': '이공계 직군 가정은 수학·과학 전담 강사 보유 여부를 첫 번째 선택 기준으로 삼으세요.'},
            {'h2': '초등 학습 습관 완성법', 'content': '아산 초등 학원들은 수학 기초 연산과 영어 파닉스 완성을 핵심으로 운영합니다. 초등 1~3학년은 주 2회 수업으로 학습 습관과 집중력 형성에 집중하고, 4학년부터 주 3회로 늘려 서술형 수학과 영어 독해를 추가하는 단계적 접근이 효과적입니다. 배방읍 소규모 학원들은 학생 수가 적어 개별 오답 분석이 가능하며, 학부모 주간 알림장을 제공하는 학원이 신뢰를 얻고 있습니다.', 'tip': None},
        ],
    },
    '당진시': {
        'subs': ['읍내동', '당진'],
        'feature': '충청남도 당진시는 현대제철과 현대건설기계 등 대형 제조업체가 밀집한 산업도시로, 당진1·2동을 중심으로 학원가가 형성되어 있습니다. 제조업 종사 가정 비율이 높아 이공계 수능 준비에 대한 관심이 강하며, 소도시 특성상 핵심 학원들의 개별 관리 수준이 높고 강사와 학생 간 밀착 지도가 잘 이루어집니다. 서해선 복선전철 개통으로 수도권 접근성이 향상되면서 교육 수요도 함께 높아지고 있습니다.',
        'faq': [
            ('당진시 학원가는 어느 지역에 집중되어 있나요?', '당진 학원가는 당진1동과 당진2동 구도심 상업지구를 중심으로 형성되어 있습니다. 당진고·당진정보고 내신 기출 자료를 보유한 학원들이 내신 대비에서 강점을 보이며, 소규모 학원 특성상 개별 관리 수준이 높습니다.'),
            ('당진에서 수능 준비는 어떻게 하나요?', '당진 학원에서 내신 관리와 기초 수능 개념을 다루고, 심화 수능은 EBS 인강과 병행하는 방식이 현실적입니다. 서해선 복선전철로 서울 접근성이 개선되어 방학 중 수도권 단기 특강 이용도 가능해졌습니다.'),
            ('당진 소도시에서 학원 선택 기준은?', '강사 경력 5년 이상 전담 여부, 같은 학교 재원생 비율, 체험 수업 운영 여부가 핵심 기준입니다. 지역 맘카페와 학부모 모임에서 꾸준히 좋은 평가를 받는 학원을 우선 고려하고, 학원을 자주 바꾸기보다 신뢰할 수 있는 한두 곳을 꾸준히 이용하는 것이 효과적입니다.'),
        ],
        'extra': [
            {'h2': '당진 학원가 현황 분석', 'content': '당진1동과 당진2동 구도심 상업지구에 당진 핵심 학원들이 집중되어 있습니다. 개원 10년 이상 학원들이 당진고·당진정보고 내신 기출 자료를 축적하고 있으며, 소규모 학원 특성상 학생 개별 오답 분석과 강사 밀착 지도가 이루어집니다. 현대제철 임직원 가정 유입 이후 수학·과학 심화 수요가 증가하면서 이공계 전담 학원들도 성장하고 있습니다.', 'tip': None},
            {'h2': '제조업 가정 교육 특성', 'content': '현대제철·현대건설기계 직원 가정은 이공계 직군 특성상 수학·과학 교육에 높은 관심을 보입니다. 수능 수학과 과학탐구 전담 강사를 보유한 학원을 우선 선택하고, 자녀가 이공계 대학 진학을 목표로 한다면 중2부터 수학 심화와 물리·화학 기초를 병행하는 것이 효과적입니다. 직업 안정성이 높은 대기업 가정 특성상 꾸준한 사교육 투자가 이루어지며, 이것이 당진 학원 수준 향상을 견인하고 있습니다.', 'tip': None},
            {'h2': '중등 내신 집중 전략', 'content': '당진 중등 학원들은 지역 중학교 내신 기출을 분석해 시험 2~3주 전 집중 특강을 운영합니다. 같은 학교 재원생 10명 이상인 학원을 선택하면 기출 분석 정확도가 높아 내신 직전 효율이 올라갑니다. 수학은 단원별 기출 유형 반복, 영어는 교과서 암기와 서술형 대비, 국어는 출제 교사 경향 파악이 당진 중등 내신의 핵심 전략이며, 방학 중 집중 선행보다 학기 중 기출 완성에 집중하는 것이 효과적입니다.', 'tip': '소도시 학원에서는 강사에게 직접 출제 경향 분석 여부를 먼저 확인하세요.'},
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
for si, data in chungnam.items():
    path = os.path.join(base, DO, si, 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(make_html(si, data))
    count += 1
    print(f'생성: {DO}/{si}')

print(f'\n완료: {count}개 페이지')
