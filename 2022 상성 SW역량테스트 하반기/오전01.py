"""
인기게임 싸움땅
진행방식
n*n 격자
격자에는 무기가 있을 수 있다
초기에 무기들이 없는 빈 격자에 플레이어들이 위치
각 플레이어는 초기 능력치 가진다 모두 다르다
1-1 첫번째 플레이어부터 본인이 향하고 있는 방향으로 한칸이동 격자 벗어나면 정반대 방향 전환 하여 1이동
1-2 이동한 방향에 플레이어가 없다면 해당칸에 총이 있는지 확인 총이 있는 경우 총을 획득
    이미 총을 가지고 있는 경우 놓여 있는 총들과 플레이어가 가지고 있는 총 가운데 공격력이 더쎈총 획득
    나머지 총들은 해당 격자에 둔다
1-3 이동한 칸에 플레이어가 있는 경우 두 플레이어가 싸우게 된다
    초기능력치와 들고 있는 공격력의 합을 비교해 더 큰 플레이어가 이김
    수치가 같으면 초기 능력치가 높은 플레이어가 승리
    이긴 플레이어는 각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이만큼 포인트 획득
1-4 진 플레이어는 본인이 가지고 있는 총을 해당 격자에 내려 놓고,
    해당 플레이어가 원래 가지고 있던 방향대로 한칸이동한다
    만약 이동하려는 칸에 다른 플레이어가 있거거나 격자 범위 밖인 경우
    오른쪽으로 90도 회전하여 빈칸이 보이는 순간 이동
    만약 해당칸에 총이 있다면 가장 공격력이 높은 총을 획득하고 나머지 총들은 해당 격자에 내려놓는다
1-5 이긴 플레이어는 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력 높은 총 획득
    나머지 총들은 해당 격자에 내려 놓는다
"""
n,m,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
players = []
points = [0] * m
is_player = [[0] * n for _ in range(n)] # 플에이어 번호가 매겨진 격자
guns = [[[] for _ in range(n)] for _ in range(n)] # 각 칸에 총들을 담음
dx = [-1,0,1,0]
dy = [0,1,0,-1]

pnum = 1
for _ in range(m):
    x,y,d,s = map(int, input().split())
    x -= 1
    y -= 1
    players.append([x,y,d,s,0]) # 좌표와 방향 초기능력 총가지고있는지 여부 저장
    is_player[x][y] = pnum # 플레이어가 있는지 체크 번호를 넣는다
    pnum += 1
for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            guns[i][j].append(board[i][j])

def in_range(nx,ny):

    return 0 <= nx < n and 0 <= ny < n

def player_move(cx,cy,cd):
    nx, ny = cx + dx[cd], cy + dy[cd]
    if not in_range(nx, ny):
        if cd < 2:
            cd = cd + 2
        elif cd >= 2:
            cd = cd - 2
        nx, ny = cx + dx[cd], cy + dy[cd]
    return nx,ny,cd

for _ in range(k):
    for i in range(len(players)):
        cx,cy,cd = players[i][0],players[i][1],players[i][2]
        nx,ny,cd = player_move(cx,cy,cd) # 플레이어가 한칸 이동함
        players[i][2] = cd
        # 해당하는칸에 플레이어가 없다면
        if not is_player[nx][ny]:
            # 지금 칸을 제거하고
            is_player[cx][cy] = 0
            # 이동하는 칸에 이동한다
            is_player[nx][ny] = i + 1
            players[i][0],players[i][1] = nx , ny
            if players[i][4] > 0:
                if len(guns[nx][ny]) > 0:
                    guns[nx][ny].append(players[i][4])
                    guns[nx][ny].sort()
                    players[i][4] = guns[nx][ny][-1]
                    guns[nx][ny].pop()
            else:
                if len(guns[nx][ny]) > 0:
                    guns[nx][ny].sort()
                    players[i][4] = guns[nx][ny][-1]
                    guns[nx][ny].pop()

            # print(players[i][3],players[i][4])
        # 이동할 칸에 플레이어가 있다면
        else:
            """
            누가 이겼고 졌는지 판단하는 로직 
            """
            p1 = is_player[nx][ny]
            p2 = is_player[cx][cy]
            p1s,p2s = players[p1-1][3],players[p2-1][3]
            p1g,p2g = players[p1-1][4],players[p2-1][4]
            p1t, p2t = p1s+p1g, p2s+p2g # 각 플레이어의 능력치와 총공격력을 합한다
            winner,loser = 0,0
            if p1t > p2t:
                winner = p1
                loser = p2
            elif p1t < p2t:
                winner = p2
                loser = p1
            elif p1t == p2t:
                if p1s > p2s:
                    winner = p1
                    loser = p2
                else:
                    winner = p2
                    loser = p1

            """
            진 플레이어의 행동강력
            """
            is_player[cx][cy] = 0  # 그 전칸의 플레이어는 지우고
            if players[loser-1][4] > 0:
                guns[nx][ny].append(players[loser-1][4]) # 가지고 있는 총을 내려 놓는다
                players[loser-1][4] = 0
            ld = players[loser - 1][2]
            nnx, nny = nx, ny
            for j in range(4):
                nnx = nx + dx[ld]
                nny = ny + dy[ld]
                if not in_range(nnx, nny) or is_player[nnx][nny]:
                    ld = (ld + 1) % 4
                else:
                    break
            players[loser - 1][2] = ld
            if players[loser - 1][4] > 0:
                if len(guns[nnx][nny]) > 0:
                    guns[nnx][nny].append(players[loser - 1][4])
                    guns[nnx][nny].sort()
                    players[loser - 1][4] = guns[nnx][nny][-1]
                    guns[nnx][nny].pop()
            else:
                if len(guns[nnx][nny]) > 0:
                    guns[nnx][nny].sort()
                    players[loser - 1][4] = guns[nnx][nny][-1]
                    guns[nnx][nny].pop()
            is_player[nnx][nny] = loser
            players[loser - 1][0], players[loser - 1][1] = nnx, nny
            """
            이긴 플레이어의 행동강령
            """
            points[winner-1] += abs(p1t-p2t)
            if players[winner-1][4] > 0:
                if len(guns[nx][ny]) > 0:
                    guns[nx][ny].append(players[winner-1][4])
                    guns[nx][ny].sort()
                    players[winner-1][4] = guns[nx][ny][-1]
                    guns[nx][ny].pop()
            else:
                if len(guns[nx][ny]) > 0:
                    guns[nx][ny].sort()
                    players[winner-1][4] = guns[nx][ny][-1]
                    guns[nx][ny].pop()
            is_player[nx][ny] = winner
            players[winner-1][0] , players[winner-1][1] = nx,ny

print(*points)