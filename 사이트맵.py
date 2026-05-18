"""
사이트맵.py
===========
sitemap-index.xml + 도별 sitemap-{en}.xml 16개 생성.

실행: python 사이트맵.py
출력: 새로운학원/sitemap-index.xml
      새로운학원/sitemap-seoul.xml ... (16개)
"""

import sys
from pathlib import Path
from datetime import date

sys.stdout.reconfigure(encoding='utf-8')

BASE  = Path(r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원')
SITE  = 'https://energyplus.kr'
TODAY = date.today().isoformat()

# 도 → 영문 파일명
DO_EN = {
    '강원도':        'gangwon',
    '경기도':        'gyeonggi',
    '경상남도':      'gyeongnam',
    '경상북도':      'gyeongbuk',
    '광주광역시':    'gwangju',
    '대구광역시':    'daegu',
    '대전광역시':    'daejeon',
    '부산광역시':    'busan',
    '서울특별시':    'seoul',
    '세종시':        'sejong',
    '울산광역시':    'ulsan',
    '인천광역시':    'incheon',
    '전북특별자치도':'jeonbuk',
    '제주도':        'jeju',
    '충청남도':      'chungnam',
    '충청북도':      'chungbuk',
}

# 레벨별 우선순위 / 갱신주기
LEVEL_CONFIG = {
    0: ('1.0', 'daily'),
    1: ('0.9', 'weekly'),
    2: ('0.8', 'weekly'),
    3: ('0.7', 'weekly'),
    4: ('0.6', 'monthly'),
    5: ('0.5', 'monthly'),
}


def path_to_url(html_path: Path) -> str:
    rel = html_path.relative_to(BASE).parent
    parts = rel.parts
    if not parts or parts == ('.',):
        return f'{SITE}/'
    return SITE + '/' + '/'.join(parts) + '/'


def get_level(html_path: Path) -> int:
    rel = html_path.relative_to(BASE).parent
    return len([p for p in rel.parts if p != '.'])


def make_url_entry(loc: str, priority: str, changefreq: str) -> str:
    return (
        '  <url>\n'
        f'    <loc>{loc}</loc>\n'
        f'    <lastmod>{TODAY}</lastmod>\n'
        f'    <changefreq>{changefreq}</changefreq>\n'
        f'    <priority>{priority}</priority>\n'
        '  </url>'
    )


def make_sitemap(url_tags: list) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + '\n'.join(url_tags) + '\n'
        '</urlset>\n'
    )


def main():
    # 도별 URL 수집
    do_entries: dict[str, list] = {do: [] for do in DO_EN}
    root_entries = []

    # 루트 페이지
    pri, freq = LEVEL_CONFIG[0]
    root_entries.append(make_url_entry(f'{SITE}/', pri, freq))

    for html in sorted(BASE.rglob('index.html')):
        level = get_level(html)
        url   = path_to_url(html)
        pri, freq = LEVEL_CONFIG.get(level, ('0.4', 'monthly'))
        entry = make_url_entry(url, pri, freq)

        # 첫 번째 경로 파트가 도 이름
        rel_parts = [p for p in html.relative_to(BASE).parent.parts if p != '.']
        if rel_parts and rel_parts[0] in do_entries:
            do_entries[rel_parts[0]].append(entry)
        else:
            root_entries.append(entry)

    # 도별 sitemap 파일 생성
    sitemap_files = []
    for do, en in DO_EN.items():
        entries = do_entries.get(do, [])
        if not entries:
            continue
        filename = f'sitemap-{en}.xml'
        content  = make_sitemap(entries)
        (BASE / filename).write_text(content, encoding='utf-8')
        sitemap_files.append((filename, len(entries)))
        print(f'  {filename}: {len(entries)}개')

    # 루트 sitemap (루트 index.html 포함)
    if root_entries:
        root_file = 'sitemap-root.xml'
        (BASE / root_file).write_text(make_sitemap(root_entries), encoding='utf-8')
        sitemap_files.insert(0, (root_file, len(root_entries)))
        print(f'  {root_file}: {len(root_entries)}개')

    # sitemap-index.xml 생성
    index_entries = '\n'.join(
        f'  <sitemap>\n'
        f'    <loc>{SITE}/{fname}</loc>\n'
        f'    <lastmod>{TODAY}</lastmod>\n'
        f'  </sitemap>'
        for fname, _ in sitemap_files
    )
    index_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + index_entries + '\n'
        '</sitemapindex>\n'
    )
    (BASE / 'sitemap-index.xml').write_text(index_xml, encoding='utf-8')

    total = sum(c for _, c in sitemap_files)
    print(f'\n완료: sitemap-index.xml + {len(sitemap_files)}개 파일 / 총 {total}개 URL')


if __name__ == '__main__':
    main()
