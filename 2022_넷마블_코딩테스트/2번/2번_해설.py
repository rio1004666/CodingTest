"""
문제이해
피자가 육각형모양으로 있다
각 위치마다 토핑이 있는데 토핑은 알파벳 대문자로 표현
피자의 아름다움은 모든 육각형을 골라서 한변의 길이가 2이상인 육각형의 테두리의 점수(종류별 1점)의 제곱의 합
한변의 길이가 50인 정육각모양의 아름다움의 점수를 구하기
네이버신입공채와 문제스타일이 비슷 육각형 격자
빡구현..... => 어떻게 짜느냐에 따라 코드량이 달라짐
관찰 : 육각형 테두리 => 특정중심으로부터 동일한 거리
거리가 1 => 육각형 6개
거리가 2 => 육각형 12개
모든 육각형인애들을 본다면 시작점을 중심으로 모든지점애들의 최단거리 알고리즘을 사용
온전히 모든 육각형들을 볼수있는 거리를 찾아서 탐색 BFS => 이것이 포인트
거리 -> 관찰 포인트

육각형이라고 겁먹을 필요없이 이동하면 얼마만큼의 변화량이 생기는지 정의한다 get_dir부분

"""

import sys
from collections import deque

si = sys.stdin.readline
n = int(si())
board = [list(si().strip()) for _ in range(n * 2 - 1)]
ans = 0


def in_range(x, y):
    if x < 0 or x >= len(board):
        return False
    if y < 0 or y >= len(board[x]):
        return False
    return True


def get_dirs(x, y):
    if x < n - 1:
        return ((-1, -1), (-1, 0), (0, 1), (1, 1), (1, 0), (0, -1))
    elif x == n - 1:
        return ((-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1))
    else:
        return ((-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1))


dist = [[-1 for _ in range(len(board[i]))] for i in range(n * 2 - 1)]


def bfs(sx, sy):
    global dist
    for i in range(len(dist)):
        for j in range(len(dist[i])):
            dist[i][j] = -1
    possible = [True for _ in range(n * 2 + 1)]
    appear = [[0 for _ in range(26)] for _ in range(n * 2 + 1)]
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in get_dirs(x, y):
            nx, ny, nd = x + dx, y + dy, dist[x][y] + 1
            if not in_range(nx, ny):
                possible[nd] = False
                break
            if dist[nx][ny] != -1:
                continue
            dist[nx][ny] = nd
            appear[nd][ord(board[nx][ny]) - ord('A')] = 1
            q.append((nx, ny))
        if not possible[dist[x][y] + 1]:
            break

    global ans
    for d in range(1, n):
        if not possible[d]:
            break
        kind = sum(appear[d])
        ans += kind * kind


for i in range(2 * n - 1):
    for j in range(len(board[i])):
        bfs(i, j)
print(ans)