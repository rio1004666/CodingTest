
"""
설계 및 관찰

n*n 격자
꼬리잡기 놀이

3명이상이 한팀
머리사람 - 중간사람들 - 꼬리사람 으로 구성
각 팀마다 정해진 동선이 있다 - 동선은 이어져 있다
각 이동선은 겹치지 않는다

시뮬레이션 + dfs
1. 각 팀은 머리사람 따라서 한칸 이동
2. 각 라운드마다 공이 정해진 선을 따라 던져진다 - 각 방향으로 모든 행 또는 모든 열로 공이 던져진다
3. 공을 맞은 최초로 만나게 되는 사람만이 공을 얻게 되고 점수를 얻게 된다
   1) 점수는 해당 사람이 머리사람을 시작으로 팀내에서 K번째 사람이라면 K의 제곱만큼 점수를 얻게 된다
   2) 아무도 공을 받지 못하는 경우 아무 점수 얻지 못함
   3) 공을 획득한 팀은 머리 사람과 꼬리 사람이 바뀐다

이 문제에서 핵심은 동선과 팀원들을 어떻게 표현할것인가 가 관건이다
그리고 4방향으로 공이 날라오는 과정과
머리와 꼬리가 바뀌는것 그리고 점수를 계산할때 그 맞은 사람의 팀번호와 몇번째 사람인지 알아내는 것일 것이다

그러면 팀의 좌표를 관리하고 또 2차원 격자에 그대로 그 좌표들을 옮겨주도록 하면 좋을거같다
팀의 좌표를 모으기 위해 각팀의 머리를 찾아서 꼬리까지 dfs 탐색으로 모든다 bfs 방식으로 찾아도 된다
각 팀별로 이동동선과 팀원들의 좌표를 묶는다 

"""
def in_range(nx,ny):
    return 0 <= nx < n and 0 <= ny < n


def dfs(pos,cx,cy,cnt,num):
    for i in range(4):
        nx , ny = cx + dx[i] , cy + dy[i]
        if not in_range(nx,ny):continue
        if visited[nx][ny]: continue
        if board[nx][ny] == 0: continue
        if len(teams[cnt]) == 1 and board[nx][ny] == 4:continue
        groups[nx][ny] = num
        if board[nx][ny] == 3:
            tails_idx[cnt] = pos + 1
        visited[nx][ny] = True
        teams[cnt].append((nx,ny)) # 동선전체를 기억한다
        dfs(pos+1,nx,ny,cnt,num)

def make_teams():
    cnt,num = 0,0 # cnt는 좌표를 기억하기 위한 팀번호 group은 2차원 격자에 기억하기 위한 팀번호이다
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                # 머리부터 넣는다
                visited[i][j] = True
                teams[cnt].append((i,j))
                # 팀원들을 찾기 위한 여정이 시작된다
                dfs(0,i,j,cnt,num)
                cnt += 1
                num += 1

def move_team(no):
    # 팀하나가 움직인다
    # 머리부터 움직이므로 가장 끝에 있는 좌표가 머리가 된다
    head = teams[no][-1]
    teams[no] = [head] + teams[no][:-1]
    # 2차원 격자에도 옮겨야겟지
    # 꼬리사람까지는 1,2,3을 표시해주고
    for i in range(tails_idx[no]+1):
        # 맨처음 좌표는 머리이므로 머리사람을 붙인다
        if i == 0:
            hx,hy = teams[no][0]
            board[hx][hy] = 1
        elif 0 < i <= tails_idx[no]-1:
            bx,by = teams[no][i]
            board[bx][by] = 2
        elif i == tails_idx[no]:
            tx,ty = teams[no][i]
            board[tx][ty] = 3
    # 나머지는 동선을 표시해준다
    for i in range(tails_idx[no]+1,len(teams[no])):
        ox,oy = teams[no][i]
        board[ox][oy] = 4


def turn_direction(num):
    # 방향을 전환할 때 꼬리사람부터 다시 거꾸로 머리사람이 꼬리사람이 된다
    renew_team = []
    for i in range(tails_idx[num],-1,-1):
        renew_team.append(teams[num][i])
    for i in range(len(teams[num])-1,tails_idx[num],-1):
        renew_team.append(teams[num][i])
    for i in range(tails_idx[num]+1):
        # 맨처음 좌표는 머리이므로 머리사람을 붙인다
        if i == 0:
            hx,hy = renew_team[0]
            board[hx][hy] = 1
        elif 0 < i <= tails_idx[num]-1:
            bx,by = renew_team[i]
            board[bx][by] = 2
        elif i == tails_idx[num]:
            tx,ty = renew_team[i]
            board[tx][ty] = 3
    # 나머지는 동선을 표시해준다
    for i in range(tails_idx[num]+1,len(renew_team)):
        ox,oy = renew_team[i]
        board[ox][oy] = 4
    teams[num] = renew_team

def throw_balls(round):
    # k라운드에 공이 한방향으로 모두 던져짐
    # 규칙성이 있다
    # 오른쪽으로 가는 공들은 한칸씩 체크하면서 맞는 팀이 있는지 확인한다
    # 그럴려면 한칸씩 탐색하면서 사람인지 먼저 판단하고 그게 어느팀에 속하는지 알아야한다
    # 최초의 사람만이다
    # 어느팀인지 알기 위해 팀소속을 기록해두는 자료구조를 하나 선언하자 2차원 격자로
    # 그리고 그 팀원이 몇번째 사람인지를 찾기위해 좌표를 획득하고 그 좌표로 팀원이 몇번재 존재하는지 찾는다
    round = round % (4*n)
    if round < n:
        for y in range(n):
            if 1 <= board[round][y] <= 3:
                num_of_team = groups[round][y]
                position = teams[num_of_team].index((round,y)) + 1
                team_scores[num_of_team] += (position*position)
                turn_direction(num_of_team)
                break

    elif round < (2*n):
        round -= n
        for x in range(n-1,-1,-1):
            if 1 <= board[x][round] <= 3:
                num_of_team = groups[x][round]
                position = teams[num_of_team].index((x, round)) + 1
                team_scores[num_of_team] += (position*position)
                turn_direction()
                break

    elif round < (3*n):
        round -= (2*n)
        for y in range(n-1,-1,-1):
            if 1 <= board[n-round][y] <= 3:
                num_of_team = groups[n-round][y]
                position = teams[num_of_team].index((n-round,y)) + 1
                team_scores[num_of_team] += (position*position)
                turn_direction()
                break
    elif round < (4*n):
        round -= (3*n)
        for x in range(n):
            if 1 <= board[x][n-round] <= 3:
                num_of_team = groups[x][n-round]
                position = teams[num_of_team].index((x, n-round)) + 1
                team_scores[num_of_team] += (position * position)
                turn_direction()
                break


def simulate():
    # 팀은 한번 꾸리고나면 그다음부터는 방향이 바뀌거나 이동만 하기때문에 더이상 꾸릴 필요가 없다
    make_teams()
    # k라운드동안 시뮬레이션이 진행됩니다

    for round in range(k):
        # 모든 팀원들이 한번씩 이동합니다
        for no in range(m):
            move_team(no)
        # 각 라운드에 해당하는 방향에서 모든 행 또는 모든 열에서 공을 던져서 맞는 팀은 점수를 얻습니다
        throw_balls(round)
    # for i in range(m):
    #     print(teams[i])
    # print(tails_idx)
    # print(team_scores)
    # for i in range(n):
    #     print(*board[i])

# 입력부분

n,m,k = tuple(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(n)]

# 자료구조 선언부분

# 팀원들을 모집하기 위한 자료구조

teams = [[] for _ in range(m)] # m개의 팀원들을 각각 관리하는 자료구조

tails_idx = [0] * m # 꼬리가 몇번째 원소인지만 알면 좌표를 구할 수 있다
visited = [[False] * n for _ in range(n)] # dfs 방문체크시 활용하는 자료구조
groups = [[-1] * n for _ in range(n)]
team_scores = [0] * m
# 공을 던지는 방향과 유사하게 한다
dx = [0,-1,0,1]
dy = [1,0,-1,0]

simulate()
ans = sum(team_scores)
print(ans)
