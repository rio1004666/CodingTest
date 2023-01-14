"""
문제이해
L자리 비밀번호를 만들기
조건1. 같은숫자 중복 안됨
조건2. 다른숫자를 건너뛰게 이동하는거 안됨
조건3. 내가 완성한 비밀번호 그린후 선분사이의 교차점이 하나이상 존재
k개의 고장난 숫자는 사용하지 않는다


번호판을 재배정하기
사각형테두리를 원형으로 배치하기 - 교차판정쉽게한다
1 2 3     0 1 2
4 5 6  -> 7 8 3    (1이 0으로 2가 1로 3이 2로 6이 3으로 이렇게 원으로 간다)
7 8 9     6 5 4
1과 4가 연결된 선분이라면
영역이 나뉜다 그리고 나누어진 두 영역에서
연결이 이루어지면 교차가 일어나고
한영역에서만 선분이 이루어지면 교차가 없어진다
이제 이렇게 아이디어를 구상했다면
완전탐색으로 구현한다

그리고 8은 가운데에 있으므로 어디에든 갈 수 있다
8은 예외처리한다
0은 8을 빼면 홀수만 갈 수 있다
왜냐면 조건2에서 한칸 건너뛰어서 이동할 수 없다고 했으므로
이것을 원형판에 적용했을 때 0번위치에 있는 점은
2,4,6을 가지 못한다 ( 조건2번에 의해서 )
2도 다 홀수만 갈 수 있다 ( 원형모양에서 )
홀수번호는 맞은편의 점만 가지 못한다 (4차이만큼나면 못간다)
"""
import sys

si = sys.stdin.readline
L, K = map(int, si().split())
banned = [False for _ in range(10)]
# 사각형 격자를 원형으로 변환하는 테크닉 ( 중복 없음 )
conv = {
    1: 0,
    2: 1,
    3: 2,
    4: 7,
    5: 8,
    6: 3,
    7: 6,
    8: 5,
    9: 4,
}
# 사각형에서의 금지된 숫자를 원형에서의 금지된 숫자로 체크
for b in map(int, si().split()):
    banned[conv[b]] = True
ans = 0


def can_go(x, y):
    # 두개의 점을 파라미터로 받아서 한개의 점이라도 8이 있다면 어느점이든 갈 수 있음
    if 8 in (x, y):  # 8은 중앙에 있으니 모든 점 갈 수 있다
        return True
    if x % 2 == 0:  # 짝수는 홀수랑 8만 갈 수 있다.
        return y % 2 == 1
    return abs(x - y) != 4  # 홀수는 정반대 위치 빼고 다 갈 수 있다.


def is_cross(x1, y1, x2, y2):
    x1, y1 = min(x1, y1), max(x1, y1)
    x2, y2 = min(x2, y2), max(x2, y2)
    if x1 in (x2, y2) or y1 in (x2, y2):
        return False
    if 8 in (x1, y1):
        return is_cross(x2, y2, x1, y1)
    shorts = []
    if y1 - x1 < 4:
        v = x1
    else:
        v = y1
    while True:
        v = (v + 1) % 8
        if v == y1 or v == x1:
            break
        shorts.append(v)
    assert len(shorts) <= 2
    if x2 in shorts and y2 not in shorts:
        return True
    if x2 not in shorts and y2 in shorts:
        return True
    return False


def func(len, cur, visit, lines):
    # 현재까지 길이가 len 이고, 마지막에 cur에 위치 했다.
    # 이미 사용한 숫자들은 visit에, 사용한 선분들은 lines 로 저장된다.
    global ans
    if len == L:
        cross = False
        for l1 in lines:
            for l2 in lines:
                if is_cross(l1[0], l1[1], l2[0], l2[1]):
                    cross = True
        if cross:
            ans += 1
        return

    visit[cur] = True
    for nxt in range(9):
        if visit[nxt]: continue
        if banned[nxt]: continue
        if not can_go(cur, nxt): continue
        func(len + 1, nxt, visit, lines + [(cur, nxt)])
    visit[cur] = False

# 모든 점을 돌면서 갈 수 있는 점들을 방문한다
for i in range(9):
    if banned[i]: continue
    func(1, i, [False for _ in range(10)], [])
print(ans)