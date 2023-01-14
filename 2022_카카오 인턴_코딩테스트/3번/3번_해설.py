import sys

MAX = 1000000000
si = sys.stdin.readline
SA, SB = map(int, si().split())
GA, GB = 0, 0
N = int(si())
items = [list(map(int, si().split())) for _ in range(N)]
for RA, RB, _, _, _ in items:
    GA = max(GA, RA)
    GB = max(GB, RB)
dy = [[MAX for _ in range(200)] for __ in range(200)]
dy[SA][SB] = 0


def renew(nextA, nextB, newValue):
    # dy[nextA][nextB] 를 newValue 로 갱신시켜라
    nextA = min(nextA, GA)
    nextB = min(nextB, GB)
    dy[nextA][nextB] = min(dy[nextA][nextB], newValue)


ans = MAX
for A in range(GA + 1):
    for B in range(GB + 1):
        # 현재 능력치가 A, B 이다.
        if dy[A][B] == MAX:
            # 도달할 수 없는 불가능한 상황
            continue

        # dy[A][B] 값을 알고 있다 == 시작 상황에서 A, B 까지 필요한 최소 시간을 안다.

        # 1. 이 순간에 1번 작업을 했을 때
        renew(A + 1, B, dy[A][B] + 1)
        # 2. 이 순간에 2번 작업을 했을 때
        renew(A, B + 1, dy[A][B] + 1)
        # 3. 이 순간에 아이템을 썼을 때
        for RA, RB, CA, CB, T in items:
            if A < RA or B < RB:
                continue
            nextA, nextB = A + CA, B + CB
            renew(nextA, nextB, dy[A][B] + T)
print(dy[GA][GB])