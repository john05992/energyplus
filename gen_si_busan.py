import os
import urllib.parse

base = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
DO = '부산광역시'
DO_SHORT = '부산'
CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
CLOUDINARY_IMG = '/v1778460866/1_fyhcx0.webp'

def cloudinary_url(text):
    encoded = urllib.parse.quote(text, safe='')
    return f'{CLOUDINARY_BASE}/l_text:NanumGothic_45_bold:{encoded},co_white,g_south_west,x_30,y_30,b_rgb:00000066{CLOUDINARY_IMG}'

busan = {
    '해운대구': {
        'subs': ['좌동', '반여동', '반여'],
        'feature': '해운대구는 부산 최고 부촌이자 교육 특구로 반여·재송동을 중심으로 부산 최대 학원가가 형성되어 있습니다. 좌동과 우동 센텀시티 인근에는 수능 종합 학원과 특목고 전문 학원들이 밀집해 있으며, 고소득 전문직 가정 비율이 높아 소수정예 프리미엄 학원 수요가 강합니다. 부산 전역에서 해운대 학원을 이용하기 위해 통학하는 학생이 있을 만큼 부산 내 학원 수준 최상위 지역입니다.',
        'faq': [
            ('해운대구 반여·재송동 학원가가 부산 최대인 이유는?', '반여동과 재송동은 해운대구 최대 아파트 밀집 지역으로 학부모 교육열이 매우 높습니다. 수십 년간 형성된 학원가로 지역 중고교 내신 기출 데이터가 방대하게 축적되어 있으며, 학원 간 경쟁이 치열해 수업 품질이 높습니다.'),
            ('해운대구에서 의대·최상위권 대학 입시 준비가 가능한가요?', '좌동과 센텀시티 인근에 의대 전문 학원과 최상위권 입시 학원들이 운영됩니다. 수능 수학·과학 심화 과정이 체계적이며, SKY·의약계열 합격 실적을 공개하는 학원을 선택해 객관적으로 비교하세요.'),
            ('해운대구 초등학생 학원 과열 경쟁이 심한가요?', '해운대는 부산 내에서 초등 선행 경쟁이 가장 심한 지역 중 하나입니다. 선행보다 현행 완성에 집중하는 학원을 의식적으로 선택하는 것이 장기적으로 유리하며, 아이의 학습 스트레스를 주기적으로 확인하는 것이 중요합니다.'),
        ],
        'extra': [
            {'h2': '해운대·반여 학원가 분석', 'content': '반여동 시장 인근과 재송동 아파트 단지 주변은 부산에서 가장 많은 학원이 집중된 지역입니다. 수능 전 과목 단과 학원 조합이 자유롭고, 강사진 수준과 합격 실적이 부산 내 최상위권입니다. 좌동 마린시티와 우동 센텀시티 인근에는 프리미엄 소수정예 학원들이 자리잡고 있으며, 강남 학원가 출신 강사가 운영하는 학원도 있습니다.', 'tip': '해운대 유명 학원은 방학 전 조기 마감이 잦으니 2~3개월 전 문의를 권장합니다.'},
            {'h2': '부산 최상위권 입시 전략', 'content': '해운대구 학원들은 SKY·의약계열 진학을 목표로 하는 학생을 위한 전문 코스를 운영합니다. 고1 초반부터 내신 최상위 유지와 수능 기초를 함께 쌓고, 고2 때 수능 비중을 높이는 단계적 전환이 표준 전략입니다. 수시 학생부 종합 전형을 목표로 한다면 고1부터 세특 관리와 독서·탐구 활동을 체계적으로 설계하는 학원을 선택하세요.', 'tip': None},
            {'h2': '수능 이과 준비 로드맵', 'content': '해운대구 이과 수험생은 수학과 과학탐구 단과 학원 조합이 핵심 전략입니다. 수학은 중3~고1 때 수학Ⅱ·미적분 기초를 시작하고, 고2 때 수능 전 범위 1회독을 목표로 합니다. 과학탐구는 고2 초반에 2과목을 선정해 집중하는 것이 효율적이며, 반여동과 재송동의 이과 전문 학원들이 화학·물리 심화 과정을 체계적으로 운영합니다.', 'tip': '의대를 목표로 한다면 고1 때부터 수학·과학 심화를 시작하는 것이 현실적인 타이밍입니다.'},
        ],
    },
    '부산진구': {
        'subs': ['서면동', '전포동', '부전동', '양정동', '초읍동'],
        'feature': '부산진구는 부산 최대 도심 상권인 서면을 중심으로 부산 교통 허브에 위치한 학원가를 형성하고 있습니다. 서면역과 부전역 인근에 수능·내신 전문 학원들이 집중되어 있으며, 부산 전역에서 교통이 편리해 통학 접근성이 뛰어납니다. 양정동과 초읍동은 지역 학교 내신에 밀착된 소수정예 학원들이 탄탄하게 운영되고 있으며, 전포동은 카페거리 인근으로 젊은 전문 강사들이 운영하는 학원들이 새롭게 자리잡고 있습니다.',
        'faq': [
            ('부산진구 서면 학원가의 강점은 무엇인가요?', '부산 1·2호선이 교차하는 서면역 인근으로 부산 전 지역에서 접근이 편리합니다. 수능 종합 학원과 단과 학원들이 집중되어 있으며, 학원 간 경쟁이 치열해 수업 품질이 높고 학비가 상대적으로 합리적입니다.'),
            ('부산진구 양정동 학원은 어떤 특징이 있나요?', '양정동은 서면과 가깝지만 주거 밀집 지역 특성상 지역 학교 내신에 밀착된 소수정예 학원들이 강세입니다. 학교별 담당 강사 제도를 운영하는 학원이 많아 내신 시험 전 집중 대비 효율이 높습니다.'),
            ('부산진구 중학생 영어 학원은 어디가 좋나요?', '서면 인근 영어 전문 학원들이 레벨 테스트 후 수준별 반 편성을 운영합니다. 내신 영어와 회화를 구분해 운영하는 학원을 필요에 맞게 선택하고, 전포동 영어 카페형 학원들도 회화 실력 향상에 효과적입니다.'),
        ],
        'extra': [
            {'h2': '서면·전포 학원가 분석', 'content': '서면역 인근은 부산 최대 상권답게 대형 종합 학원과 소규모 단과 학원이 수백 개 밀집해 있습니다. 부산 1호선·2호선 더블 역세권으로 접근성이 탁월해 부산진구 외 다른 구에서도 서면 학원을 이용하는 학생이 많습니다. 전포동 카페거리 인근에는 소규모 전문 학원들이 새롭게 개원하며 신선한 교육 방식을 시도하고 있어 기존 대형 학원과 좋은 대안을 이루고 있습니다.', 'tip': None},
            {'h2': '부산 도심 학원 활용법', 'content': '서면은 부산 내 교통 허브이므로 부산진구 외 학생도 이용하기 좋습니다. 내신은 거주 지역 학원에서 밀착 관리하고, 수능 심화나 특목고 입시는 서면 전문 학원을 이용하는 방식이 효율적입니다. 부산 1·2호선이 교차하므로 해운대·동래·사하 등 어느 지역에서도 서면까지 한 번에 올 수 있어 과목별 최적 학원 조합이 가능합니다.', 'tip': '서면 학원은 퇴근 시간대 혼잡을 피해 오후 6시 이전 또는 8시 이후 수업 시간대를 선택하면 편리합니다.'},
            {'h2': '내신·수능 균형 전략', 'content': '부산진구 고등 학원들은 내신 기간과 수능 준비 기간을 명확히 구분해 운영합니다. 내신 시험 3주 전에는 수능 수업 비중을 줄이고 교과서 기반 내신 집중 모드로 전환합니다. 고1·2는 내신 60%, 수능 40% 비율로, 고3은 수능 70%, 내신 30%로 단계적으로 전환하는 것이 부산진구 학원들의 표준 전략입니다. 수능 모의고사 후 즉시 오답 분석 수업을 진행하는 학원이 성적 향상 속도가 빠릅니다.', 'tip': None},
        ],
    },
    '수영구': {
        'subs': ['남천동', '민락동', '광안동', '망미동', '수영동'],
        'feature': '수영구는 남천동과 민락동을 중심으로 부산 동부 주요 학원가가 형성되어 있습니다. 광안리 해수욕장과 민락수변공원 인근 쾌적한 주거 환경에 고소득 가정이 밀집해 있으며, 소수정예 프리미엄 학원 수요가 강합니다. 해운대구와 인접해 해운대 학원가를 병행 이용하기 편리하고, 부산 2호선으로 서면·동래 학원에도 쉽게 접근할 수 있어 부산 내 학원 선택 폭이 넓은 지역입니다.',
        'faq': [
            ('수영구 남천동 학원가의 특징은 무엇인가요?', '남천동은 광안대교 조망이 가능한 고급 주거지로 소수정예 프리미엄 학원들이 강세입니다. 학생 개별 관리가 탄탄하고 학부모 상담이 정기적으로 이루어지는 학원들이 신뢰를 얻고 있습니다.'),
            ('수영구에서 해운대 학원 이용이 가능한가요?', '수영구에서 해운대 반여·재송동까지 차로 10~15분, 버스나 지하철로도 20분 내외입니다. 수영구 지역 학원에서 내신을 관리하고 수능 심화나 특목고 준비는 해운대 학원을 병행하는 방식이 많이 활용됩니다.'),
            ('수영구 고등학생 수시 준비 학원은 어디가 좋나요?', '남천동과 망미동에 수능·내신 병행 학원들이 있습니다. 학생부 종합 전형을 목표로 한다면 세특 관리와 독서 활동을 연계 지원하는 학원을 선택하고, 고1 초반부터 입시 전략을 세우는 것이 중요합니다.'),
        ],
        'extra': [
            {'h2': '남천·민락 학원가 분석', 'content': '남천동 남천삼익비치아파트 인근과 민락동 수변공원 주변에 소수정예 학원들이 분포해 있습니다. 수영구는 학원 수는 많지 않지만 학생 개별 관리 수준이 높은 프리미엄 학원들이 강세입니다. 광안동과 수영동에는 오랫동안 운영된 내신 전문 학원들이 지역 학교 기출 분석에 강점을 보이고 있습니다.', 'tip': None},
            {'h2': '해운대 연계 학원 활용법', 'content': '수영구는 해운대구와 생활권이 겹치는 지역으로 해운대 학원가 연계 이용이 가장 자연스러운 구입니다. 수영구 소수정예 학원에서 내신 밀착 관리를 받으면서, 수능 심화 단과 수업이나 특목고 입시 준비는 해운대 반여·재송동 학원을 활용하는 이원화 전략이 비용과 효율 면에서 최적입니다. 주 1~2회 해운대 병행이 현실적이며, 학원 시간대와 교통 동선을 미리 설계해두세요.', 'tip': '수영구에서 해운대 반여동까지 145번 버스 또는 지하철 2호선으로 이동 가능합니다.'},
            {'h2': '고등 문과 계열 입시 전략', 'content': '수영구 고등 문과 학원들은 국어·영어·수학 내신과 수능을 함께 다루며, 사회탐구 단과 학원도 망미동과 광안동에 운영됩니다. 수시 학생부 종합 전형을 목표로 한다면 고1부터 세특 관리와 독서 이력을 체계적으로 쌓아야 합니다. 논술 전형은 고2 초반부터 준비해야 하며, 부산 주요 대학(부산대·동아대·경성대) 기출 논술 분석 과정을 운영하는 학원을 선택하세요.', 'tip': None},
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
for gu, data in busan.items():
    path = os.path.join(base, DO, gu, 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(make_html(gu, data))
    count += 1
    print(f'생성: {DO}/{gu}')

print(f'\n완료: {count}개 페이지')
