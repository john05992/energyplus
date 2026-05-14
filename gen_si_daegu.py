import os
import urllib.parse

base = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'
DO = '대구광역시'
DO_SHORT = '대구'
CLOUDINARY_BASE = 'https://res.cloudinary.com/dg9uf6vh6/image/upload'
CLOUDINARY_IMG = '/v1778460866/1_fyhcx0.webp'

def cloudinary_url(text):
    encoded = urllib.parse.quote(text, safe='')
    return f'{CLOUDINARY_BASE}/l_text:NanumGothic_45_bold:{encoded},co_white,g_south_west,x_30,y_30,b_rgb:00000066{CLOUDINARY_IMG}'

daegu = {
    '수성구': {
        'subs': ['수성동2가', '수성2가', '율하동', '율하', '시지', '노변동', '수성만촌동', '만촌동', '신천동', '효목동'],
        'feature': '수성구는 대구 최고 교육 특구로 범어동과 만촌동을 중심으로 대구 최대 학원가가 형성되어 있습니다. 전국적으로도 유명한 대구 수성구 학원가는 수능과 내신을 모두 다루는 종합 학원부터 특목고 전문 학원까지 선택지가 풍부하며, 대구 전역에서 학생들이 수성구 학원을 이용하기 위해 통학합니다. 고소득 전문직 가정 비율이 높아 학원 수준에 대한 눈높이가 대구 내 최상위이며, SKY·의약계열 합격 실적이 우수한 학원들이 집중되어 있습니다.',
        'faq': [
            ('수성구 학원가가 전국적으로 유명한 이유는?', '수성구는 수십 년간 대구 교육 1번지로 자리잡은 지역으로 수능·내신 전문 학원의 밀집도와 수준이 전국 최상위권입니다. 의대·SKY 합격 실적이 매년 높게 유지되며, 대구뿐 아니라 경북 지역에서도 수성구 학원을 이용하는 학생이 있습니다.'),
            ('수성구 학원 등록이 어렵다고 하는데 사실인가요?', '유명 학원은 정원이 빠르게 차는 경우가 많습니다. 특히 수능 전문 학원과 의대 전문 학원은 학기 시작 2~3개월 전에 문의하는 것이 현명합니다. 재원생 소개로 입학하는 경우도 많으니 지역 학부모 커뮤니티 정보를 적극 활용하세요.'),
            ('수성구 초등학생 선행 경쟁이 심한가요?', '수성구는 대구 내에서 초등 선행 경쟁이 가장 심한 지역입니다. 선행보다 현행 완성을 중심에 두는 학원을 의식적으로 선택하는 것이 중요하며, 아이의 학습 흥미와 부담 수준을 주기적으로 확인해야 합니다.'),
        ],
        'extra': [
            {'h2': '범어·만촌 학원가 분석', 'content': '범어네거리 인근과 만촌동 아파트 단지 주변은 대구 최고 수준의 학원들이 밀집한 지역입니다. 수능 전 과목 단과 학원 조합이 자유롭고 강사진 수준이 높으며, 합격 실적을 투명하게 공개하는 학원 문화가 잘 형성되어 있습니다. 황금동과 지산동에는 소수정예 내신 전문 학원들이 지역 중고교 기출 분석에 강점을 보이고 있습니다.', 'tip': '수성구 유명 학원은 방학 전 조기 마감이 잦으므로 최소 2개월 전에 문의하세요.'},
            {'h2': '대구 최상위권 입시 전략', 'content': '수성구 학원들은 SKY·의약계열 진학을 목표로 하는 학생을 위한 전문 코스를 운영합니다. 고1 초반부터 내신 최상위 유지와 수능 기초를 함께 쌓고, 고2 2학기부터 수능 비중을 70% 이상으로 높이는 것이 표준 전략입니다. 수시와 정시 비중을 고2 때 미리 설계하고 그에 맞춰 학원 조합을 최적화하는 것이 수성구 입시의 핵심입니다.', 'tip': None},
            {'h2': '수능 이과 준비 로드맵', 'content': '수성구는 의대 전문 학원이 다수 운영될 만큼 이과 수능 대비 인프라가 탁월합니다. 수학은 중3~고1 때 수학Ⅱ·미적분 기초를 시작하고, 고2 때 수능 전 범위 1회독을 완성하는 것이 목표입니다. 과학탐구는 고2 초반에 화학Ⅰ·물리Ⅰ 또는 생명과학Ⅰ 중심으로 2과목을 선정해 집중하세요. 수능 킬러 문항 집중 분석 수업을 운영하는 전문 학원을 선택하면 상위권 진입 속도가 빠릅니다.', 'tip': None},
        ],
    },
    '달서구': {
        'subs': ['이곡동', '이곡', '성서', '월성동', '상인동', '월성', '대구진천', '진천', '유천동', '대구유천동', '대구죽전동', '감삼동', '본리동'],
        'feature': '달서구는 대구 서남부 최대 인구 밀집 구로 월성동과 성당동을 중심으로 대구 제2의 학원가가 형성되어 있습니다. 성서산업단지와 인접한 특성상 다양한 직종 가정의 교육 수요를 충족하는 학원들이 고루 발달해 있으며, 수성구보다 합리적인 학비로 수준 높은 수업을 받을 수 있습니다. 감삼동과 죽전동에는 지역 학교 내신에 밀착된 소수정예 학원들이 학부모 신뢰를 얻고 있습니다.',
        'faq': [
            ('달서구 월성·성당동 학원가는 어떤가요?', '월성동과 성당동은 대규모 아파트 단지 밀집 지역으로 내신 전문 학원들이 집중되어 있습니다. 지역 중고교 기출 분석이 오랫동안 축적되었으며, 수성구보다 학비가 합리적이면서 수업 수준은 높습니다.'),
            ('달서구에서 수성구 학원 병행이 가능한가요?', '달서구에서 수성구 범어동까지 차로 20~30분, 대구 도시철도로도 이동이 가능합니다. 내신은 달서구 학원에서 관리하고 수능 심화나 특목고 준비는 수성구 학원을 병행하는 방식이 활용됩니다.'),
            ('달서구 초등 학원 선택 기준은 무엇인가요?', '감삼동과 월성동 아파트 단지 내 소규모 학원들이 초등 관리에 특화되어 있습니다. 선행보다 현행 완성에 집중하고 숙제 관리가 철저한 학원을 우선으로 선택하세요.'),
        ],
        'extra': [
            {'h2': '월성·성당 학원가 분석', 'content': '월성동과 성당동은 달서구 최대 아파트 밀집 지역으로 내신·수능 전문 학원들이 고루 분포합니다. 성당못 인근 학원가는 20년 이상 운영된 검증된 학원들이 많아 지역 중고교 내신 기출 자료가 방대합니다. 감삼동과 죽전동의 소규모 학원들은 학생 개별 관리 수준이 높아 성적 향상 효율이 좋으며, 학부모 상담이 정기적으로 이루어지는 학원들이 신뢰를 얻고 있습니다.', 'tip': None},
            {'h2': '내신 밀착 관리 전략', 'content': '달서구 학원들은 지역 중고교 내신 기출을 철저히 분석해 시험 2~3주 전 집중 특강을 운영합니다. 학교별 담당 강사 제도를 운영하는 학원에서 같은 학교 재원생과 함께 공부하면 시험 출제 경향 파악에 가장 효율적입니다. 수학은 개념 이해 후 기출 유형 반복 풀이, 영어는 교과서 본문 완전 암기, 국어는 교사 출제 경향 분석이 내신 점수를 빠르게 끌어올리는 핵심입니다.', 'tip': '내신 시험 1주 전에는 새로운 개념 학습을 중단하고 기출과 오답 반복에만 집중하세요.'},
            {'h2': '초등 학습 습관 완성법', 'content': '달서구 초등 학원들은 학습 습관 형성을 최우선으로 운영합니다. 숙제 확인과 오답 노트 관리를 철저히 하는 학원, 학부모에게 주간 학습 현황을 공유하는 학원이 초등 시기에 가장 효과적입니다. 초등 저학년은 주 2회, 고학년은 주 3회 수업이 적당하며, 학원 수를 늘리기보다 한두 곳을 꾸준히 다니며 완성도를 높이는 것이 장기적으로 유리합니다.', 'tip': None},
        ],
    },
    '북구': {
        'subs': ['국우동', '도남동', '침산', '침산동', '원대동', '칠곡지구', '대구칠곡', '칠곡', '동천동', '복현동', '신암동', '산격동'],
        'feature': '북구는 대구 북부 최대 인구 밀집 구로 칠성동과 태전동을 중심으로 학원가가 형성되어 있습니다. 경북대학교와 인접한 산격동 일대는 대학 출신 강사들이 운영하는 전문 학원들이 분포하며, 태전지구와 관음지구 신도시 개발로 소수정예 학원 수요가 빠르게 증가하고 있습니다. 수성구보다 합리적인 학비로 지역 학교 내신에 밀착된 수업을 받을 수 있으며, 학부모 부담이 낮으면서도 성적 향상 효율이 높은 학원들이 많습니다.',
        'faq': [
            ('북구 칠성·태전동 학원가의 특징은?', '칠성동 칠성시장 인근과 태전동 신도시 아파트 단지에 내신 전문 학원들이 집중되어 있습니다. 경북대 인근 특성상 대학 출신 강사들이 운영하는 전문 학원이 많으며, 학비가 수성구보다 합리적입니다.'),
            ('북구에서 경북대 관련 입시 준비 학원은?', '산격동 경북대 인근에 논술·구술 전문 학원과 이공계 심화 학원들이 운영됩니다. 경북대 출신 강사들이 해당 학교 입시 전형을 잘 분석하고 있어 경북대 진학을 목표로 하는 학생에게 유리합니다.'),
            ('북구 태전지구 신도시 학원 수준은?', '태전지구는 2010년대 이후 대규모 아파트 단지가 들어서며 학원 수가 빠르게 늘었습니다. 젊은 학부모 비율이 높아 소수정예 관리형 학원 수요가 강하며, 신도시 커뮤니티를 통한 정보 공유가 활발합니다.'),
        ],
        'extra': [
            {'h2': '칠성·태전 학원가 분석', 'content': '칠성동 칠성네거리 인근은 북구 전통 학원가로 지역 중고교 내신 기출이 오랫동안 축적된 검증된 학원들이 운영됩니다. 태전동 신도시에는 최신 커리큘럼을 도입한 신규 학원들이 경쟁하며 수준이 빠르게 올라가고 있습니다. 경북대 인근 산격동에는 이공계 심화와 논술 전문 학원들이 있어 목적에 맞는 학원 조합이 가능합니다.', 'tip': None},
            {'h2': '합리적 학원비 활용법', 'content': '북구는 수성구 대비 학원비가 20~30% 낮아 비용 대비 효과가 높은 지역입니다. 단과 수업 조합으로 필요한 과목만 등록하면 월 비용을 크게 줄일 수 있습니다. 방학 집중 특강을 활용해 학기 중 학원 수를 줄이는 전략도 효과적이며, 학원 2~3곳을 체험한 뒤 등록하면 같은 비용으로 더 나은 수업을 받을 수 있습니다.', 'tip': '수성구 학원가와 비교해도 북구 상위 학원들의 수업 수준은 크게 차이 나지 않습니다.'},
            {'h2': '중등 내신 집중 전략', 'content': '북구 학원들은 지역 중학교 내신 기출을 기반으로 시험 2~3주 전 집중 특강을 운영합니다. 수학은 단원별 핵심 개념 정리와 기출 반복, 영어는 교과서 본문 암기와 서술형 대비가 핵심입니다. 국어는 학교 지정 교재와 교사 출제 경향에 맞춘 수업을 제공하는 학원을 선택하면 단기간에 큰 점수 차를 만들 수 있습니다.', 'tip': None},
        ],
    },
    '동구': {
        'subs': ['이시아폴리스', '봉무동'],
        'feature': '동구는 동대구역과 대구국제공항을 품은 대구 동부 교통 중심지입니다. 동대구역 인근과 신암동을 중심으로 학원들이 분포해 있으며, 율하지구 신도시 개발로 학원 수요가 빠르게 증가하고 있습니다. KTX 동대구역 덕분에 경북 지역 학생들도 동구 학원을 이용하는 경우가 있으며, 효목동과 신천동에는 지역 학교 내신에 밀착된 소수정예 학원들이 운영됩니다.',
        'faq': [
            ('동구 동대구역 인근 학원가의 특징은?', '동대구역 인근은 교통 요충지 특성상 다양한 학원들이 분포합니다. KTX 접근성 덕분에 경북 지역 학생도 이용하는 광역 학원들이 있으며, 수능 종합 학원과 단과 학원이 고루 운영됩니다.'),
            ('동구 율하지구 신도시 학원 환경은?', '율하지구는 2015년 이후 대규모 아파트 입주가 이어지며 학원 수가 빠르게 늘었습니다. 젊은 학부모 비율이 높고 소수정예 관리형 학원 수요가 강하며, 단지 커뮤니티를 통한 학원 정보 공유가 활발합니다.'),
            ('동구 중학생 수능 기초 준비는 언제 시작하나요?', '동구 학원들은 중3 2학기~고1 초반에 수능 수학 기초 개념을 시작하는 방식이 일반적입니다. 내신을 안정화한 이후 수능 기초를 병행하는 것이 효율적입니다.'),
        ],
        'extra': [
            {'h2': '동대구·신암 학원가 분석', 'content': '동대구역 1·2번 출구 인근과 신암동 주거지에 학원들이 분포해 있습니다. 동대구역의 교통 편의성 덕분에 수성구·북구 학원가와 연계 이용이 편리하며, 수능 심화나 특목고 입시는 수성구 학원을 병행하는 학생도 있습니다. 율하지구에는 최신 커리큘럼을 도입한 신규 학원들이 경쟁 중이며, 효목동 기존 학원들은 지역 내신 기출 분석에 강합니다.', 'tip': None},
            {'h2': '교통 허브 학원 활용법', 'content': '동구는 KTX 동대구역과 대구국제공항이 있어 대구 내 교통 접근성이 최상입니다. 이 교통 인프라를 활용해 내신은 동구 지역 학원에서, 수능 심화는 수성구 범어·만촌 학원을 주 1~2회 병행하는 방식이 효율적입니다. 동구에서 수성구까지 대구 도시철도로 20분 내외로 이동이 가능합니다.', 'tip': '학원 시간대와 귀가 동선을 미리 설계해두면 병행 학원 이용이 훨씬 수월합니다.'},
            {'h2': '고등 수능 단계별 전략', 'content': '동구 고등 학원들은 고1 내신 안정화를 최우선으로 하고, 고2부터 수능 비중을 점진적으로 높이는 방식을 채택합니다. 수학은 수능 기출 유형 분석과 오답 반복 정리를 꾸준히 진행하고, 영어는 EBS 연계 교재 독해 속도를 끌어올립니다. 국어 비문학은 꾸준한 훈련이 필요하므로 고1 초반부터 주 1회 이상 단과 수업을 유지하는 것이 좋습니다.', 'tip': None},
        ],
    },
    '중구': {
        'subs': ['반월당', '고성동', '칠성동', '수창동'],
        'feature': '대구 중구는 대구 도심 한가운데 위치한 구로 동성로 상권과 대구역을 중심으로 학원들이 분포해 있습니다. 도심 특성상 주거 인구보다 유동 인구가 많아 대형 학원보다 단과 전문 학원과 소수정예 학원들이 강세입니다. 대구 1·2호선이 교차하는 교통 허브로 중구 학원들은 인근 구 학생들도 이용하는 광역 학원 성격이 강하며, 국어·논술·영어 회화 전문 학원들이 특히 발달해 있습니다.',
        'faq': [
            ('대구 중구 학원가의 특징은 무엇인가요?', '동성로와 대구역 인근에 단과 전문 학원들이 집중되어 있습니다. 도심 특성상 과목별 단과 학원 조합이 자유롭고, 대구 전역에서 교통으로 접근하기 편리합니다.'),
            ('중구 학원을 이용하는 학생들은 주로 어디서 오나요?', '중구 자체 거주 학생 외에 수성구·달서구·북구에서 도심 학원을 이용하는 학생들이 많습니다. 특히 논술·수능 국어 전문 학원의 경우 대구 전역에서 통학하는 학생이 있습니다.'),
            ('대구 중구에서 논술 준비가 가능한가요?', '동성로 인근에 논술·구술 전문 학원들이 운영됩니다. 대구·경북 지역 주요 대학 기출 분석과 첨삭이 체계적으로 이루어지며, 고2 초반부터 준비를 시작하는 것이 이상적입니다.'),
        ],
        'extra': [
            {'h2': '대구 도심 학원가 분석', 'content': '대구역 인근과 동성로 일대에 수능 국어·영어·논술 전문 학원들이 분포해 있습니다. 도심 학원들은 대구 전역에서 접근이 편리해 과목별 단과 학원을 조합하는 방식으로 이용하는 학생이 많습니다. 삼덕동과 남산동에는 소수정예 학원들이 소그룹 수업으로 개인 관리에 강점을 보이며, 특히 수능 국어와 논술 분야에서 두각을 나타내는 학원들이 있습니다.', 'tip': None},
            {'h2': '단과 학원 조합 전략', 'content': '대구 중구는 과목별 단과 학원이 잘 발달해 있어 필요한 과목만 골라 조합하는 방식이 효율적입니다. 수학은 거주 지역 학원에서, 수능 국어나 논술은 중구 전문 학원을 이용하는 식으로 역할을 나누면 비용과 효율을 동시에 잡을 수 있습니다. 단과 학원을 너무 많이 조합하면 이동 시간이 늘어 오히려 학습 효율이 떨어질 수 있으니 최대 3~4과목으로 제한하는 것이 현실적입니다.', 'tip': '과목별 단과 조합 시 이동 동선과 총 학원 시간을 먼저 계산해두세요.'},
            {'h2': '고등 문과 입시 전략', 'content': '대구 중구 학원들은 수능 국어·영어·수학(문과형)과 사회탐구 단과 수업을 체계적으로 운영합니다. 문과 수시를 목표로 한다면 국어와 사회탐구 내신을 철저히 관리하면서 학생부 세특을 전략적으로 설계해야 합니다. 논술 전형은 고2 초반부터 대구·경북 주요 대학의 기출 논술 분석과 첨삭을 반복하는 것이 핵심입니다.', 'tip': None},
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
for gu, data in daegu.items():
    path = os.path.join(base, DO, gu, 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(make_html(gu, data))
    count += 1
    print(f'생성: {DO}/{gu}')

print(f'\n완료: {count}개 페이지')
