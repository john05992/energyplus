"""
사이트맵.py
===========
새로운학원/ 아래 생성된 index.html 을 스캔해서 sitemap.xml 을 만든다.

실행: python 사이트맵.py
출력: 새로운학원/sitemap.xml
"""

import sys
from pathlib import Path
from datetime import date

sys.stdout.reconfigure(encoding='utf-8')

BASE  = Path(r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원')
SITE  = 'https://energyplus.kr'
TODAY = date.today().isoformat()

# 레벨별 우선순위 / 갱신주기
LEVEL_CONFIG = {
    0: ('1.0',  'daily'),    # 루트
    1: ('0.9',  'weekly'),   # 도
    2: ('0.8',  'weekly'),   # 시/구
    3: ('0.7',  'weekly'),   # 동
    4: ('0.6',  'monthly'),  # 학년
    5: ('0.5',  'monthly'),  # 키워드
}


def path_to_url(html_path: Path) -> str:
    """index.html 절대경로 → 사이트 URL"""
    rel = html_path.relative_to(BASE).parent  # index.html 제외
    parts = rel.parts
    if parts == ('.', ) or parts == ():
        return f'{SITE}/'
    return SITE + '/' + '/'.join(parts) + '/'


def get_level(html_path: Path) -> int:
    """디렉터리 깊이 = 레벨 (BASE 기준 0이 루트)"""
    rel = html_path.relative_to(BASE).parent
    parts = [p for p in rel.parts if p != '.']
    return len(parts)


def make_url_entry(loc: str, priority: str, changefreq: str) -> str:
    return (
        '  <url>\n'
        f'    <loc>{loc}</loc>\n'
        f'    <lastmod>{TODAY}</lastmod>\n'
        f'    <changefreq>{changefreq}</changefreq>\n'
        f'    <priority>{priority}</priority>\n'
        '  </url>'
    )


def main():
    entries = []

    # 루트 페이지
    root_pri, root_freq = LEVEL_CONFIG[0]
    entries.append((0, f'{SITE}/', root_pri, root_freq))

    # 생성된 index.html 전체 스캔
    for html in sorted(BASE.rglob('index.html')):
        level = get_level(html)
        url   = path_to_url(html)
        pri, freq = LEVEL_CONFIG.get(level, ('0.4', 'monthly'))
        entries.append((level, url, pri, freq))

    # 레벨 → URL 순 정렬
    entries.sort(key=lambda x: (x[0], x[1]))

    url_tags = [make_url_entry(url, pri, freq) for _, url, pri, freq in entries]

    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + '\n'.join(url_tags) + '\n'
        '</urlset>\n'
    )

    out = BASE / 'sitemap.xml'
    out.write_text(sitemap, encoding='utf-8')
    print(f'완료: {len(entries)}개 URL → {out}')


if __name__ == '__main__':
    main()
