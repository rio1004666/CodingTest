"""

2차원 격자 배열
숫자 아무거나 써저잇다
매번 인접한 곳으로 이동
단 더 큰 숫자로만 갈 수 있다
중복방문 안됨
한번은 기회를 주는데
찬스를 쓰면 더 작은 숫자가 있는곳으로 이동가능
내가 갈 수 있는 가장 긴 경로는 얼마인가?
n,m <= 5
bfs 나 dfs 로는 안됨 - 중복되면 안되기때문애
최장거리구하기때문에 또 bfs 나 다익스트라는 안된다
완전탐색뿐이다
최장경로는 NP-Complete라는 3^이라는 시간복잡도를 가질 수 밖에ㅐ없다 보통

백트래킹 함수를 구현하도록 한다

def backtracking(x,y,length,chance,visited)
x,y위치에 어떻게 잘 도착해서 length개만큼 지났고
chance개를 썻다 그리고 중복되지 않아야하므로 visited로 중복을 피할 수 잇따

이렇게 방문체크를 하는 이유는 chance 때문이다
더 낮은칸으로 갈 수 있기때문에 또 높은칸으로 중복칸으로 갈 수 있다

1.보편적인 이동
x,y에서 출발해서 인접한 4방향 칸에서 더 큰 숫자로 이동
숫자도 더 크고 방문한적이 없다면 찬스를 사용하지 않고 이동 가능하므로
이 칸으로 방문하여 이 칸에 대해 재귀적으로 또 인접한 4칸에 방문
backtracking(nx,ny,lenght+1,False,visited)
2.찬스를 쓰는 경우 ( if chance == False )
인접한 4칸 중 더 작은수와 방문하지 않은 수로 재귀호출을 해준다
backtracking(nx,ny,length+1,True,visited)

이론적으로는 3^25 시간복잡도를 가진다
현실적으로는 아니다
매순간 3군데를 갈 수가 없다 선택지가 줄어들 수 밖에 없다
알고리즘 시간복잡도 계산 방법이
emprical 한것이 잇다 이것은 넣어보고 계산해보는것인데
예상하기 어려우므로 그렇게 좋은 문제는 아니다...?

"""



import sys
si = sys.stdin.readline
N = 5
a = [si().strip() for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
ans = 0
def BT(x,y,length, chance, visit):
    global N,ans
    ans = max(ans,length)
    visit[x][y] = 1
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx,ny, = x + dx , y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if visit[nx][ny] == 1:
            continue
        if a[x][y] < a[nx][ny]:
            BT(nx,ny,length+1,chance,visit)
        elif a[x][y] > a[nx][ny] and not chance:
            BT(nx,ny,length+1,True,visit)
    visit[x][y] = 0
for i in range(N):
    for j in range(N):
        BT(i,j,1,False,visit)
print(ans)