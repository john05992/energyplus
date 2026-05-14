import os
import urllib.parse

base = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
DO = '대전광역시'
DO_SHORT = '대전'
CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
CLOUDINARY_IMG = '/v1778460866/1_fyhcx0.webp'

def cloudinary_url(text):
    encoded = urllib.parse.quote(text, safe='')
    return f'{CLOUDINARY_BASE}/l_text:NanumGothic_45_bold:{encoded},co_white,g_south_west,x_30,y_30,b_rgb:00000066{CLOUDINARY_IMG}'

daejeon = {
    '서구': {
        'subs': ['둔산동', '탄방동', '둔산', '갈마동', '관저동', '원내동', '관저', '도안동', '도안', '도안지구'],
        'feature': '대전 서구는 둔산신도시를 중심으로 대전 최대 학원가가 형성된 대전 교육 1번지입니다. 둔산동 갈마지하차도 인근과 탄방동 일대에 수능·내신 전문 학원들이 밀집해 있으며, 정부청사와 대전시청 인근 특성상 고학력 공무원·전문직 가정 비율이 높아 학원 수준과 학부모 눈높이가 대전 내 최상위입니다. 관저동과 월평동에도 소수정예 관리형 학원들이 탄탄하게 운영되고 있습니다.',
        'faq': [
            ('대전 서구 둔산동 학원가가 대전 최대인 이유는?', '둔산신도시는 대전 최대 행정·상업 중심지로 고학력 전문직 가정이 밀집해 있습니다. 수십 년간 내신 기출 데이터가 축적된 검증된 학원들이 많으며, 학원 간 경쟁이 치열해 수업 품질이 높습니다.'),
            ('서구 둔산동에서 수능 준비와 내신 관리를 동시에 할 수 있나요?', '둔산동 학원들은 내신과 수능을 병행하는 투트랙 커리큘럼을 운영합니다. 내신 기간에는 집중 내신 모드로, 평소에는 수능 유형 수업으로 전환하는 방식이 표준입니다.'),
            ('관저동·월평동 학원은 둔산동과 비교해 어떤가요?', '관저동과 월평동은 둔산동보다 학비가 합리적이면서 소수정예 학원들이 많습니다. 지역 학교 내신 밀착 관리 수준은 둔산동과 크게 차이 나지 않으며, 담임 강사 제도를 운영하는 학원들이 학부모 신뢰를 얻고 있습니다.'),
        ],
        'extra': [
            {'h2': '둔산 학원가 분석', 'content': '둔산동 갈마지하차도 사거리 인근과 탄방역 주변은 대전 최고 수준의 학원들이 밀집한 지역입니다. 수능 전 과목 단과 학원 조합이 자유롭고 강사진 수준이 높으며, 대전·충청권 최상위 합격 실적을 보유한 학원들이 집중되어 있습니다. 정부청사 인근 특성상 이공계 박사급 강사를 보유한 과학 전문 학원도 있어 이과 수험생에게 유리한 환경입니다.', 'tip': '둔산 유명 학원은 방학 전 조기 마감이 잦으니 2개월 전 문의를 권장합니다.'},
            {'h2': '대전 최대 학원가 활용법', 'content': '둔산 학원가는 과목별 단과 학원이 매우 잘 갖춰져 있어 필요한 과목만 조합하는 방식이 효율적입니다. 대전 전역에서 버스·도시철도로 접근이 가능하므로 대전 다른 구에서 둔산 학원을 병행 이용하는 학생도 많습니다. 학원 수가 많은 만큼 체험 수업 비교가 필수이며, 합격 실적과 강사 재직 기간을 꼭 확인하세요.', 'tip': None},
            {'h2': '수능·내신 병행 전략', 'content': '대전 서구 학원들은 고1·2 내신을 최우선으로 관리하면서 수능 기초를 함께 쌓습니다. 고2 2학기부터 수능 비중을 50% 이상으로 높이고, 고3 초반에 수능 전 과목 체계를 완성합니다. 내신 시험 3주 전에는 수능 수업 비중을 줄이고 집중 내신 모드로 전환하는 것이 둔산 학원들의 표준 운영 방식입니다.', 'tip': None},
        ],
    },
    '유성구': {
        'subs': ['지족동', '노은동', '노은', '지족', '반석동', '반석', '관평동', '관평'],
        'feature': '유성구는 KAIST·충남대·한국과학기술원 등 이공계 최고 대학들이 밀집한 대전 과학 도시의 핵심 지역입니다. 노은동과 지족동을 중심으로 학원가가 형성되어 있으며, 대덕연구단지와 연구개발특구 종사자 가정 비율이 높아 수학·과학 심화 학원과 이공계 입시 전문 학원 수요가 전국 최상위 수준입니다. 박사급 연구직 가정이 많아 자녀 교육에서 개념 이해 깊이와 논리적 사고력을 중시하는 경향이 강합니다.',
        'faq': [
            ('유성구 학원가가 이공계 교육에 강한 이유는?', 'KAIST·충남대·한국과학기술원 인근 특성상 이공계 박사·연구직 강사 풀이 매우 풍부합니다. 수학·과학 심화 수업 수준이 전국 최상위이며, 과학고·영재학교 입시 전문 학원도 다수 운영됩니다.'),
            ('유성구에서 과학고·영재학교 입시 준비가 가능한가요?', 'KAIST 부설 한국과학영재학교 입시를 전문으로 다루는 학원들이 노은동과 봉명동에 있습니다. 수학올림피아드·과학경시 준비 과정을 운영하며, 중1~중2 때부터 준비를 시작하는 것이 일반적입니다.'),
            ('유성구 일반 중학생 내신 관리 학원은 어디가 좋나요?', '노은동과 지족동 학원들이 지역 중학교 기출 분석에 강합니다. 시험 2주 전 집중 특강과 담임 강사 제도를 운영하는 학원을 우선으로 선택하세요.'),
        ],
        'extra': [
            {'h2': '노은·지족 학원가 분석', 'content': '노은역 인근과 지족동 아파트 단지 주변에 학원들이 집중되어 있습니다. 연구단지 종사자 가정 비율이 높아 수학·과학 심화 학원들이 특히 발달해 있으며, 단순 점수 향상보다 개념 이해 깊이를 중시하는 수업 방식이 인기입니다. KAIST 출신·재학 강사들이 운영하는 소규모 전문 학원도 있어 최상위권 학생들에게 차별화된 수업을 제공합니다.', 'tip': None},
            {'h2': 'KAIST 인근 이공계 교육 환경', 'content': '유성구는 KAIST·한국과학기술원·충남대 이공대가 집중된 국내 최고 이공계 교육 환경을 자랑합니다. 이 환경이 수학·과학 강사 풀의 질을 극적으로 높이며, 과학고·영재학교·의대 입시를 준비하는 학생들에게 전국 어디서도 받기 힘든 수준의 수업이 가능합니다. 유성구에서 이공계 진학을 목표로 하는 학생이라면 이 지역 학원 인프라를 적극 활용하는 것이 전략적으로 유리합니다.', 'tip': 'KAIST 출신 강사의 수업은 개념의 깊이가 다릅니다. 상위권 목표라면 강사 이력을 꼭 확인하세요.'},
            {'h2': '특목고 입시 준비 전략', 'content': '유성구 학원들은 과학고·영재학교·외고 입시를 위한 전문 코스를 체계적으로 운영합니다. 수학올림피아드(KMO)와 한국물리·화학올림피아드 준비 과정이 잘 갖춰져 있으며, 영재학교 입시에 필요한 창의 문제 해결 수업도 운영됩니다. 중1 초반부터 수학 심화와 과학 탐구 과정을 시작하고, 중2 때 자기소개서와 면접 대비를 추가하는 것이 합격 전략의 핵심입니다.', 'tip': None},
        ],
    },
    '중구': {
        'subs': ['태평동', '유천동', '태평'],
        'feature': '대전 중구는 대전 도심의 역사적 중심지로 대흥동과 은행동을 중심으로 학원들이 분포해 있습니다. 대전역과 충남대학교 인근 특성상 교통 접근성이 뛰어나며, 도심 특성상 단과 전문 학원과 소수정예 학원들이 강세입니다. 충남대·한밭대 인근에서 대학 출신 강사들이 운영하는 전문 학원들이 있으며, 대전 구도심 특성상 오랫동안 자리잡은 검증된 학원들이 내신 기출 자료를 방대하게 보유하고 있습니다.',
        'faq': [
            ('대전 중구 학원가의 특징은 무엇인가요?', '대흥동과 은행동 일대에 단과 전문 학원과 소수정예 학원들이 분포해 있습니다. 대전 구도심 특성상 20년 이상 운영된 검증된 학원들이 많으며, 지역 학교 내신 기출 자료가 풍부합니다.'),
            ('충남대 인근 학원은 어떤 강점이 있나요?', '충남대·한밭대 출신 강사들이 운영하는 전문 학원들이 있어 이공계 심화와 논술 수업 수준이 높습니다. 특히 충남대 의대·이공대 진학을 목표로 하는 학생에게 해당 대학 출신 강사의 입시 분석이 강점입니다.'),
            ('대전 중구 학원비는 서구보다 저렴한가요?', '서구 둔산동보다 10~20% 낮은 편입니다. 합리적인 학비로 수준 높은 수업을 받고 싶다면 중구 검증 학원들이 좋은 선택입니다.'),
        ],
        'extra': [
            {'h2': '대흥·은행 학원가 분석', 'content': '대흥동 으능정이 문화거리 인근과 은행동 중앙시장 주변에 학원들이 분포해 있습니다. 대전역과의 접근성이 좋아 대전 다른 구에서도 이용하는 학생이 있으며, 특히 국어·논술·영어 전문 학원들이 강세입니다. 중촌동과 목동에는 지역 학교 내신에 밀착된 소수정예 학원들이 개인 관리 수준이 높아 학부모 신뢰를 얻고 있습니다.', 'tip': None},
            {'h2': '도심 학원 활용법', 'content': '대전 중구는 대전 도심 교통 허브로 버스·도시철도로 대전 전역에서 접근이 편리합니다. 거주 지역 학원에서 내신을 관리하고, 수능 국어·논술 등 전문 과목은 중구 도심 학원을 이용하는 방식이 효율적입니다. 단과 학원 조합이 자유롭고 학원 수가 적당해 선택에 혼란이 적으며, 강사와의 장기 신뢰 관계를 쌓기 좋은 환경입니다.', 'tip': None},
            {'h2': '내신 집중 관리법', 'content': '대전 중구 학원들은 지역 중고교 내신 기출을 꼼꼼히 분석해 시험 2주 전 집중 특강을 운영합니다. 수학은 단원별 핵심 정리와 기출 반복, 영어는 교과서 본문 암기와 서술형 대비, 국어는 교사 출제 경향 파악이 핵심입니다. 중구는 학원 수가 많지 않아 강사와의 개인적 신뢰 관계가 형성되기 쉽고, 이를 활용한 맞춤 피드백이 내신 성적 향상에 효과적입니다.', 'tip': '담임 강사와 정기 상담을 통해 취약 단원을 구체적으로 파악하고 집중하는 것이 핵심입니다.'},
        ],
    },
    '동구': {
        'subs': ['판암동', '용운동', '대동', '삼성동', '자양동'],
        'feature': '대전 동구는 대전역과 동대전 IC를 품은 대전 동부 관문 지역입니다. 판암동과 용운동을 중심으로 지역 학교 내신에 밀착된 학원들이 운영되며, 대전 다른 구보다 학원비가 합리적인 편입니다. 충남대·한밭대와의 접근성이 좋아 대학 출신 강사들이 운영하는 소규모 전문 학원들도 있으며, 대전 서구 둔산동 학원가까지 버스나 도시철도로 이동이 가능해 심화 수업 병행이 용이합니다.',
        'faq': [
            ('대전 동구 학원가의 특징은 무엇인가요?', '판암동과 용운동에 지역 학교 내신에 밀착된 소수정예 학원들이 분포합니다. 대전 내에서 학원비가 합리적인 지역 중 하나이며, 강사와의 밀착 관리가 가능한 소규모 학원들이 강세입니다.'),
            ('동구에서 서구 둔산동 학원 병행이 가능한가요?', '대전 1호선 도시철도로 판암역에서 탄방역(둔산 인근)까지 약 20분 이내 이동이 가능합니다. 내신은 동구 지역 학원에서, 수능 심화는 둔산동 학원을 주 1~2회 병행하는 방식이 현실적입니다.'),
            ('대전 동구 초등 학원 선택 기준은?', '판암동과 삼성동 아파트 단지 내 소규모 학원들이 초등 관리에 특화되어 있습니다. 숙제 확인과 오답 관리가 철저한 학원, 학부모 상담이 정기적인 학원을 우선으로 선택하세요.'),
        ],
        'extra': [
            {'h2': '판암·용운 학원가 분석', 'content': '판암동 판암역 인근과 용운동 주거지에 내신 전문 학원들이 분포해 있습니다. 대전 동구는 학원 수가 많지 않아 지역 학부모 사이에서 검증된 학원 정보가 빠르게 공유됩니다. 오랫동안 운영된 학원들은 지역 중고교 내신 기출 자료를 충분히 보유하고 있으며, 소수정예 운영으로 학생 개별 관리 수준이 높습니다.', 'tip': None},
            {'h2': '합리적 학원 선택 전략', 'content': '대전 동구는 서구 둔산동보다 학원비가 20~30% 낮아 비용 대비 효과가 높습니다. 단과 수업 조합으로 필요한 과목만 등록하면 월 비용을 크게 줄일 수 있으며, 방학 집중 특강을 활용해 학기 중 학원 수를 줄이는 전략도 효과적입니다. 학원 선택 시 강사 재직 기간과 지역 학교 기출 보유 여부를 먼저 확인하고, 체험 수업으로 수업 방식을 직접 확인한 후 등록하세요.', 'tip': '동구 학원에서 내신을 관리하고 수능 심화는 도시철도로 둔산 학원을 병행하는 방식이 가장 비용 효율적입니다.'},
            {'h2': '초등 기초 완성 가이드', 'content': '대전 동구 초등 학원들은 수학 기초 개념 이해와 영어 파닉스 완성을 핵심으로 운영합니다. 초등 저학년은 주 2회 수업으로 학습 습관을 먼저 잡고, 고학년은 주 3회로 늘려 수학 서술형과 영어 독해를 추가하는 단계적 접근이 효과적입니다. 과도한 선행보다 현행 완성에 집중해 아이의 자신감을 먼저 키우는 것이 중등 진입 후 지속 성장의 기반이 됩니다.', 'tip': None},
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
for gu, data in daejeon.items():
    path = os.path.join(base, DO, gu, 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(make_html(gu, data))
    count += 1
    print(f'생성: {DO}/{gu}')

print(f'\n완료: {count}개 페이지')
