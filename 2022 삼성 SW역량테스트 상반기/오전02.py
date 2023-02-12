"""

필요한 자료구조 : 그룹핑하기 위해 그룹핑번호를 매기는 변수 , 2차원 격자도 새로 만든다
필요한 알고리즘 : 같은 그룹으로 묶기 위해 dfs 혹은 bfs 탐색을 활용하여 같은 그룹끼리 번호를 매긴다
필요한 관찰 : 아름다움을 계산하기 위해 그룹별 갯수를 관리하는 1차원 배열 구함
           아름다움을 계산하기 위해 모든 격자칸을 돌면서 맞닿아 있는 변의 수가 다르다는 것을 어떻게 아느냐
           -> 4방향으로 보면서 다르면 카운팅 1을 센다 -> 방문했다고 체크한다
           이 과정을 한 번에 체크한다
           1번그룹과 2번그룹이 맞닿아 있는 변의 수를 곱한것이 2를 곱한것이다
           그룹의 갯수와 적힌 숫자가 적힌 값의 배수이므로 이를 2곱한값은
           2번더한것과 마찬가지다
           또 1번과 2번이 계산되고 2번과 1번이 계산되므로
           두번중첩이 되므로 2를 나누어 주어야 원하는 정답이 나온다

           회전 알고리즘
           n은 홀수이고 가운데 십자모양에 속해 있는 칸들은 반시계방향
           그 외 부분들은 시계방향으로 돌린다

"""

n = int(input())

board = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [[False] * n for _ in range(n)]
group = [[0] * n for _ in range(n)] # 같은 그룹끼리 체크하고 관리하기
group_cnt = [0 for _ in range(n*n+1)] # 같은 그룹의 갯수를 관리하기(1번부터 증가하는 배열)
group_n = 0 # 그룹핑하기 위한 변수
ans = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
next_board = [[0] * n for _ in range(n)]

def in_range(x, y):
    return (0 <= x < n and 0 <= y < n)


def dfs(x, y):
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny): continue
        if visited[nx][ny]: continue
        if board[x][y] != board[nx][ny]: continue
        visited[nx][ny] = True
        group[nx][ny] = group_n
        group_cnt[group_n] += 1
        dfs(nx, ny)


def make_group():
    # 그룹핑할때마다 초기화 해준다
    # 그룹의 갯수 초기화
    global group_n
    group_n = 0
    # 방문체크 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
    # 그룹핑 시작 -> dfs 탐색
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_n += 1
                visited[i][j] = True
                group[i][j] = group_n
                group_cnt[group_n] = 1
                dfs(i, j)


# 모듈별 단위별로 테스트 해본다
def in_range(x, y):
    return (0 <= x < n and 0 <= y < n)


def get_art_score():
    art_score = 0
    # art계산은 인접한 면이 다르면 예술성 점수를 구하는 방식으로 가므로 이미 갯수와 그 그룹의 숫자가 무엇인지 알고 있기때문에
    # 계산할 수 있다
    # 모든 칸을 순회하면서 인접한 칸을 확인하면서 다른 그룹이라면 예술성점수를 계산해준다
    for i in range(n):
        for j in range(n):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = i + dx, j + dy
                # 범위를 벗어나면 건너뛴다
                if not in_range(nx, ny): continue
                if board[i][j] != board[nx][ny]:
                    g1, g2 = group[i][j], group[nx][ny]  # 두개의 그룹을 우선 겟한다
                    num1, num2 = board[i][j], board[nx][ny]
                    cnt1, cnt2 = group_cnt[g1], group_cnt[g2]
                    art_score += (cnt1 + cnt2) * num1 * num2
    return art_score


def get_score():
    make_group()
    # 계산시에 양옆에서 중복을 계산하기 때문에 2를 나누어 줍니다 ( 문제 정확하게 읽기 )
    return get_art_score() // 2


def rotate_square(sx,sy,sn):
    # 보드를 돌리려면 0,0이세부터 돌려야한다는 전제가 깔려 있다
    for cx in range(sx, sx + sn):
        for cy in range(sy, sy + sn):
            ox, oy = cx - sx , cy - sy # 항상 0,0 으로 시작해서 변위를 구한다 즉 문제예시에서 0,0은 0,1로 각각 0과 1이 더해지는 이 변위를 구하는 것이다
            rx, ry = oy , sn - ox - 1
            next_board[sx+rx][sy+ry] = board[cx][cy] # 현재의 칸을 돌렸을 경우 다음 보드판에 넣는다



def rotate():

    # 십자가 모양부터 돌린다
    # 십자가 모양의 가운데 있는 칸들은 반시계방향으로 돈다 이때 규칙은 x좌표와 y좌표가 자리만 바뀌면 된다
    for i in range(n):
        for j in range(n):
            # 열에 있는 숫자들은 x좌표와 y좌표만 바꾸어주면된다
            if j == n//2:
                next_board[j][i] = board[i][j]
            # 문제는 행의 숫자들을 반시계방향으로 돌렸을 경우 문제이다
            # 반시계방향으로 움직이는 공식을 적용한다
            elif i == n//2:
                next_board[n-j-1][i] = board[i][j]



    # 4개의 정사각형 영역과 한개의 십자가 모양 영역이 돌아가므로
    # 4개의 정사각형 영역은 돌아가는 위치만 다르고 회전하는 것은 똑같이 동작하므로 하나의 함수를 만들어서 돌린다
    rotate_square(0,0,n//2)
    rotate_square(0,n//2+1,n//2)
    rotate_square(n//2+1,0,n//2)
    rotate_square(n//2+1,n//2+1,n//2)

    for i in range(n):
        for j in range(n):
            board[i][j] = next_board[i][j]
# 1단계씩 디버깅한다 시뮬레이션 문제는
for _ in range(4):
    ans += get_score()
    rotate()
print(ans)