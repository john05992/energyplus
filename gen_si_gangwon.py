import os
import urllib.parse

base = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
DO = '강원도'
DO_SHORT = '강원'
CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
CLOUDINARY_IMG = '/v1778460866/1_fyhcx0.webp'

def cloudinary_url(text):
    encoded = urllib.parse.quote(text, safe='')
    return f'{CLOUDINARY_BASE}/l_text:NanumGothic_45_bold:{encoded},co_white,g_south_west,x_30,y_30,b_rgb:00000066{CLOUDINARY_IMG}'

gangwon = {
    '춘천시': {
        'subs': ['석사동', '석사', '후평동', '후평'],
        'feature': '강원도 춘천시는 효자동과 퇴계동을 중심으로 춘천 최대 학원가가 형성된 지역입니다. 강원대학교와 한림대학교가 위치한 교육도시 특성상 대학 출신 전문 강사들이 풍부하며, 내신 기출 자료가 꾸준히 축적되고 있습니다. 강원도청 소재지로 공무원 및 전문직 가정 비율이 높아 교육 관심도가 강원도 내 최상위이며, 강남지구 신도시 개발로 소수정예 관리형 학원 수요도 증가하고 있습니다.',
        'faq': [
            ('춘천시 효자동 학원가의 특징은 무엇인가요?', '효자동은 춘천 핵심 주거지로 초등·중등 학원들이 안정적으로 운영됩니다. 강원대·한림대 출신 강사들이 많아 수업 수준이 높으며, 춘천 지역 중고교 내신 기출 자료가 방대하게 축적된 학원들이 내신 대비에서 강점을 보입니다.'),
            ('춘천에서 수능 심화 준비가 가능한가요?', '퇴계동과 석사동에 수능 종합 학원들이 운영됩니다. 강원도 내에서 춘천이 가장 학원 수준이 높으며, 심화 수능 준비는 서울 대치동 온라인 강의와 병행하는 방식이 일반적입니다.'),
            ('춘천 강남지구 신도시 학원 현황은 어떤가요?', '강남동은 2010년대 이후 개발 신도시로 소수정예 관리형 학원들이 늘고 있습니다. 아파트 단지 커뮤니티를 통한 정보 공유가 활발하며, 체험 수업을 운영하는 학원들의 신뢰도가 높습니다.'),
        ],
        'extra': [
            {'h2': '춘천 효자·퇴계 학원가 분석', 'content': '효자동 주거지와 퇴계동 상업지구에 춘천 최대 학원가가 형성되어 있습니다. 개원 10년 이상 검증된 학원들이 다수 운영 중이며, 춘천고·춘천여고·강원대사범부속고 등 주요 고교 내신 기출 자료를 보유한 학원들이 내신 대비에서 높은 효율을 보입니다. 강원대 인근 특성상 이공계 강사 풀이 풍부합니다.', 'tip': None},
            {'h2': '강원대 인근 교육 환경', 'content': '강원대학교와 한림대학교가 위치한 춘천은 강원도 내에서 가장 우수한 강사 풀을 보유하고 있습니다. 대학원생 및 졸업생 출신 강사들이 수능 수학·과학·영어 수업을 운영하며, 교대 출신 강사들의 국어 논술 수업도 강점입니다. 강원대 의대·사범대 진학을 목표로 하는 학생들을 위한 전문 입시 상담 학원도 운영됩니다.', 'tip': '대학 인근 학원은 강사 출신 학교와 전공을 미리 확인하면 선택에 도움이 됩니다.'},
            {'h2': '지방 소도시 학원 활용법', 'content': '춘천은 수도권 대비 학원 수가 적지만 핵심 학원들의 수업 집중도가 높습니다. 수도권처럼 여러 학원을 분산 등록하기보다 한두 학원을 깊게 이용하며 강사와 신뢰 관계를 쌓는 것이 효과적입니다. 부족한 심화 과목은 EBS 인강과 병행하고, 오답 분석과 질문 해결은 담당 강사에게 집중하는 방식이 지방 소도시에서 가장 현실적인 전략입니다.', 'tip': None},
            {'h2': '중등 내신 완성 전략', 'content': '춘천 중등 학원들은 지역 중학교 내신 기출을 체계적으로 분석해 시험 2~3주 전 집중 특강을 운영합니다. 같은 학교 재원생 15명 이상인 학원은 기출 분석 정확도가 높아 내신 직전 효율이 크게 올라갑니다. 수학은 단원별 개념 완성 후 기출 유형 반복, 영어는 교과서 본문 암기와 서술형 대비, 국어는 출제 교사별 경향 파악이 핵심입니다.', 'tip': None},
        ],
    },
    '원주시': {
        'subs': ['단구동', '무실동', '단계동', '개운동', '무실', '반곡동'],
        'feature': '강원도 원주시는 무실동과 단구동을 중심으로 강원도 내 춘천과 함께 가장 발달된 학원가가 형성된 지역입니다. 혁신도시 기업도시 개발로 수도권 이전 직원 가정과 전문직 가정 유입이 증가하면서 학원 수준에 대한 눈높이가 빠르게 올라갔습니다. 연세대학교 원주캠퍼스와 가톨릭관동대 등 대학교 인근 강사 풀을 바탕으로 수능 심화 학원들이 꾸준히 성장하고 있습니다.',
        'faq': [
            ('원주 무실동 학원가 수준은 어떤가요?', '무실동은 원주 최대 신도시로 소수정예 관리형 학원들이 집중되어 있습니다. 기업도시 이전 가정 특성상 교육 관심도가 높으며, 최신 커리큘럼을 갖춘 학원들이 경쟁하며 수준이 빠르게 향상되고 있습니다.'),
            ('원주 기업도시 가정의 교육 특성은 어떤가요?', '기업도시·혁신도시 이전 가정은 수도권 교육 수준을 원주에서도 유지하려는 수요가 강합니다. 온라인 강의 병행과 방학 수도권 특강 참여가 활발하며, 원주 학원에서는 내신 관리와 기초 수능 준비를 맡기는 방식이 일반적입니다.'),
            ('원주에서 수능 준비는 어떻게 하나요?', '단구동과 무실동에 수능 종합 학원들이 운영됩니다. 수능 심화는 연세대 원주캠퍼스 강사 출신 학원이 이과 심화에서 강점을 보이며, 부족한 심화 과목은 EBS 인강과 병행하는 방식이 현실적입니다.'),
        ],
        'extra': [
            {'h2': '원주 무실·단구 학원가 분석', 'content': '무실동 대단지 아파트와 단구동 상업지구를 중심으로 원주 최대 학원가가 형성되어 있습니다. 기업도시·혁신도시 개발 이후 수도권 이전 가정의 유입으로 학원 수준에 대한 눈높이가 높아졌으며, 최신 커리큘럼과 AI 학습 도구를 도입한 학원들이 경쟁하고 있습니다. 원주 지역 주요 고교 내신 기출 자료를 보유한 학원들이 내신 대비에서 높은 신뢰를 받고 있습니다.', 'tip': None},
            {'h2': '기업도시 교육 환경', 'content': '원주 기업도시와 혁신도시에는 수도권 대기업·공공기관 이전 직원 가정이 밀집해 있습니다. 이들 가정은 수도권 수준의 학원 품질을 요구하며, 이러한 수요가 원주 학원 수준 향상을 견인하고 있습니다. 온라인 수업 병행이나 방학 서울 단기 특강 활용이 활발하며, 원주 학원은 평상시 내신 관리와 기초 수능 준비에 집중하는 방식이 가장 효과적입니다.', 'tip': '기업도시 이전 가정은 원주 학원과 서울 온라인 강의를 병행하는 하이브리드 전략을 많이 씁니다.'},
            {'h2': '수능 준비 현실적 전략', 'content': '원주에서 수능 준비는 학원 수업과 EBS 인강 병행이 현실적입니다. 원주 학원에서 개념 이해와 기출 분석을 다루고, EBS 연계 교재와 인강으로 심화 보완하는 방식이 효과적입니다. 모의고사 직후 오답 분석 수업을 즉시 진행하는 학원을 선택하면 성적 향상 속도가 빠르며, 방학 중 서울 단기 특강 1~2회 참여로 수능 최신 트렌드를 보완하는 것도 좋은 전략입니다.', 'tip': None},
            {'h2': '초등 학습 습관 완성법', 'content': '원주 초등 학원들은 수학 기초 연산과 영어 파닉스 완성을 핵심으로 운영합니다. 초등 1~3학년은 주 2회 수업으로 학습 습관과 집중력 향상에 집중하고, 4학년부터 주 3회로 늘려 서술형 수학과 영어 독해를 추가하는 단계적 접근이 효과적입니다. 무실동 소규모 학원들은 학생 수가 적어 개별 오답 분석이 가능하며, 학부모 정기 상담을 운영하는 학원이 신뢰를 얻고 있습니다.', 'tip': None},
        ],
    },
    '강릉시': {
        'subs': ['교동', '강릉교동', '포남동'],
        'feature': '강원도 강릉시는 교동과 포남동을 중심으로 강릉 최대 학원가가 형성된 지역입니다. 관동대학교와 강릉원주대학교 인근 교육 인프라를 바탕으로 강원 영동 지역 최대 교육 도시로 자리잡고 있습니다. 관광·서비스업 외에도 공무원 및 전문직 가정이 많아 교육 투자 의지가 강하며, 강릉 지역 중고교 내신 기출 자료가 축적된 학원들의 내신 대비 효율이 높습니다.',
        'faq': [
            ('강릉 교동 학원가의 특징은 무엇인가요?', '교동은 강릉 원도심으로 오래된 검증된 학원들이 많습니다. 강릉 지역 주요 중고교 내신 기출 자료가 방대하게 축적되어 있으며, 10년 이상 운영된 학원들의 내신 대비 효율이 높습니다.'),
            ('강릉에서 수능 준비는 어떻게 하나요?', '교동과 포남동에 수능 종합 학원들이 운영됩니다. 강릉원주대 출신 강사들의 이과 심화 수업이 있으며, 부족한 심화 과목은 EBS 인강과 병행하는 방식이 강릉 학생들의 일반적인 수능 준비 전략입니다.'),
            ('강릉 포남동 신도시 학원은 어떤가요?', '포남동은 강릉 신도시 주거지로 소수정예 관리형 학원들이 운영됩니다. 젊은 학부모 비율이 높아 최신 커리큘럼을 갖춘 학원들에 대한 수요가 강하며, 지역 맘카페를 통한 학원 정보 공유가 활발합니다.'),
        ],
        'extra': [
            {'h2': '강릉 교동·포남 학원가 분석', 'content': '교동 원도심 상업지구와 포남동 주거지에 강릉 최대 학원 밀집 지역이 형성되어 있습니다. 교동은 개원 10년 이상 검증된 학원들이 강릉 지역 주요 고교인 강릉고·강릉여고 내신 기출 자료를 방대하게 보유하고 있으며, 포남동은 신도시 특성에 맞춘 소수정예 학원들이 증가 중입니다.', 'tip': None},
            {'h2': '소도시 학원 최대 활용법', 'content': '강릉은 수도권 대비 학원 수가 적지만 핵심 학원들의 수업 밀도가 높습니다. 여러 학원에 분산 등록하기보다 한두 학원을 집중 이용하며 강사와 밀착 관계를 유지하는 것이 효과적입니다. 부족한 심화 콘텐츠는 EBS 인강과 유명 강사 유료 강의로 보완하고, 오답 분석과 질문 해결은 담당 강사에게 집중하는 방식이 강릉에서 검증된 전략입니다.', 'tip': 'EBS 인강과 지역 학원 병행은 강릉처럼 소도시에서 가장 효과적인 수능 준비법입니다.'},
            {'h2': '수능 장거리 대비 전략', 'content': '강릉에서 수능을 준비하는 학생들은 수도권 학생 대비 심화 학원 선택지가 제한적입니다. 이를 보완하는 방법은 방학 중 강원도교육청 무료 특강 적극 활용, 서울 유명 학원 방학 단기 특강 1회 참여, 온라인 수능 모의고사 그룹 스터디 병행입니다. 강릉 학원에서는 개념 완성과 내신 관리에 집중하고, 수능 실전 연습은 자체적으로 꾸준히 진행하는 것이 현실적입니다.', 'tip': None},
            {'h2': '고등 내신 집중 관리법', 'content': '강릉 고등 학원들은 지역 고교 내신 기출을 체계적으로 분석해 시험 2~3주 전 집중 특강을 운영합니다. 강릉고·강릉여고 재원생이 20명 이상인 학원은 기출 분석 정확도가 높아 내신 직전 효율이 크게 올라갑니다. 수학은 기출 유형별 반복, 영어는 교과서 암기와 서술형 대비, 국어는 출제 교사별 경향 파악이 핵심이며, 내신 후 수능 준비 전환 일정을 학원과 미리 합의하는 것이 중요합니다.', 'tip': None},
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
        "datePublished": "2026-05-12",
        "dateModified": "2026-05-12",
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
for si, data in gangwon.items():
    path = os.path.join(base, DO, si, 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(make_html(si, data))
    count += 1
    print(f'생성: {DO}/{si}')

print(f'\n완료: {count}개 페이지')
