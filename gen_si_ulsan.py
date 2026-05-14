import os
import urllib.parse

base = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
DO = '울산광역시'
DO_SHORT = '울산'
CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
CLOUDINARY_IMG = '/v1778460866/1_fyhcx0.webp'

def cloudinary_url(text):
    encoded = urllib.parse.quote(text, safe='')
    return f'{CLOUDINARY_BASE}/l_text:NanumGothic_45_bold:{encoded},co_white,g_south_west,x_30,y_30,b_rgb:00000066{CLOUDINARY_IMG}'

ulsan = {
    '남구': {
        'subs': ['울산삼산', '울산달동', '달동'],
        'feature': '울산 남구는 삼산동과 달동을 중심으로 울산 최대 학원가가 형성된 지역입니다. 삼산로 상업지구와 대단지 아파트가 밀집한 특성상 수능·내신 전문 학원들이 경쟁하며 수준을 높이고 있습니다. 현대자동차·SK에너지 임원급 및 전문직 가정 비율이 높아 학원 수준에 대한 눈높이가 울산 내 최상위이며, 무거동과 옥동 신도시에도 소수정예 관리형 학원들이 탄탄하게 운영되고 있습니다.',
        'faq': [
            ('남구 삼산동 학원가의 특징은 무엇인가요?', '삼산동은 울산 최대 상업지구와 맞닿아 있어 학원 수가 가장 많고 경쟁이 치열합니다. 내신 기출 자료가 방대하게 축적되어 있으며, 고소득 전문직 가정 수요를 바탕으로 심화 커리큘럼 수준이 울산 내 최상위를 유지합니다.'),
            ('달동 학원가는 어떤 특징이 있나요?', '달동은 대단지 아파트 단지가 밀집해 초등·중등 학원 수요가 안정적입니다. 같은 학교 재원생 비율이 높은 내신 전문 학원들이 시험 직전 집중 특강에서 강점을 보이며, 학부모 카페를 통한 학원 정보 공유가 매우 활발합니다.'),
            ('남구에서 수능 심화 준비는 어떻게 하나요?', '삼산동과 무거동에 수능 종합 학원들이 집중되어 있습니다. 고1부터 내신과 수능을 병행 준비하는 구조가 잘 갖춰져 있으며, 심화 이과 수능은 울산대학교 인근 무거동 학원들이 강점을 보입니다.'),
        ],
        'extra': [
            {'h2': '삼산·달동 학원가 분석', 'content': '삼산로 상업지구와 달동 아파트 단지 사이에 울산 최대 규모 학원가가 형성되어 있습니다. 수능 전 과목 단과 조합이 자유롭고 개원 10년 이상 검증된 학원들이 다수 운영 중입니다. 특히 울산 지역 상위권 고교인 학성고·무거고 내신 기출 자료가 축적된 학원들의 내신 대비 효율이 높으며, 강사 전담 과목 여부를 미리 확인하면 선택에 유리합니다.', 'tip': None},
            {'h2': '울산 최대 학원가 활용법', 'content': '삼산·달동은 학원 수가 많아 선택지가 넓지만 그만큼 옥석 가리기가 중요합니다. 개원 2년 이상에 재원생 후기가 꾸준한 학원을 우선 선택하고, 체험 수업 후 결정하는 방식이 실패를 줄입니다. 수능 단과 학원은 같은 학교 학생 비율이 높은 곳보다 수능 성적 향상 실적을 공개하는 학원이 더 신뢰할 수 있는 지표입니다. 두세 곳에 분산 등록보다 한두 곳을 깊게 이용하는 것이 효과적입니다.', 'tip': '학원 등록 전 강사 1:1 상담을 꼭 요청하세요. 전담 강사 여부를 직접 확인할 수 있습니다.'},
            {'h2': '수능·내신 병행 전략', 'content': '울산 남구 학원들은 고1·2 내신과 수능 병행 관리를 핵심 강점으로 내세웁니다. 고1은 학교 내신 70%, 수능 기초 30% 비율로 균형을 잡고, 고2 2학기부터 수능 비중을 50%로 높이는 것이 일반적입니다. 고3 초반에는 수능 전 과목 체계를 완성하고 내신 시험 기간만 일시적으로 내신 집중 모드로 전환하는 전략이 남구 상위권 학생들이 주로 쓰는 방식입니다.', 'tip': None},
            {'h2': '초등 기초 완성 가이드', 'content': '남구 초등 학원들은 수학 연산 기초와 영어 파닉스 완성을 핵심으로 운영합니다. 초등 1~3학년은 주 2회 수업으로 학습 습관 형성에 집중하고, 4학년부터 주 3회로 늘려 서술형 수학과 영어 독해를 추가하는 단계적 설계가 효과적입니다. 달동·삼산동 소규모 학원들은 학생 수가 적어 오답 분석이 개별적으로 이루어지며, 학부모 주간 상담을 운영하는 학원들이 신뢰를 얻고 있습니다.', 'tip': None},
        ],
    },
    '북구': {
        'subs': ['송정', '송정동', '화봉동'],
        'feature': '울산 북구는 현대자동차 공장 인근 신도시 개발로 매곡동과 진장동을 중심으로 학원가가 빠르게 성장하고 있습니다. 현대자동차 직원 가정 비율이 높아 안정적인 교육 수요가 형성되어 있으며, 신도시 특성상 소수정예 관리형 학원에 대한 선호도가 강합니다. 진장지구 개발로 아파트 단지 내 새로운 학원들이 속속 개원하고 있으며, 내신 기출 축적과 함께 수준이 빠르게 향상되고 있습니다.',
        'faq': [
            ('북구 매곡동 학원가 수준은 어떤가요?', '매곡동은 북구 핵심 주거지로 초등·중등 학원들이 안정적으로 운영됩니다. 현대자동차 직원 가정이 많아 교육 관심도가 높으며, 학부모 간 정보 공유가 활발해 신뢰받는 학원들이 자연스럽게 검증됩니다.'),
            ('북구 진장지구 신규 학원은 믿을 수 있나요?', '진장지구는 2010년대 이후 개발 신도시로 신규 학원이 많습니다. 개원 1년 이상에 지역 맘카페 후기가 꾸준한 학원, 체험 수업을 운영하는 학원을 우선 선택하세요. 신규 학원이라도 강사 경력이 10년 이상이면 수업 수준은 검증된 경우가 많습니다.'),
            ('북구에서 울산 남구 학원 통학이 가능한가요?', '매곡동에서 삼산동까지 버스로 약 25~35분 거리입니다. 내신은 북구 지역 학원을 이용하고, 수능 심화나 특목고 준비는 남구 삼산동 학원을 병행하는 방식이 현실적입니다. 대중교통 이동 시간이 길기 때문에 고2 이전부터 통학 체력을 고려해 결정하세요.'),
        ],
        'extra': [
            {'h2': '매곡·진장 학원가 분석', 'content': '매곡동 주거지와 진장지구 아파트 단지를 중심으로 북구 최대 학원 밀집 지역이 형성되어 있습니다. 매곡동은 개원 5년 이상 학원들이 내신 기출을 축적하며 신뢰를 쌓고 있고, 진장지구는 신도시 특성상 최신 커리큘럼을 앞세운 학원들이 경쟁 중입니다. 두 지역 모두 현대자동차 직원 가정의 안정적인 수요가 학원 운영을 뒷받침하고 있습니다.', 'tip': None},
            {'h2': '현대자동차 가정 교육 특성', 'content': '현대자동차 직원 가정은 직업 안정성이 높아 사교육 투자에 적극적인 편입니다. 수도권 이전이나 특목고 진학보다 지역 대학 이공계 우수 학과 진학을 목표로 하는 가정이 많으며, 이에 따라 수능 수학·과학 심화 학원 수요가 강합니다. 울산과기원(UNIST) 진학을 목표로 하는 학생들을 위한 수학·과학 심화 특강을 운영하는 학원들이 북구에서도 증가하고 있습니다.', 'tip': 'UNIST 진학 목표 학생은 중3부터 수학 심화 + 과학탐구 병행 학원을 찾으세요.'},
            {'h2': '신도시 학원 선택법', 'content': '진장지구처럼 신도시는 학원 정보가 부족할 수 있습니다. 선택 기준은 강사 경력 5년 이상 전담 여부, 체험 수업 운영 여부, 지역 맘카페 3개월 이상 후기 축적 여부입니다. 같은 중학교 재원생 비율이 높은 내신 학원은 기출 축적이 빠르며, 신규 학원이라도 재원생 수가 꾸준히 증가하는 곳은 긍정적인 신호입니다.', 'tip': None},
            {'h2': '중등 내신 집중 전략', 'content': '북구 중등 학원들은 지역 중학교 내신 기출을 분석해 시험 3주 전부터 집중 특강을 운영합니다. 수학은 기출 유형별 오답 반복, 영어는 교과서 본문 암기와 서술형 연습, 국어는 담당 교사 출제 경향 분석이 핵심입니다. 같은 학교 재원생 20명 이상인 학원은 내신 기출 분석 정확도가 높아 시험 직전 효율이 크게 올라갑니다.', 'tip': None},
        ],
    },
    '중구': {
        'subs': ['복산', '반구동'],
        'feature': '울산 중구는 울산 원도심으로 성남동과 복산동을 중심으로 울산 전통 학원가가 오랫동안 형성되어 온 지역입니다. 울산 역사 중심가 특성상 오래된 검증된 학원들이 많으며, 지역 중고교 내신 기출 자료가 방대하게 축적되어 있습니다. 최근 원도심 정비 사업과 함께 젊은 가족 유입이 늘면서 소수정예 관리형 학원 수요도 함께 증가하고 있습니다.',
        'faq': [
            ('중구 성남동 학원가는 어떤 특징이 있나요?', '성남동은 울산 원도심 핵심 학원가로 20년 이상 운영된 학원들이 많습니다. 울산 지역 중고교 내신 기출 자료가 가장 방대하게 축적되어 있으며, 수능·내신 병행 전문 학원들이 중구 학생들의 오랜 신뢰를 받고 있습니다.'),
            ('중구에서 단과 학원 조합이 가능한가요?', '성남동과 복산동 인근에 수능 단과 학원들이 분포해 있어 과목별 조합이 가능합니다. 국어·수학·영어 각각 전문 단과 학원을 조합하면 월 학원비를 종합 학원보다 절감하면서 수준 높은 수업을 들을 수 있습니다.'),
            ('중구에서 고등 이과 입시 준비는 어떻게 하나요?', '복산동과 태화동에 수능 이과 전문 학원들이 있습니다. 수학 미적분·기하와 과학탐구 물화생지 전담 강사를 보유한 학원을 선택하고, 고2 2학기부터 수능 이과 체계를 완성하는 일정을 학원과 함께 설계하는 것이 효과적입니다.'),
        ],
        'extra': [
            {'h2': '성남·복산 학원가 분석', 'content': '성남동 원도심 상업지구와 복산동 주거지에 울산 중구 최대 학원 밀집 지역이 형성되어 있습니다. 개원 15년 이상의 검증된 학원들이 다수 운영 중이며, 특히 울산 내 주요 고교인 울산고·학성고 등의 내신 기출 자료를 방대하게 보유한 학원들이 내신 대비에서 강점을 보입니다.', 'tip': None},
            {'h2': '울산 도심 학원 활용법', 'content': '중구는 울산 시내버스 노선이 집중되어 남구·북구·동구에서 접근이 편리합니다. 거주 지역 학원에서 내신을 관리하고, 수능 심화 단과 수업은 성남동 전문 학원을 이용하는 분리 전략이 효율적입니다. 특히 수능 국어·영어 전문 단과 학원이 성남동에 집중되어 있어 이 과목을 강화하고자 하는 학생들에게 유리합니다.', 'tip': '단과 학원은 등록 전 강사 경력과 수능 성적 향상 사례를 반드시 확인하세요.'},
            {'h2': '단과 학원 조합 전략', 'content': '울산 중구 단과 학원들은 과목별 전문성이 높습니다. 수학은 개념+기출 분석 전문 학원, 영어는 독해 속도와 문법 오류 교정 전문 학원, 국어는 비문학 독해와 화작문 전문 학원으로 조합하면 각 과목의 약점을 집중 보완할 수 있습니다. 월 총 학원비 예산을 정하고 우선순위 과목부터 등록하는 방식이 현실적입니다.', 'tip': None},
            {'h2': '고등 이과 입시 전략', 'content': '울산 중구 고등 이과 학원들은 수학 미적분·기하와 과학탐구를 연계해 수능 이과 체계를 완성하는 데 강점이 있습니다. 울산과기원(UNIST)·부산대 이공계를 목표로 하는 학생이라면 고2 초반부터 수능 이과 커리큘럼을 시작하고, 고3 여름방학에 취약 과목 집중 보강을 넣는 일정이 효과적입니다. 물리·화학 전담 강사를 보유한 학원이 이과 수능 준비에서 가장 신뢰할 수 있는 선택입니다.', 'tip': None},
        ],
    },
}


def make_region_list(gu, subs):
    links = '\n          '.join(
        f'<li><a href="/{DO}/{gu}/{s}/">{s}</a></li>' for s in subs
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


def make_html(gu, data):
    subs = data['subs']
    feature = data['feature']
    faqs = data['faq']
    extra = data['extra']

    cld = cloudinary_url(f'{DO_SHORT} {gu} 학원 실제내부')
    desc = f'{gu} 영어학원·수학학원 정보를 동별로 안내합니다. {", ".join(subs[:3])} 등 {gu} 전 지역 학원을 한눈에 찾아보세요. 내신 전문 학원부터 수능 대비 학원까지 지역별로 확인하실 수 있습니다.'
    keywords = f'{gu} 수학학원, {gu} 영어학원, {DO_SHORT} {gu} 학원, {gu} 학원 추천, {gu} 내신 학원, {gu} 학원 정보'

    region_list_html = make_region_list(gu, subs)
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

  <title>{gu} 수학학원 영어학원 모음집 | 동네학원 모여라</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="동네학원 모여라">
  <meta name="robots" content="index, follow">
  <meta name="naver-site-verification" content="6c8552333b0e48ee6249eeecfdd0e6c5c62384eb">

  <meta property="og:type" content="article">
  <meta property="og:title" content="{gu} 수학학원 영어학원 모음집 | 동네학원 모여라">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://energyplus.kr/{DO}/{gu}/">
  <meta property="og:site_name" content="동네학원 모여라">
  <meta property="og:locale" content="ko_KR">
  <meta property="og:image" content="{cld}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{gu} 수학학원 영어학원 모음집 | 동네학원 모여라">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{cld}">
  <meta name="theme-color" content="#F97316">
  <link rel="canonical" href="https://energyplus.kr/{DO}/{gu}/">

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
        "@id": "https://energyplus.kr/{DO}/{gu}/#article",
        "headline": "{gu} 수학학원 영어학원 모음집",
        "description": "{desc}",
        "image": "{cld}",
        "datePublished": "2026-05-12",
        "dateModified": "2026-05-12",
        "author": {{"@type": "Organization", "name": "동네학원 모여라", "url": "https://energyplus.kr/"}},
        "publisher": {{
          "@type": "Organization",
          "name": "동네학원 모여라",
          "url": "https://energyplus.kr/",
          "logo": {{"@type": "ImageObject", "url": "https://energyplus.kr/images/로고.jpg", "width": 200, "height": 200}}
        }},
        "mainEntityOfPage": {{"@type": "WebPage", "@id": "https://energyplus.kr/{DO}/{gu}/"}},
        "inLanguage": "ko-KR"
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type": "ListItem", "position": 1, "name": "홈", "item": "https://energyplus.kr/"}},
          {{"@type": "ListItem", "position": 2, "name": "{DO}", "item": "https://energyplus.kr/{DO}/"}},
          {{"@type": "ListItem", "position": 3, "name": "{gu}", "item": "https://energyplus.kr/{DO}/{gu}/"}}
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
        <img src="{cld}" alt="{gu} 학원 실제 내부" class="hero-img">
      </div>
      <div class="hero-text">
        <div class="site-headline">
          <p class="headline-badge">{DO} {gu} 학원 정보</p>
          <h1 class="headline-main">{gu}<br>수학학원 영어학원 모음집</h1>
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
          <h2 class="section-title">{gu} 영어학원 수학학원 지역별 안내</h2>
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
for gu, data in ulsan.items():
    path = os.path.join(base, DO, gu, 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(make_html(gu, data))
    count += 1
    print(f'생성: {DO}/{gu}')

print(f'\n완료: {count}개 페이지')
