"""

시뮬레이션(단계) BFS(최단거리)
n*n 격자
m명
베이스 캠프
편의점
1. 가고싶은 편의점 방향으로 1칸 움직임
   최단거리로 움직이는 방법이 여러가지 있다면 우선순위의 방향으로 움직임
   즉 한번 움직일때 똑같이 최단거리가 2로 판정이 됫을 경우 어느방향으로 갈지 정하는 우선순위 표가 있다
   근데..흠 여기서 중요한가...? 어차피 한칸에 여러사람 잇을 수 있고
   최단거리가 같아도 최단시간내에 가는것 자체는 같다......
   방향은 크게 상관없을듯??
   아니다 여튼 1분마다 한칸씩 움직이는 행위를 하기때문에..
   또 지나갈수없는 곳이 생기기에 매분마다 판단해줘야해서 방향을 정하기는 해야한다
   매분마다
   각 방향별로 출발햇을 경우 최단거리를 구하고
   방향과 거리를 같이 저장해서
   매 분마다 판정하여서 어디로 한칸 이동할지 정한다
   그리고 m분 즉 목표로하는 시가전까지 편의점에서 가장 가까운 베이스 캠프에 들린다
   즉 첫번째로이동할때는 무조건 베이스 캠프로 이동하는것이 유리하다


그러면 어떻게 설계를 해야할까?

1번사람은 맨처음에 1번편의점에서 가장가짜운 베이스캠프를 가야하므로
1분에 1번 편의점에서 bfs탐색을 하여 가장 가까운 베이스 캠프 리스트를 받아온다 행과열을 기억한다 칸수와
그후 정렬하여 가장 앞에 잇는 베이스캠프의 위치를 가져와서 방문표시를 한다 2차원 격자에

2분에는 똑같이 2번편의점에서 가장 가까운 베이스 캠프를 찾아 방문시키고 2번사람의 위치를 기억한다
2차원 격자는 한 칸에 여러 사람이 있을 수 있으므로 칸마다 리스트를 만들어서
관리하도록 한다

그리고 나머지 사람들은 현재칸에서 각 방향별로 편의점까지 도착하는 최단거리를 bfs로 구하여
그 방향으로 한칸 이동하도록 한다


모든 사람이 편의점에 도착하면 그 시간을 리턴하게 하면 되고
모든 사람이 편의점에 도착했는지 알기 위해 판단하는 함수를 생성한다
어차피 각 사람들을 이동해야하는지 안해야하는지 체크를 하고 이미 도착했다면 패스하기때문에
이때 카운팅을 하여 다 도착했는지 판단하고 리턴하면 된다

기본적으로 사람들은 다 격자 밖으로 있기때문에

맨 처음은 베이스캠프로 가는 방법을 선택한다

2차원 격자를 1칸마다 리스트로 만들어서 베이스캠프에 도착하는 순간
1번사람이 한번왓엇다는 표시를 위치로 기록해준다
그 후 그 위치기록이 있다면 피하고 돌아서 간다
베이스캠프든 편의점이든 마찬가지이다

2차원격자에는 베이스캠프가 표시되어있고
편의점의 위치는 좌표로 던져주기때문에

1칸씩 리스트로 넣어주는 2차원 격자

편의점 좌표에서 출발하여 탐색하는  bfs 함수를 생성
베이스 캠프에서 출발하여 탐색하는  bfs 함수를 생성

그리고 각 편의점에 사람이 도착했다는 표시를 해주는 배열 생성

그런데 가는 도중에 베이스캠프를 밝고 가는 경우애는?
그러니까 베이스캠프에서 편의점으로 가는도중에 베이스캠프를 밝고가는것이 최단거리라면
베이스캠프를 밟고가도되나? 또 그런경우에ㅐ 베이스캠프를 또 재방문할 수 없나?

그러면 가장 가까이에 있는 베이스캠프와 편의점 사이에는 다른 베이스 캠프가 없다는 것을 전제로 한다?
잇다고 하더라도 이미 한번 들어갓다온적있는 베이스캠프이기때문에?

그리고 매분마다 최단거리가 달라질 수 있다는 것은
내가 최단거리라고 생각했지만
다른 사람이 베이스캠프를 들어옴으로써 내가 우회해야할 경우가 발생하면 최단거리가 아니게 되므로
매분마다 최단거리 계산을 해야한다
흠..
주인사람이 편의점으로 돌어오기전에는 다른 사람이 지나갈수있다....? 라는게 되기때문에
무조건 움직여서 듪어와야함

t분안에 m명이 모두 다 도착한다고 보장하였으므로 무조건 각 t분에 t번 사람은 베이스 캠프로 이동하고
나머지 이동할 수 있는 사람들은 이동하도록 한다
최대 30명이 움직인다

"""
import sys
from collections import deque

n,m = tuple(map(int,input().split()))

board = [list(map(int, input().split())) for _ in range(n)]

convenients = []

# m개의 편의점의 위치를 입력받는다

for _ in range(m):
    x,y = tuple(map(int, input().split()))
    convenients.append((x-1,y-1)) # 좌표를 저장해준다
    board[x-1][y-1] = 2 # 편의점임을 표시해준다

# 자료구조 형성
"""
리스트로 이루어진 2차원 격자 생성 
여러사람이 한칸에 있을 수 있음 
베이스캠프 및 편의점 사람의 위치가 겹쳐지므로 이 자료구조를 선택함 

"""
check = [[[] for _ in range(n)] for _ in range(n)]
is_basecamp = [False] * m
people = [(-1,-1)] * m # 사람들의 위치는 격자밖이므로 -1,-1로 초기화
arrived = [False] * m
ans = 0
dx = [-1,0,0,1] # 상좌우하 우선순위로 맞추기 위한 테크닉
dy = [0,-1,1,0]
"""
이제 t분마다 시뮬레이션을 돌린 베이스 코딩을 시작 
"""


def in_range(nx,ny):
    return 0 <= nx < n and 0 <= ny < n


def move_basecamp(num):
    # 이 함수에서 3번을 수행한다
    # 편의점에서 가장 가까운 베이스캠프를 찾는다
    # 여기서 bfs 탐색을 사용한다
    visited = [[0]*n for _ in range(n)]
    sx,sy = convenients[num]
    visited[sx][sy] = 1
    q = deque([(0,sx,sy)]) # 거리,행,열 순으로 정렬하기 위해 이렇게 셋팅
    base_camps = []
    while q:
        dist,cx,cy = q.popleft()
        if board[cx][cy] == 1:
            base_camps.append((dist,cx,cy))
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not in_range(nx,ny):continue
            if visited[nx][ny]:continue
            # 한번이라도 베이스캠프나 편의점을 방문했던적이 있다면 지나갈 수 없으므로 최단거리로 선택될 수 없다
            if len(check[nx][ny]) > 0 : continue
            visited[nx][ny] = 1
            q.append((dist+1,nx,ny))
    # 갈 수 있는 가장 작은 베이스 캠프들의 정보를 모아서 정렬후 가장 앞에 있는 원소를 반환한다
    # 정렬 후
    base_camps.sort()
    # 그 위치를 반환하고

    _ , mx, my = base_camps[0]
    # 2차원격자 리스트에 넣어주면 된다
    check[mx][my].append((mx,my,num)) # 사람읩 번호까지 기억해주어야 나중에 겹쳐도 이동할 수 있다 탐색해서
    people[num] = (mx,my) # 사람들의 위치를 저장하는 곳이 필요하다
    is_basecamp[num] = True # 베이스캠프로 이미 한번 이동했다면 그다음부터 일반적인 이동으로 진행된다
    return




def find_my_convenient(d,num):
    visited = [[0] * n for _ in range(n)]
    sx, sy = people[num]
    # 해당방향으로 이동했을 경우 최단거리를 구해볼것이다
    ssx , ssy = sx + dx[d] , sy + dy[d]
    if not in_range(ssx,ssy):
        return sys.maxsize
    visited[ssx][ssy] = 1
    q = deque([(1, ssx, ssy)])  # 거리,행,열 순으로 정렬하기 위해 이렇게 셋팅

    while q:
        dist, cx, cy = q.popleft()
        # 자신의 편의점을 찾았을 경우 최단거리 구한다
        if cx == convenients[num][0] and cy == convenients[num][1]:
            return dist
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not in_range(nx, ny): continue
            if visited[nx][ny]: continue
            # 한번이라도 베이스캠프나 편의점을 방문했던적이 있다면 지나갈 수 없으므로 최단거리로 선택될 수 없다
            if len(check[nx][ny]) > 0: continue
            visited[nx][ny] = 1
            q.append((dist + 1, nx, ny))
    return sys.maxsize


def move_blank(num):
    # 베이스캠프를 떠나서 실질적으로 편의점으로 향해서 한 칸 이동하기 위해 각 방향으로 출발했을 경우
    # 최단거리를 구하고 그래도 다양한 방법이 있다면 방향의 우선순위를 이용하여
    # 한칸이동하는 과정을 그리기
    info = []
    for d in range(4):
        dist = find_my_convenient(d,num)
        info.append((dist,d))
    info.sort()
    dist,d = info[0]
    px,py = people[num]
    # 빈칸을 지났을 경우에만 자취를 지운다
    # 그런데 궁금한건 니가가는 도중에 베이스캠프를 지나갈수도 있는거자나?
    # 그럴때는 자취를 남겨? 즉 절대 지나갌 수 없는 길로 만들어??
    if board[px][py] == 0:
        check[px][py].remove((px,py,num))
    nx,ny = px + dx[d] , py + dy[d]
    check[nx][ny].append((nx,ny,num))
    people[num] = (nx,ny)
    cx,cy = convenients[num]
    # 이동하고 난 후 도착했다면 체크하고 더 이상 이동하지 않음
    if nx == cx and ny == cy:
        arrived[num] = True




def move(num):
    global ans
    # 아직 베이스캠프로 이동하지 못했다면
    if not is_basecamp[num]:
        # 각 사람들의 번호에 해당하는 분시간이 되면 베이스캠프로 이동하는 모션을 취한다
        move_basecamp(num)
    # 이미 베이스캠프로 이동했다면
    else:
        # 사람들 번호 이후의 분시간들에 대해서는 일반적인 4방향 이동을 실시한다
        move_blank(num)

def is_over():
    for i in range(m):
        if not arrived[i]:
            return False
    return True
def simulate():
    global ans
    # 1분씩 일어날 일들을 여기에서 구현
    # 모두 편의점에 도착하는 시간 즉 정답시간이 현재 m번째 사람이라면
    # 베이스캠프에 들어가는 행위를 해야한다
    # 우선 한번의 시뮬레이션을 돌릴 함수들을 정의한다
    # 그 후 반복한다
    # 현재사람이 베이스 캠프로 이동했고 나머지 사람들은 한칸씩 움직이는 과정을 그려나가야함
    # 0번사람이 움직이면 그 이후 사람들은 아직 움직이지 않았으므로 0번사람만 움직인다
    # 1번사람이 움직이면 앞에 0번사람은 이미 베이스캠프로 가든 한번은 이동하였으므로 이동할 수 ㅣㅇㅆ다
    # 2번사람이 움직인다고 하면 0번,1번사람이 움직일 수 있다
    # 그 이후는 0번 1번 2번 사람 모두 움직일 수 있다
    # 물론 이미 편의점에 도착했다면 움직이지 않겠지만.
    # for i in range(3):
    #     move(i)
    # 자기 편의점에 도착하지 않았을경우에만 이동할것이다
    while True:
        # m분 이하라면 뒤에 있는 사람들은 이동하지 않으므로 앞전에 움직였던 사람들만 이동합니다

        for num in range(min(m,ans+1)):
            if num < m and arrived[num]: continue
            move(num)
        # 여기까지 0번 사람이 움직이는것을 관찰해보자
        # 모두 편의점에 도착했는지 판단하는 함수
        if is_over():
            print(ans+1)
            break
        ans += 1
    return


simulate()












