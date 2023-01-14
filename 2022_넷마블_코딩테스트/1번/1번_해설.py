# 문제이해
"""
n행 m열 미로가 주어지고 (1,1)위치부터 숫자가 써져있다
사람이 (1,1) 위치에서 유저의 레벨 1부터 시작하고
가장 빠르게 최강의 몬스터를 잡는것
격자에 써져있는 숫자가 곧 몬스터의 레벨이고
목표는 최강의 몬스터는 곧 레벨이 가장 높은 몬스터이다
어떻게 플레이를 해야 최대한 빠른 시간 안에 최강의 몬스터를 잡을 수 있는가
가능한 경우가 여러가지라면 유저의 가장 높은레벨을 달성하려면 어떻게?

관찰 - 첫번째 선택지는 자기자리에서 사냥을 하는것 - 움직이지 않고 사냥해서 레벨올라감
레벨 올라가는 규칙은 몬스터의 레벨의 4배이상 높으면 레벨이 1오름
또 2배이상 높으면 레벨 2 오른다
그외에는 충분히 강한 몬스터라고 생각하여 레벨이 3 오른다
0이 써져있는 위치는 몬스터가 없다

두번째 선택지는 상하좌우로 이동한다 이동시에 내 레벨이 가고 싶은 위치의 몬스터보다
낮으면 갈 수 없다

선택을 최소 몇번해야 최강의 몬스터를 잡을 수 있을지
그 경우의 수가 여러가지라면 그 시간에 최대레벨을 어디까지 올릴 수 있을지
n,m <= 50
몬스터 레벨은 100까지 가능
원래 일반적인 최단거리는 위치의 정보만 가지고 그래프 탐색을 하나 ,
관철 - 최단시간 - 최단거리 - 그래프 잘 모델링해서 최단거리 알고리즘으로 구현
이 문제에서는 레벨도 존재하기때문에
정점을 n x m x 110개의 정점을 만들것이다
각 정점은 특정위치에서 x행 y열에서 레벨이 lv인 상태를 의미 - 상태 그래프 ( 레벨도 그래프에 같이 저장해준다 )
또 한번에 레벨이 많이 올라밧자 3개만 오르기 때문에

간선의 정의는  ( x,y,lb )
첫번째 간선은 위치는 그대로 있고 레벨만 오르는 선택지로 상태가 변함 (1가지)
두번째 간선은 인접한 칸으로 이동한 레벨은 그대로 (4가지)
최강의 몬스터에서 제일 빠른시간에 도착한 정점이 답이 된다
"""
# 스킵
import sys
from collections import deque
si = sys.stdin.readline
n, m = map(int, si().split())
MAX = 100000
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
a = [list(map(int, si().split())) for _ in range(n)]
gx, gy = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] > a[gx][gy]:
            gx, gy = i, j
dist = [[[MAX for _ in range(150)] for _ in range(m)] for _ in range(n)]
dist[0][0][1] = 0
q = deque()
q.append((0, 0, 1))
arrive_min_dist, max_lv = MAX, 0
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m
while q:
    x, y, lv = q.popleft()
    d = dist[x][y][lv]
    if d + 1 > arrive_min_dist:
        continue
    # move
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny):
            continue
        if dist[nx][ny][lv] <= d + 1:
            continue
        if a[nx][ny] > lv:
            continue
        dist[nx][ny][lv] = d + 1
        q.append((nx, ny, lv))
    # lv up
    if a[x][y] > 0:
        if a[x][y] <= lv // 4:
            nlv = lv + 1
        elif a[x][y] <= lv // 2:
            nlv = lv + 2
        else:
            nlv = lv + 3
        if dist[x][y][nlv] > d + 1:
            dist[x][y][nlv] = d + 1
            if x == gx and y == gy:
                if arrive_min_dist > d + 1:
                    arrive_min_dist = d + 1
                if arrive_min_dist == d + 1:
                    max_lv = max(max_lv, nlv)
            else:
                q.append((x, y, nlv))
print(arrive_min_dist, max_lv)