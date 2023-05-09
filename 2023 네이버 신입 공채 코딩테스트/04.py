"""
1. 문제이해

   철수와 영희가 싸움을 한다
    N X M 행렬에서
    철수는
    k개의 연속된 블럭조각을 선택 어떤 형태든 상관없음 (서로 연결된 블럭조각 선택)
    영희는 철수가 정한 k개의 블록조각을 제외한 k개의 연속된 조각을 선택함

    어떤 최선을 다함?
    영희가 고른 블록조각들의 숫자들이 써져 있는데 합이 가장 높은 점수를 얻는 블록조각을 선택함
    철수가 선택한 블록조각에 대해서 영희가 얻을 수 있는 점수의 최소와 최대를 구하면 된다

    범위 : N,M <= 30 / K <= 6

2. 관찰

   이슈 1.

   인접한 K개의 격자로 가능한 모든 경우의 수 (중복 없이)

   전체 격자에서 임의의 하나 위치를 선정 -> 인접한 위치를 후보에 넣는다 -> 이 포인트들을 붙인다 -> 또 인접한 포인트들을 추가한다
   이렇게 인접한 칸들을 붙여 나간다 => k개
   *************** 중요한건 중복을 제거 => 시간초과 면할 수 있다
   똑같은 모양의 격자를 여러번 센다면 탐색공간이 너무 커진다

   중복을 제거해서 K개의 인접한 격자들을 모두 찾음 =>  BFS 처럼 인접한 k개 조작들을 찾고 , DFS로 중복되는 블럭들을 제거한다


   이슈 2.
   위에서 선택한 선택지들에서 불가능한 선택지 제거 한다 ( 철수가 선택한 블럭에서 그와 겹치지 않는 블럭들을 선택해야함 )

   불가능한 선택지 제거 -> 철수가 선택해도 영희가 여전히 선택가능

   하나의 선택지 선택하고 완전하게 겹치지 않으면 된다
   그러면 가능하다라고 판단한다

   이슈 3.

   영희가 얻을 수 있는 최소 최대 점수 계산 로직

   구현의 기본
   2차원격자의 셀들의 좌표를 탐색하는 것이 기본
   좌표를 탐색할 때는 보통 BFS 느낌 사용
   중복을 제거하는 블럭들을 찾기 위해 DFS 재귀 탐색으로 경우의 수를 필터링

   여튼 빡구현류의 문제......

"""

import sys
import copy

si = sys.stdin.readline
n, m, k = map(int, si().split())
a = [list(map(int, si().split())) for _ in range(n)]
pieces = []
counting = [[0 for _ in range(m)] for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
path = []
cells = set() # 한 셀의 선택의 중복을 피하기 위한 set 사용
mems = set() # 한 블럭의 선택의 중복을 피하기 위한 set 사용

# k개의 조각들을 정렬한 상태로 비교하면서 중복을 제거할 수 있다

def encode():
    return tuple(sorted(path)) # 한 블럭의 좌표들을 정렬함으로써 오름차순의 좌표들로 통일하여 중복여부를 결정할 수 있다

# 한 포인트를 선택하고 인접한 포인트들을 체크표시 해줌
def add(x, y):

    path.append((x, y))
    visit[x][y] = True

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        counting[nx][ny] += 1
        if counting[nx][ny] == 1: # 1번 담은 셀은 더이상 담지 않도록 유도한다 즉 2번이상 담는것 (중복) 은 제외한다
            cells.add((nx, ny)) # 중복된 셀 선택을 피하기 위한 체크 (핵심)

# 선택을 철회함
def pop(x, y):
    path.pop() # 블럭에서 셀을 제거합니다
    visit[x][y] = False # 방문표시를 해제한다
    # 인접한 4개의 셀을 체크해봅니다
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        # 범위 벗어난것은 선택하지 않습니다
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        counting[nx][ny] -= 1
        if counting[nx][ny] == 0:
            cells.remove((nx, ny))

# k개의 인접한 조각들을 중복없이 찾기 위한 dfs 재귀 탐색
def func(cnt, score):
    # 중복을 제거하기 위한 종료조건
    if encode() in mems:
        return
    mems.add(encode())
    if cnt == k:
        # 블럭을 완성하고 바구니에 담는다 (점수,조각들모음) -> 추후에 점수를 기준으로 정렬할것임
        pieces.append((score, set(path)))
    else:
        _cells = copy.deepcopy(cells) # 원본과 분리하여 복사하는 deepcopy
        for x, y in _cells:
            if visit[x][y]:
                continue
            add(x, y)
            func(cnt + 1, score + a[x][y]) # 점수들까지 계산한다
            pop(x, y)

# 모든 칸을 돌면서 인접한 셀들을 붙이며 중복이 없는 블록들을 쓸어담는 기능을 구현한다

for i in range(n):
    for j in range(m):
        add(i, j) # 일단 해당 셀부터 담고 인접한 후보 셀들을 넣어본다
        func(1, a[i][j]) # 1개부터 시작해서 K개가 될때까지 넣어본다 , 점수도 같이 계산한다
        pop(i, j)

pieces.sort(reverse=True) # 점수별로 정렬합니다.

# Filtering unavailable pieces

valid_pieces = []

# 16만개
for i in range(len(pieces)):

    flag = False
    # 16만개 => 16만 x 16만개면 시초가 아닐까? 커지면 커질수록 안겹치는 블럭들이 금방 금방 나옵니다
    # 격자의 크기가 크면 클수록 안겹치는 블럭들이 금방 금방 나온다
    for j in range(len(pieces)):
        if pieces[i][1].intersection(pieces[j][1]):
            continue
        flag = True
        break
    if flag:
        valid_pieces.append(pieces[i])

pieces = valid_pieces # 철수/영희 둘다 선택이 가능한 조각들만 모아놓은게 valid_pieces

# 내림차순으로 블럭들을 정렬한다면 가장 높은 점수일때 이것이 영희가 얻을 수 있는 가장 높은 블럭이되고
# 최고점수와 겹치지 않는 다른 블럭들을 고른다면 자연스럽게 영희는 최고점수를 선택하면 된다

# maximal valid piece
max_point = valid_pieces[0][0]  # 최대점수는 0번지의 블럭 점수를 고르면 된다

# 최소점수가 문제인데 -> 철수가 어떻게 플레이해야 영희의 점수를 견제할 수 있을까 생각해보면
# 철수가 일단 가능한 조각들 전부 하나씩 다 선택해본다
# 영희는 남은 조각들 중에 겹치지 않는 블럭들을 선택해보면서 겹치지 않는 첫 조각이 최소가 된다
# 철수가 모든 블럭을 선택한것에 대한 영희의 선택인 완전탐색을 해본다
# 나는 그냥 최소점수도 영희가 최소점수가 되는 블럭을 선택하고 겹치지 않는 블럭을 선택하면 된다고 생각했는데...
# 아 영희는 항상 최선을 다해 가장 높은 점수를 얻는것을 목표로 하므로
# 철수가 선택한 블록을 제외한 가장 높은점수 중 최소값을 구하면 될것이므로
# 철수가 한번씩 다 선택해보는 완전탐색을 사용한다

# minimal valid piece : 철수가 선택 후 영희가 최선을 다해 높은점수를 얻을 수 있는 블럭들 중 최고의 점수 중 최소값

min_point = sys.maxsize

# 이거또한 최대점수를 갖는 블럭과 겹칠 수 잇는 조각 자체가 1000개밖에 안되기 때문에 2중 for문이 풀로 돌아가진 않을것이다

for pA in pieces: # 철수가 하나 선택한다
    point = sys.maxsize
    for pB in pieces: # 영희가 하나 선택한다
        if pA[1].intersection(pB[1]): # 안겹치는 블럭을 선택했을 때 그것을 선택한다
            continue
        point = pB[0]
        break

    min_point = min(min_point, point)

print(min_point, max_point)