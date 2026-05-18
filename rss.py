"""
rss.py
======
feed.xml 생성 (네이버 서치어드바이저 RSS 제출용)
도/시/동 레벨(1~3) 페이지를 최대 200개 포함.

실행: python rss.py
출력: 새로운학원/feed.xml
"""

import sys
import urllib.parse
from pathlib import Path
from datetime import date

sys.stdout.reconfigure(encoding='utf-8')

BASE  = Path(r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원')
SITE  = 'https://energyplus.kr'
BRAND = '동네학원 찾기 - 에너지+'
TODAY = date.today().isoformat()
MAX_ITEMS = 200


def path_to_url(html_path: Path) -> str:
    rel = html_path.relative_to(BASE).parent
    parts = rel.parts
    if not parts or parts == ('.',):
        return f'{SITE}/'
    encoded = '/'.join(urllib.parse.quote(p, safe='') for p in parts)
    return SITE + '/' + encoded + '/'


def path_to_title(html_path: Path) -> str:
    rel = html_path.relative_to(BASE).parent
    parts = [p for p in rel.parts if p != '.']
    if not parts:
        return '전국 동네 학원 찾기 - 에너지+'
    return ' > '.join(parts) + ' 학원 정보'


def main():
    items = []

    # 루트
    items.append((f'{SITE}/', '전국 동네 학원 찾기 - 에너지+'))

    # 레벨 1~3 (도 / 시 / 동)
    for html in sorted(BASE.rglob('index.html')):
        rel = html.relative_to(BASE).parts
        if rel and rel[0] == '과외':
            continue
        depth = len([p for p in html.relative_to(BASE).parent.parts if p != '.'])
        if depth < 1 or depth > 3:
            continue
        url   = path_to_url(html)
        title = path_to_title(html)
        items.append((url, title))

    items = items[:MAX_ITEMS]

    rss_items = '\n'.join(
        f'    <item>\n'
        f'      <title>{title}</title>\n'
        f'      <link>{url}</link>\n'
        f'      <guid>{url}</guid>\n'
        f'      <pubDate>{TODAY}</pubDate>\n'
        f'    </item>'
        for url, title in items
    )

    feed = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        '  <channel>\n'
        f'    <title>{BRAND}</title>\n'
        f'    <link>{SITE}/</link>\n'
        f'    <atom:link href="{SITE}/feed.xml" rel="self" type="application/rss+xml"/>\n'
        '    <description>전국 동네 학원 정보를 지역별로 제공합니다.</description>\n'
        '    <language>ko</language>\n'
        f'    <lastBuildDate>{TODAY}</lastBuildDate>\n'
        f'{rss_items}\n'
        '  </channel>\n'
        '</rss>\n'
    )

    (BASE / 'feed.xml').write_text(feed, encoding='utf-8')
    print(f'완료: feed.xml 생성 ({len(items)}개 항목)')


if __name__ == '__main__':
    main()
