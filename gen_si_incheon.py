import os
import urllib.parse

base = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
DO = '인천광역시'
DO_SHORT = '인천'
CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
CLOUDINARY_IMG = '/v1778460866/1_fyhcx0.webp'

def cloudinary_url(text):
    encoded = urllib.parse.quote(text, safe='')
    return f'{CLOUDINARY_BASE}/l_text:NanumGothic_45_bold:{encoded},co_white,g_south_west,x_30,y_30,b_rgb:00000066{CLOUDINARY_IMG}'

incheon = {
    '남동구': {
        'subs': ['구월동', '구월', '인천논현', '인천논현동'],
        'feature': '남동구는 인천 최대 인구 밀집 구로 구월동과 간석동을 중심으로 인천 최대 학원가가 형성되어 있습니다. 구월동 로데오거리 인근은 수십 년간 내신·수능 기출 데이터가 쌓인 검증된 학원들이 집중되어 있으며, 소래포구 인근 논현·서창 지역은 신도시 개발로 소수정예 학원 수요가 빠르게 늘고 있습니다. 인천지하철 1호선으로 부평·부천 학원가 연계 이용도 가능합니다.',
        'faq': [
            ('남동구 구월동 학원가가 인천 최대인 이유는?', '구월동은 인천 최대 유통상권과 함께 형성된 학원가로 수십 년간 내신 기출 데이터가 축적되어 있습니다. 인천지하철 1호선 인천시청역 인근에 대형 학원부터 소수정예 학원까지 선택지가 풍부합니다.'),
            ('남동구 중학생 내신 관리 학원은 어디가 좋나요?', '구월동과 간석동 학원들이 지역 중학교 기출 분석에 강합니다. 같은 학교 재원생 비율이 높은 학원일수록 내신 대비 효율이 높으며, 시험 2주 전 집중 특강 운영 여부를 꼭 확인하세요.'),
            ('남동구 논현·서창 신도시 학원 수준은 어떤가요?', '논현지구와 서창지구 신도시 개발로 젊은 가정이 유입되며 학원 수가 빠르게 늘고 있습니다. 소수정예 관리형 학원이 많으며, 단지 커뮤니티를 통한 정보 공유가 활발해 검증된 학원을 찾기 수월합니다.'),
        ],
        'extra': [
            {'h2': '구월·간석 학원가 분석', 'content': '구월동 인천시청역 인근은 인천에서 학원 밀집도가 가장 높은 지역입니다. 수능 종합 학원, 내신 전문 학원, 단과 학원이 고루 분포해 있으며 학원 간 경쟁이 치열해 수업 품질 대비 학비가 합리적입니다. 간석동은 인천지하철 1호선 간석오거리역 인근으로 접근성이 좋고 지역 중학교 내신 기출 분석에 강한 장기 운영 학원들이 많습니다. 두 지역 모두 20년 이상 운영된 학원이 다수 있어 학부모 신뢰도가 높습니다.', 'tip': None},
            {'h2': '내신 집중 관리 전략', 'content': '남동구 학원들은 지역 중고교 내신 시험 3주 전부터 집중 내신 모드로 전환합니다. 수학은 단원별 핵심 개념 정리와 기출 반복, 영어는 교과서 본문 암기와 서술형 대비가 핵심입니다. 국어는 학교 교사의 출제 경향을 파악한 학원이 효과적이며, 사회·과학은 시험 2주 전부터 집중 보강하면 전과목 평균을 효과적으로 끌어올릴 수 있습니다.', 'tip': '같은 학교 재원생이 많은 학원이 내신 기출 분석에 가장 강합니다.'},
            {'h2': '수능 단계별 준비법', 'content': '고1은 내신 안정화와 수능 기초 개념을 병행하고, 고2부터 수능 비중을 점진적으로 높이는 것이 남동구 학원들의 표준 전략입니다. 수학은 수능 기출 유형 분석과 오답 정리를 꾸준히 반복하고, 영어는 EBS 연계 교재 위주로 독해 속도를 끌어올립니다. 구월동 수능 종합 학원들은 모의고사 후 즉시 오답 분석 수업을 진행해 취약 영역을 빠르게 보완합니다.', 'tip': None},
        ],
    },
    '부평구': {
        'subs': ['인천삼산동', '삼산', '인천삼산', '삼산동', '부평동', '부평', '산곡동'],
        'feature': '부평구는 수도권 서부 교통 요충지로 경인선·7호선·수인분당선이 교차하는 부평역을 중심으로 인천 서부 최대 학원가가 형성되어 있습니다. 삼산동 아파트 단지와 부평동 상권을 중심으로 내신·수능 전문 학원들이 밀집해 있으며, 서울 구로·부천 학원가까지의 교통이 편리해 심화 수업 병행이 용이합니다. 인천 내에서 학원 선택 폭이 가장 넓은 구 중 하나입니다.',
        'faq': [
            ('부평구 학원가가 인천 서부 최대인 이유는?', '부평역을 중심으로 경인선·7호선·수인분당선이 교차해 접근성이 탁월합니다. 부평 상권과 삼산동 대단지 아파트 수요가 맞물려 수십 년간 학원가가 발전해 왔으며, 인천에서 학원 선택지가 가장 풍부한 지역입니다.'),
            ('부평구에서 서울 구로·부천 학원 병행이 가능한가요?', '부평역에서 경인선으로 부천까지 10분, 구로까지 20분 내외입니다. 내신은 부평 학원에서 관리하고 수능 심화는 부천·서울 학원을 병행하는 방식이 많이 활용됩니다.'),
            ('부평구 삼산동 아파트 단지 학원 특징은?', '삼산동은 대단지 아파트 밀집 지역으로 소수정예 관리형 학원이 많습니다. 아파트 단지 내 학원들은 같은 학교 재원생 비율이 높아 내신 대비 효율이 높으며, 학부모 상담이 주기적으로 이루어지는 학원이 신뢰를 얻고 있습니다.'),
        ],
        'extra': [
            {'h2': '부평역 학원가 분석', 'content': '부평역 1·5번 출구 인근에 수능·내신 종합 학원과 단과 학원들이 집중되어 있습니다. 수십 년간 형성된 학원가답게 지역 중고교 내신 기출 자료가 방대하며, 학교별 담당 강사를 운영하는 학원도 있습니다. 부평 문화의 거리 인근에는 소규모 전문 학원들이 밀집해 과목별 단과 조합이 자유롭습니다. 삼산동 방면에는 소수정예 관리형 학원들이 탄탄하게 운영되고 있습니다.', 'tip': None},
            {'h2': '교통 허브 도시 학원 활용법', 'content': '부평은 경인선·7호선·수인분당선이 교차하는 인천 최고 교통 허브입니다. 이 교통망을 활용해 내신은 부평 지역 학원에서, 수능 킬러 문항이나 특목고 입시 준비는 부천·서울 학원을 병행하는 방식이 효율적입니다. 주 1~2회 외부 학원 병행이 현실적이며, 귀가 시간과 학습 부담을 감안해 학원 시간대를 설계하는 것이 중요합니다.', 'tip': '교통이 좋다고 학원을 과도하게 병행하면 오히려 학습 효율이 떨어집니다. 과목별 목적에 맞게 선택하세요.'},
            {'h2': '초등 기초 완성 가이드', 'content': '부평구 초등 학원들은 수학 기초 개념과 영어 파닉스 완성을 핵심으로 운영합니다. 삼산동과 갈산동 아파트 단지 내 소규모 학원들은 초등 저학년 학습 습관 형성에 특화되어 있습니다. 초등 3학년까지 수학 사칙연산과 분수 기초를 완성하고, 영어는 파닉스 완성 후 리딩 과정으로 넘어가는 단계적 접근이 중요합니다. 과도한 선행보다 현행 완성에 집중하는 학원을 선택하는 것이 장기적으로 유리합니다.', 'tip': None},
        ],
    },
    '연수구': {
        'subs': ['동춘', '동춘동', '연수동', '송도', '송도동'],
        'feature': '연수구는 송도국제도시를 중심으로 글로벌 기업과 외국인 거주자가 밀집한 인천 최고 프리미엄 교육 지역입니다. 삼성바이오로직스·셀트리온 등 바이오·IT 기업 임직원 가정과 외국계 기업 종사자 가정 비율이 높아 영어 특화 학원과 이공계 심화 학원 수요가 강합니다. 연수동과 동춘동에는 지역 학교 내신에 밀착된 검증된 학원들이 운영되며, 송도에는 국제학교 연계 영어 프로그램을 운영하는 학원도 있습니다.',
        'faq': [
            ('송도 학원가의 가장 큰 특징은 무엇인가요?', '글로벌 기업 임직원과 외국인 거주자 비율이 높아 영어 회화·독해 전문 학원과 국제학교 연계 프로그램이 발달해 있습니다. 이공계 바이오·IT 가정 특성상 수학·과학 심화 학원 수요도 매우 강합니다.'),
            ('연수구 국제중·특목고 입시 학원은 어디에 있나요?', '송도동과 연수동에 국제중·외고·과학고 전문 입시 학원들이 있습니다. 영어 심화 과정과 수학 올림피아드 준비 과정을 함께 운영하는 학원이 많으며, 자기소개서와 면접 대비까지 원스톱으로 지원합니다.'),
            ('연수구 일반 내신 관리 학원도 수준이 높은가요?', '연수동과 동춘동의 내신 전문 학원들이 지역 중고교 기출 분석에 강합니다. 학부모 교육 수준이 높은 지역 특성상 학원 수업 품질에 대한 기대가 높아 전반적인 학원 수준이 인천 내에서 가장 높은 편입니다.'),
        ],
        'extra': [
            {'h2': '송도 글로벌 학원 환경 분석', 'content': '송도국제도시는 UN기구, 글로벌 기업, 외국인학교가 집중된 인천 최고 국제 도시입니다. 이 환경을 반영해 원어민 영어 학원, IB 과정 연계 학원, 영어 토론·논술 전문 학원들이 발달해 있습니다. 삼성바이오·셀트리온 임직원 자녀를 위한 이공계 심화 수학·과학 학원도 송도에서 인기입니다. 일반 내신 학원부터 국제 커리큘럼 학원까지 선택지가 인천에서 가장 다양한 지역입니다.', 'tip': None},
            {'h2': '영어 특화 교육 활용법', 'content': '송도의 외국인 밀집 환경을 최대한 활용하려면 원어민 영어 학원과 내신·수능 영어 학원을 분리해 다니는 것이 효율적입니다. 원어민 수업은 회화·듣기·토론에 집중하고, 한국인 강사 수업은 독해·문법·수능 유형에 집중합니다. 영어로 진행하는 수학·과학 수업을 제공하는 학원도 있어 이중 언어 학습 환경을 원하는 가정에 적합합니다.', 'tip': '영어 실력이 높은 학생은 수능 영어를 단독으로 집중하기보다 독서와 토론으로 종합적 실력을 키우는 방향이 장기적으로 유리합니다.'},
            {'h2': '특목고 입시 준비 전략', 'content': '연수구는 인천 내에서 외고·과학고·국제중 합격 실적이 가장 높은 구 중 하나입니다. 중1 초반부터 수학 심화와 영어 고급 과정을 시작하고, 중2 때 자기소개서 전략과 면접 대비를 추가하는 것이 일반적입니다. 송도동 학원들은 인천외고·인천과학고 기출 분석과 모의 면접 수업을 체계적으로 운영하며, 합격 실적을 공개하는 학원을 선택해 객관적으로 비교하세요.', 'tip': None},
        ],
    },
    '서구': {
        'subs': ['청라', '청라동', '가정', '가정동'],
        'feature': '인천 서구는 검단신도시와 루원시티를 중심으로 경기 북서부 신흥 교육 도시로 빠르게 성장하고 있습니다. 검단신도시는 2020년 이후 대규모 입주가 이어지며 학원 수가 폭발적으로 증가했으며, 루원시티는 인천지하철 1호선 가정역 인근으로 교통이 편리합니다. 기존 석남·가정동 학원가는 지역 학교 내신에 밀착된 검증된 학원들이 운영되고 있으며, 신도시와 구 시가지 두 축에서 학원 선택이 가능합니다.',
        'faq': [
            ('인천 서구 검단신도시 학원 수준은 어떤가요?', '2020년 이후 입주 가구가 급증하며 학원 수도 빠르게 늘었습니다. 젊은 학부모 비율이 높아 소수정예 관리형 학원에 대한 수요가 강하며, 신도시 커뮤니티를 통한 학원 정보 공유가 활발합니다.'),
            ('루원시티 인근 학원 환경은 어떤가요?', '루원시티는 가정역(인천지하철 1호선) 인근 재개발 신도시로 교통이 편리합니다. 가정동과 석남동 기존 학원들과 루원 신규 학원들이 함께 운영되며, 내신 기출이 쌓인 기존 학원들이 안정적인 선택입니다.'),
            ('인천 서구 초등 수학 학원 선택 기준은?', '검단신도시 아파트 단지 내 소규모 학원들이 초등 수학 관리에 특화되어 있습니다. 선행보다 현행 완성 위주, 숙제 확인이 철저한 학원을 우선으로 선택하세요.'),
        ],
        'extra': [
            {'h2': '검단·루원 학원 성장 분석', 'content': '검단신도시는 인천 서구 최대 신도시로 2021년 이후 대단지 아파트 입주가 이어지며 학원가가 빠르게 형성되고 있습니다. 검단사거리와 완정역 인근에 수학·영어 전문 학원들이 집중되어 있으며, 서울 강서·부천과의 접근성을 활용해 심화 수업을 외부에서 병행하는 학생도 있습니다. 루원시티는 재개발 완료 후 고소득 가정 비율이 높아지며 학원 수준도 함께 올라가고 있습니다.', 'tip': None},
            {'h2': '신도시 학원 선택 전략', 'content': '검단신도시는 신규 학원이 많아 개원 이벤트 가격에 현혹되지 않도록 주의해야 합니다. 최소 개원 1년 이상, 재원생 수와 강사 경력을 먼저 확인하고 체험 수업으로 수업 방식을 직접 확인하세요. 같은 학교 재원생 비율이 높은 학원이 내신 대비에 효율적이며, 단지 맘카페에서 6개월 이상 꾸준히 좋은 반응이 있는 학원이 안전한 선택입니다.', 'tip': '신도시 학원은 이사 직후 서두르기보다 1~2개월 관찰 후 등록하는 것이 현명합니다.'},
            {'h2': '중등 내신 완성법', 'content': '인천 서구 중등 학원들은 지역 중학교 내신 기출을 기반으로 시험 2~3주 전 집중 특강을 운영합니다. 수학은 개념 이해 후 기출 유형 반복 풀이, 영어는 교과서 본문 암기와 서술형 대비가 핵심입니다. 내신 성적이 고입에 직결되는 만큼 중1 때부터 꾸준한 내신 관리 습관을 잡아두는 것이 중3 고입 내신에서 유리한 위치를 만들어줍니다.', 'tip': None},
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
for gu, data in incheon.items():
    path = os.path.join(base, DO, gu, 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(make_html(gu, data))
    count += 1
    print(f'생성: {DO}/{gu}')

print(f'\n완료: {count}개 페이지')
