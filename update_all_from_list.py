"""
update_all_from_list.py
=======================
학원목록.txt 를 읽어 gen_do.py · gen_si_*.py 의 subs 를 자동으로 수정한 뒤
모든 generator 를 실행하여 index.html 을 재생성합니다.

  [레벨1] gen_do.py   : 각 도(道)의 'subs' → 학원목록.txt col2 시/구 목록
  [레벨2] gen_si_*.py : 각 시/구의 'subs' → 학원목록.txt col4 동 키워드 목록
          - '구' 로 끝나는 행정구 이름 제외  (단, '지구'는 유지)
          - '시' 로 끝나는 행정시 이름 제외
          - '특별시', '광역시', '자치도' 등 광역 행정명 제외
"""

import re
import os
import subprocess
from collections import defaultdict

LIST_FILE = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원\학원목록.txt'
GEN_DIR   = r'C:\Users\tlsdy\OneDrive\바탕 화면\새로운학원'

# ── 학원목록.txt col4 동 키워드 유효성 필터 ──────────────────────────
def is_dong_kw(kw):
    """레벨3 URL에 사용할 수 있는 동 단위 키워드면 True"""
    for e in ('특별시', '광역시', '특별자치도', '자치도', '자치시'):
        if kw.endswith(e):
            return False
    # '구' 로 끝나면 행정구 → 제외 (단, '지구'처럼 '지구'로 끝나면 유지)
    if kw.endswith('구') and not kw.endswith('지구'):
        return False
    # '시' 로 끝나면 행정시 → 제외
    if kw.endswith('시'):
        return False
    return True

# ── 학원목록.txt 파싱 ────────────────────────────────────────────────
# si_map  : {도: [시/구, ...]}                 (레벨1 subs 용)
# dong_map: {도: {시/구: [동키워드, ...]}}      (레벨2 subs 용)

si_map    = defaultdict(list)
dong_map  = defaultdict(lambda: defaultdict(list))
si_seen   = set()
dong_seen = set()
cur_do = cur_si = None

with open(LIST_FILE, encoding='utf-8') as f:
    for line in f:
        cols = line.rstrip('\n').split('\t')
        if len(cols) < 4:
            continue
        do   = cols[0].strip()
        si   = cols[1].strip()
        dong = cols[3].strip()

        if do:  cur_do = do
        if si:  cur_si = si
        if not (cur_do and cur_si):
            continue

        # 레벨1: 시/구 수집
        k = (cur_do, cur_si)
        if k not in si_seen:
            si_seen.add(k)
            si_map[cur_do].append(cur_si)

        # 레벨2: 동 키워드 수집
        if dong and is_dong_kw(dong):
            k2 = (cur_do, cur_si, dong)
            if k2 not in dong_seen:
                dong_seen.add(k2)
                dong_map[cur_do][cur_si].append(dong)

# ── 파싱 결과 출력 ───────────────────────────────────────────────────
print("=" * 60)
print("학원목록.txt 파싱 결과")
print("=" * 60)
for do, si_list in sorted(si_map.items()):
    print(f"\n[{do}]  시/구 {len(si_list)}개")
    for si in si_list:
        dongs = dong_map[do].get(si, [])
        print(f"  {si}: {dongs}")

# ── gen_do.py / gen_si_*.py 파일 내 subs 교체 함수 ──────────────────
def update_subs_in_file(filepath, key_subs_map):
    """
    filepath 의 Python 소스에서 key_subs_map 에 있는 키의
    'subs': [...] 를 새 리스트로 교체한다.
    key_subs_map: {키이름: [새 subs 리스트]}
    변경된 키 목록 반환.
    """
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()

    result  = []
    changed = []
    i = 0

    while i < len(lines):
        line = lines[i]
        # '키이름': { 패턴 (도/시/구 딕셔너리 항목 시작)
        m = re.match(r"\s*'([^']+)'\s*:\s*\{", line)
        if m and m.group(1) in key_subs_map:
            key = m.group(1)
            result.append(line)
            i += 1
            # 바로 다음 'subs': 라인 찾기 (최대 3라인 탐색)
            searched = 0
            while i < len(lines) and searched < 3:
                if "'subs':" in lines[i]:
                    indent = len(lines[i]) - len(lines[i].lstrip())
                    new_line = ' ' * indent + f"'subs': {repr(key_subs_map[key])},\n"
                    result.append(new_line)
                    changed.append(key)
                    i += 1
                    break
                else:
                    result.append(lines[i])
                    i += 1
                    searched += 1
        else:
            result.append(line)
            i += 1

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(result)

    return changed

# ── 도 → gen_si 파일 매핑 ────────────────────────────────────────────
DO_FILE_MAP = {
    '서울특별시':      ['gen_si_seoul.py'],
    '경기도':          ['gen_si_gyeonggi.py', 'gen_si_gyeonggi2.py'],
    '인천광역시':      ['gen_si_incheon.py'],
    '부산광역시':      ['gen_si_busan.py'],
    '대구광역시':      ['gen_si_daegu.py'],
    '대전광역시':      ['gen_si_daejeon.py'],
    '광주광역시':      ['gen_si_gwangju.py'],
    '울산광역시':      ['gen_si_ulsan.py'],
    '강원도':          ['gen_si_gangwon.py'],
    '충청남도':        ['gen_si_chungnam.py'],
    '충청북도':        ['gen_si_chungbuk.py'],
    '전북특별자치도':  ['gen_si_jeonbuk.py'],
    '경상북도':        ['gen_si_gyeongbuk.py'],
    '경상남도':        ['gen_si_gyeongnam.py'],
}

# ── [레벨1] gen_do.py : 도 → 시/구 subs 수정 ───────────────────────
# 세종시는 동 단위 직접 처리(gen_si 없음)이므로 제외
SKIP_DO    = {'세종시', '제주도'}
GEN_DO     = os.path.join(GEN_DIR, 'gen_do.py')

# 학원목록.txt 에 있는 시/구만 포함
# (단, 학원목록.txt 데이터 오류인 '용신시' 등의 오타도 포함될 수 있으므로
#  gen_do.py 에 이미 있는 도 키만 업데이트)
do_update_map = {}
for do, si_list in si_map.items():
    if do in SKIP_DO:
        continue
    # 중복 제거 + 기존 순서 유지 (학원목록.txt 등장 순서)
    do_update_map[do] = si_list

print("\n" + "=" * 60)
print("[레벨1] gen_do.py  도→시/구 subs 수정")
print("=" * 60)
changed = update_subs_in_file(GEN_DO, do_update_map)
print(f"수정된 도: {changed if changed else '없음'}")

# ── [레벨2] gen_si_*.py : 시/구 → 동 subs 수정 ─────────────────────
print("\n" + "=" * 60)
print("[레벨2] gen_si_*.py  시/구→동 subs 수정")
print("=" * 60)

for do_name, files in DO_FILE_MAP.items():
    if do_name not in dong_map:
        print(f"\n[{do_name}] 학원목록에 데이터 없음 → 스킵")
        continue
    si_dong = dict(dong_map[do_name])
    for fname in files:
        fpath = os.path.join(GEN_DIR, fname)
        if not os.path.exists(fpath):
            continue
        changed = update_subs_in_file(fpath, si_dong)
        print(f"\n[{do_name}] {fname}")
        print(f"  수정: {changed if changed else '없음'}")

# ── HTML 재생성 : gen_do.py + gen_si_*.py 실행 ──────────────────────
print("\n" + "=" * 60)
print("HTML 재생성")
print("=" * 60)

gen_files = ['gen_do.py'] + [
    fname
    for flist in DO_FILE_MAP.values()
    for fname in flist
]

for fname in gen_files:
    fpath = os.path.join(GEN_DIR, fname)
    if not os.path.exists(fpath):
        continue
    res = subprocess.run(
        ['python', fpath],
        capture_output=True, text=True, cwd=GEN_DIR
    )
    if res.returncode != 0:
        print(f"  {fname}: 오류 → {res.stderr.strip()[:200]}")
    else:
        last = res.stdout.strip().split('\n')[-1] if res.stdout.strip() else '완료'
        print(f"  {fname}: {last}")

print("\n전체 완료!")
