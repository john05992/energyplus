"""
fix_perf.py
===========
모든 HTML 파일의 렌더링 차단 요청 제거:
  1. Google Fonts → 비동기 로드 (media="print" onload 트릭)
  2. /css/style.css → preload + onload
"""

import os, re

BASE = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'

# ── 기존 패턴 ──────────────────────────────────────────────────────────
OLD_FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@800&display=swap" rel="stylesheet">'
)

OLD_CSS = '<link rel="stylesheet" href="/css/style.css">'

# ── 교체할 패턴 ────────────────────────────────────────────────────────
NEW_FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@800&display=swap">\n'
    '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@800&display=swap" media="print" onload="this.media=\'all\'">\n'
    '  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@800&display=swap"></noscript>'
)

NEW_CSS = (
    '<link rel="preload" href="/css/style.css" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n'
    '  <noscript><link rel="stylesheet" href="/css/style.css"></noscript>'
)

# ── 실행 ──────────────────────────────────────────────────────────────
updated = 0
skipped = 0

for root, dirs, files in os.walk(BASE):
    # gen_ 스크립트나 __pycache__ 제외
    dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git']]
    for fname in files:
        if not fname.endswith('.html'):
            continue
        path = os.path.join(root, fname)
        with open(path, encoding='utf-8') as f:
            html = f.read()

        changed = False

        if OLD_FONTS in html:
            html = html.replace(OLD_FONTS, NEW_FONTS)
            changed = True

        if OLD_CSS in html:
            html = html.replace(OLD_CSS, NEW_CSS)
            changed = True

        if changed:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            updated += 1
        else:
            skipped += 1

print(f'완료 — 업데이트: {updated}개 / 변경 없음: {skipped}개')
