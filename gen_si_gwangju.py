import os
import urllib.parse

base = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
DO = '광주광역시'
DO_SHORT = '광주'
CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
CLOUDINARY_IMG = '/v1778460866/1_fyhcx0.webp'

def cloudinary_url(text):
    encoded = urllib.parse.quote(text, safe='')
    return f'{CLOUDINARY_BASE}/l_text:NanumGothic_45_bold:{encoded},co_white,g_south_west,x_30,y_30,b_rgb:00000066{CLOUDINARY_IMG}'

gwangju = {
    '광산구': {
        'subs': ['수완지구', '수완동', '수완', '첨단동', '첨단지구', '산월동', '첨단', '선운지구', '선암동', '신창동'],
        'feature': '광산구는 수완지구와 첨단지구를 중심으로 광주 최대 신도시 학원가가 빠르게 형성되고 있습니다. 첨단산업단지 인근 특성상 IT·연구직 가정 비율이 높아 수학·과학 심화 학원 수요가 강하며, 수완지구 대단지 아파트에는 소수정예 관리형 학원들이 집중되어 있습니다. 광주 전통 학원가인 북구·서구보다 학원 역사는 짧지만 젊은 학부모 수요를 바탕으로 커리큘럼 수준이 빠르게 향상되고 있습니다.',
        'faq': [
            ('광산구 수완지구 학원가의 특징은 무엇인가요?', '수완지구는 광주 최대 신도시로 대단지 아파트 밀집 특성상 소수정예 관리형 학원들이 강세입니다. 젊은 학부모 비율이 높아 최신 커리큘럼과 AI 학습 도구를 도입한 학원들이 경쟁하며 수준이 빠르게 올라가고 있습니다.'),
            ('첨단지구 IT 가정 자녀 학원 환경은 어떤가요?', '첨단산업단지 IT·연구직 가정은 수학·과학 심화와 코딩 교육에 관심이 높습니다. 첨단동 인근에 수학 심화와 이공계 탐구 수업을 제공하는 학원들이 있으며, 소수정예로 개인별 학습 관리를 중시하는 방식이 인기입니다.'),
            ('광산구에서 광주 북구·서구 학원 병행이 가능한가요?', '수완동에서 북구 용봉동까지 버스로 약 30분 거리입니다. 내신은 광산구 지역 학원에서 관리하고, 수능 심화나 특목고 준비는 북구·서구 학원을 병행하는 방식도 활용됩니다.'),
        ],
        'extra': [
            {'h2': '수완·첨단 학원가 분석', 'content': '수완지구 수완중앙공원 인근과 첨단지구 첨단과학관 주변에 학원들이 집중되어 있습니다. 수완지구는 2000년대 중반 이후 형성된 신도시 학원가로 내신 기출 자료가 쌓이기 시작했으며, 같은 학교 재원생이 많은 학원들의 내신 대비 효율이 높아지고 있습니다. 첨단지구는 IT 기업 종사자 가정 특성에 맞춘 수학·과학 심화 학원과 코딩 교육 학원들이 발달해 있습니다.', 'tip': None},
            {'h2': '신도시 학원 선택 전략', 'content': '수완·첨단 신도시는 신규 학원이 많아 검증이 필요합니다. 개원 1년 이상 운영된 학원인지 먼저 확인하고, 단지 맘카페에서 6개월 이상 꾸준히 좋은 반응이 있는 학원을 선택하세요. 강사 경력과 담당 과목 전담 여부를 직접 물어보고, 체험 수업으로 수업 방식이 아이와 맞는지 확인한 후 등록 결정을 내리는 것이 중요합니다.', 'tip': '신도시 학원은 2~3곳 체험 비교 후 등록하는 것이 기본입니다.'},
            {'h2': '초등 기초 완성 가이드', 'content': '광산구 초등 학원들은 수학 기초 개념 이해와 영어 파닉스 완성을 핵심으로 운영합니다. 초등 저학년은 주 2회 수업으로 학습 습관을 먼저 잡고, 고학년은 주 3회로 늘려 서술형 수학과 영어 독해를 추가하는 단계적 접근이 효과적입니다. 수완지구 아파트 단지 내 소규모 학원들은 학생 수가 적어 개별 오답 분석이 가능하며, 학부모 상담이 정기적으로 이루어지는 학원이 신뢰를 얻고 있습니다.', 'tip': None},
            {'h2': '중등 내신 집중 관리법', 'content': '광산구 중등 학원들은 지역 중학교 내신 기출을 분석해 시험 2~3주 전 집중 특강을 운영합니다. 같은 학교 재원생 비율이 높은 학원을 선택하면 시험 출제 경향 파악에 유리합니다. 수학은 개념 이해 후 기출 유형 반복, 영어는 교과서 본문 암기와 서술형 대비, 국어는 교사 출제 경향 분석이 내신 성적을 빠르게 올리는 핵심 전략입니다.', 'tip': None},
        ],
    },
    '북구': {
        'subs': ['용봉동', '문흥동', '일곡동', '신용동', '운암동'],
        'feature': '광주 북구는 전남대학교와 조선대학교 인근의 교육 인프라를 바탕으로 광주 전통 학원가가 형성된 지역입니다. 용봉동과 문흥동을 중심으로 수능·내신 전문 학원들이 오랫동안 운영되어 왔으며, 전남대 출신 강사들이 운영하는 전문 학원들이 수업 수준을 끌어올리고 있습니다. 일곡지구 신도시 개발로 소수정예 관리형 학원 수요도 빠르게 증가하고 있습니다.',
        'faq': [
            ('북구 용봉동 학원가가 광주 전통 학원가인 이유는?', '전남대학교 인근 용봉동은 수십 년간 광주 북부 핵심 학원가로 자리잡아 왔습니다. 지역 중고교 내신 기출 자료가 방대하게 축적되었으며, 대학 출신 전문 강사들이 운영하는 학원들이 수업 수준을 높이고 있습니다.'),
            ('북구 일곡지구 학원은 어떤가요?', '일곡지구는 2000년대 이후 개발된 신도시로 소수정예 관리형 학원들이 많습니다. 아파트 단지 커뮤니티를 통한 학원 정보 공유가 활발하며, 젊은 학부모 수요에 맞춘 최신 커리큘럼 학원들이 경쟁하고 있습니다.'),
            ('북구에서 수능 심화 준비는 어디서 하나요?', '용봉동과 운암동에 수능 종합 학원들이 운영됩니다. 심화 수능 과정은 광주 서구 상무지구 학원가를 병행 이용하는 방법도 있으며, 도시철도 1호선으로 접근이 가능합니다.'),
        ],
        'extra': [
            {'h2': '용봉·문흥 학원가 분석', 'content': '전남대 정문 인근 용봉동과 문흥동 주거지에 광주 북부 최대 학원가가 형성되어 있습니다. 20년 이상 운영된 검증된 학원들이 많으며, 지역 중고교 내신 기출 자료가 방대하게 축적되어 있어 시험 직전 집중 특강 효율이 높습니다. 전남대·조선대 출신 강사들이 운영하는 전문 학원들이 분포하며, 특히 수능 국어와 영어 분야에서 강점을 보이는 학원들이 있습니다.', 'tip': None},
            {'h2': '전남대 인근 교육 환경', 'content': '전남대학교 인근은 대학원생과 교수 출신 강사들이 풍부해 수업 수준이 높습니다. 특히 수능 수학과 과학탐구 분야에서 이공계 대학원생 강사들의 전문성이 두드러지며, 논술·구술 전형을 준비하는 학생들을 위한 전문 강사도 다수 있습니다. 전남대 의대·사범대 진학을 목표로 하는 학생이라면 해당 학교 출신 강사가 운영하는 학원이 입시 전형 분석에서 유리합니다.', 'tip': '대학 인근 학원은 강사 이력이 곧 수업 수준이므로 반드시 사전에 확인하세요.'},
            {'h2': '내신·수능 균형 전략', 'content': '북구 학원들은 내신 기간과 수능 준비 기간을 명확히 구분해 운영합니다. 고1·2는 내신 60%, 수능 40% 비율로 병행하고, 고3 초반부터 수능 비중을 70%로 높이는 것이 표준 전략입니다. 모의고사 직후 오답 분석 수업을 즉시 진행하는 학원을 선택하면 성적 향상 속도가 빠르며, 내신 시험 2주 전에는 수능 수업 비중을 줄이고 집중 내신 모드로 전환합니다.', 'tip': None},
            {'h2': '합리적 학원비 활용법', 'content': '광주 북구는 서울·수도권 대비 학원비가 40~50% 낮아 비용 대비 효과가 높습니다. 단과 수업 조합으로 필요한 과목만 등록하면 월 비용을 크게 줄일 수 있으며, 방학 집중 특강을 활용해 학기 중 학원 수를 줄이는 전략도 효과적입니다. 학원비가 저렴하다고 무조건 많이 다니는 것보다, 한두 곳을 꾸준히 다니며 완성도를 높이는 것이 장기적으로 더 효과적입니다.', 'tip': None},
        ],
    },
    '서구': {
        'subs': ['치평동', '상무지구'],
        'feature': '광주 서구는 상무지구 신도시를 중심으로 광주 최고 수준의 학원가가 형성되어 있습니다. 상무대로 인근은 광주에서 학원 밀집도가 가장 높은 지역으로, 수능·내신·특목고 전문 학원들이 집중되어 있습니다. 광주광역시청과 금융 기관들이 밀집한 특성상 고소득 전문직 가정 비율이 높아 학원 수준에 대한 눈높이가 광주 내 최상위이며, 풍암지구와 서창지구에도 소수정예 관리형 학원들이 탄탄하게 운영되고 있습니다.',
        'faq': [
            ('상무지구 학원가가 광주 최고 수준인 이유는?', '상무지구는 광주광역시청과 금융가를 중심으로 고소득 전문직 가정이 밀집한 지역입니다. 학부모 교육 수준이 높고 학원에 대한 눈높이가 높아 학원들의 커리큘럼 수준이 광주 내 최상위를 유지합니다.'),
            ('광주 서구에서 특목고 입시 준비가 가능한가요?', '상무동 인근에 광주과학고·전남외고 전문 입시 학원들이 운영됩니다. 중1부터 수학 심화와 영어 고급 과정을 시작하고 중2 때 자기소개서와 면접 대비를 추가하는 것이 일반적인 전략입니다.'),
            ('서구 풍암지구 학원은 어떤 특징이 있나요?', '풍암지구는 상무지구보다 학비가 합리적이면서 소수정예 관리형 학원들이 많습니다. 지역 학교와 밀착된 내신 전문 학원들이 학부모 신뢰를 얻고 있으며, 아파트 단지 커뮤니티 정보 공유가 활발합니다.'),
        ],
        'extra': [
            {'h2': '상무·화정 학원가 분석', 'content': '상무대로 인근 상무지구와 화정동 아파트 단지 주변에 광주 최고 수준의 학원들이 밀집해 있습니다. 수능 전 과목 단과 학원 조합이 자유롭고 강사진 수준이 높으며, 광주·전남권 최상위 합격 실적을 보유한 학원들이 집중되어 있습니다. 상무지구는 광주 도심과 도시철도로 연결되어 광주 다른 구에서도 이용하는 학생이 많습니다.', 'tip': '상무지구 유명 학원은 방학 전 조기 마감이 잦으니 2개월 전에 문의하세요.'},
            {'h2': '광주 도심 학원 활용법', 'content': '상무지구는 광주 도시철도 1호선과 버스망으로 광주 전역에서 접근이 편리합니다. 광산구·북구·동구 학생들도 상무지구 수능 전문 학원을 이용하기 위해 통학하는 경우가 있으며, 특히 수능 심화나 특목고 입시 준비는 상무지구 학원이 광주 내 최고 선택지입니다. 거주 지역 학원에서 내신을 관리하고 수능 심화 단과만 상무지구에서 이용하는 분리 전략이 효율적입니다.', 'tip': None},
            {'h2': '수능 단계별 준비법', 'content': '광주 서구 학원들은 수능 준비를 고1 내신 안정화부터 체계적으로 설계합니다. 고1은 내신 우선, 고2 2학기부터 수능 비중 50%로 높이고, 고3 초반에 수능 전 과목 체계를 완성하는 것이 표준입니다. 수학은 수능 기출 유형 분석과 오답 반복, 영어는 EBS 연계 독해 속도 향상, 국어는 비문학 독해 훈련을 꾸준히 유지하는 것이 핵심입니다.', 'tip': None},
            {'h2': '고등 문과 입시 전략', 'content': '광주 서구 고등 문과 학원들은 국어·영어·수학 내신과 수능을 함께 다루며 사회탐구 단과 학원도 잘 갖춰져 있습니다. 수시 학생부 종합 전형을 목표로 한다면 고1부터 세특 관리와 독서 활동을 체계적으로 설계하는 학원을 선택하세요. 논술 전형은 고2 초반부터 전남대·조선대 기출 논술 분석과 첨삭을 반복하는 것이 효과적이며, 상무지구에 논술 전문 학원들이 운영됩니다.', 'tip': None},
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
for gu, data in gwangju.items():
    path = os.path.join(base, DO, gu, 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(make_html(gu, data))
    count += 1
    print(f'생성: {DO}/{gu}')

print(f'\n완료: {count}개 페이지')
