# d로 가는게 좋을지 l로가는게 좋을지 r로가는게 좋을지 선택한다 처음에
# 무조건 d...이 사전순으로 앞서기때문에 아랫쪽으로 갈 수 있으면 가는게 이득이다
# 조건
# 1. 격자를 벗어나면 안된다
# 2. 이동한다고 했을 경우 도착도 가능한지 확인해야한다
# 그러면 k번만에 갈 수 있는가? 만 체크하면 된다 => 관철하면
# 1번이동,2번이동,...k번 이동동안 각 4가지의 방향중 우선순위에서 바로 갈 수 있는지만 체크하면 된다
# 나의 생각은 비슷햇지만 k번동안 움직이면서 갈수있냐 안갈수있냐 체크 하는 로직을 생각하지 못했다
# k번이라는 키워드로 차례대로 보면되는것이다
# 시간복잡도는 최대 k=2500 * dir = 4  = 10000이다
import sys
si = sys.stdin.readline
N, M, sx, sy, ex, ey, K = map(int, si().split())
# 두 정점 사이의 맨하튼 거리 = 행차이 + 열차이 계산
def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
# 현재위치에서 도착지점까지 갈 수 있는지 체크하는 함수
def possible(x, y, K):
    # (x, y)에서 도착 지점까지 K번 만에 갈 수 있어?
    # 격자밖을 벗어날 수 없음을 의미
    if not (1 <= x <= N and 1 <= y <= M):
        return False
    # 현재 위치에서 맨허튼거리를 구하고 미래에 k번만에 갈 수 없음을 의미
    if get_dist(x, y, ex, ey) > K:
        return False
    # 위의 두 경우 조건이 충족되지 않으면 갈 수 있음
    return True
x, y = sx, sy
ans = []
# k번동안 움직일 것이고 지금 시작위치에 있다 => 시뮬레이션 시행
for _ in range(K):
    move = None
    # 이렇게 각 방향을 탐색하면서 다음칸 이동시 도착지에 도착할 수 있는지 계속 판단하면서 가면 인공지능처럼 k번만에 찾아갈 수 있는 경로로 찾아가게 된다
    for dir, dx, dy in [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]:
        if possible(x + dx, y + dy, K - 1):
            move = dir
            x += dx
            y += dy
            K -= 1
            break # 다른방향은 굳이 탐색할 필요가 없다
    # 모든 방향을 한번씩 가봣는데 거리가 멀어서 못간다면 진행하지 않는다
    if move == None:
        print("Impossible")
        exit()
    ans.append(move)
print(''.join(ans))
