"""

0 <= x <= 5

n x n 크기의 격자 정보 주어짐

0 = 빈공간
1 = 사무실 구역
2 = 에어컨 ( 좌 방향 )
3 = 에어컨 ( 상 방향 )
4 = 에어컨 ( 우 방향 )
5 = 에어컨 ( 아래 방향 )

예를 들어서 사무실을 시어ㅜㄴ하게 하는 과정
4단계를 거침 => 시뮬레이션

알고리즘 : dfs로 시원함을 진행

데이터 관리 : 상하좌우 벽을 표시하려면 2차원 격자 각 칸에 상하좌우 벽의 여부를 판단하는 4길이의 1차원 배열 필요

"""

DIR_NUM = 4
OFFICE = 1

# 변수 선언 및 입력:
n, m, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 각 위치의 시원함의 정도를 관리합니다.
# 처음에는 전부 0입니다.
coolness = [
    [0] * n
    for _ in range(n)
]

# 시원함을 mix할 때
# 동시에 일어나는 처리를
# 편하게 하기 위해 사용될 배열입니다.
temp = [
    [0] * n
    for _ in range(n)
]

# dx, dy 순서를 상좌우하로 설정합니다.
# 입력으로 주어지는 숫자에 맞추며,
# 4에서 현재 방향을 뺏을 때, 반대 방향이 나오도록 설정한 것입니다.
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

# 현재 위치 (x, y)에서 해당 방향으로
# 이동한다 했을 때 벽이 있는지를 나타냅니다.
block = [
    [
        [False] * DIR_NUM
        for _ in range(n)
    ]
    for _ in range(n)
]

# 시원함을 전파할 시
# 한 에어컨에 대해
# 겹쳐서 퍼지는 경우를 막기 위해
# visited 배열을 사용합니다.
visited = [
    [False] * n
    for _ in range(n)
]

# 현재까지 흐른 시간(분)을 나타냅니다.
elapsed_time = 0


# (x, y)가 격자 내에 있는지를 판단합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# (dx, dy) 값으로부터
# move_dir값을 추출해냅니다.
def rev_dir(x_diff, y_diff):
    for i, (dx, dy) in enumerate(zip(dxs, dys)):
        if dx == x_diff and dy == y_diff:
            return i

    return -1


# (x, y)위치에서 move_dir 방향으로
# power 만큼의 시원함을 만들어줍니다.
# 이는 그 다음 칸에게도 영향을 끼칩니다.
def spread(x, y, move_dir, power):
    # power가 0이 되면 전파를 멈춥니다.
    if power == 0:
        return

    # 방문 체크를 하고, 해당 위치에 power를 더해줍니다.
    visited[x][y] = True
    coolness[x][y] += power

    # Case 1. 직진하여 전파되는 경우입니다.
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if in_range(nx, ny) and not visited[nx][ny] and not block[x][y][move_dir]:
        spread(nx, ny, move_dir, power - 1)

    # Case 2. 대각선 방향으로 전파되는 경우입니다.
    if dxs[move_dir] == 0:
        for nx in [x + 1, x - 1]:
            ny = y + dys[move_dir]
            # 꺾여 들어가는 곳에 전부 벽이 없는 경우에만 전파가 가능합니다.
            if in_range(nx, ny) and not visited[nx][ny] and \
                    not block[x][y][rev_dir(nx - x, 0)] and not block[nx][y][move_dir]:
                spread(nx, ny, move_dir, power - 1)

    else:
        for ny in [y + 1, y - 1]:
            nx = x + dxs[move_dir]
            # 꺾여 들어가는 곳에 전부 벽이 없는 경우에만 전파가 가능합니다.
            if in_range(nx, ny) and not visited[nx][ny] and \
                    not block[x][y][rev_dir(0, ny - y)] and not block[x][ny][move_dir]:
                spread(nx, ny, move_dir, power - 1)


def clear_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


# 에어컨에서 시원함을 발산합니다.
def blow():
    # 각 에어컨에 대해
    # 시원함을 발산합니다.
    for x in range(n):
        for y in range(n):
            # 에어컨에 대해
            # 해당 방향으로 시원함을
            # 만들어줍니다.
            if grid[x][y] >= 2:
                move_dir = (3 - grid[x][y]) if grid[x][y] <= 3 \
                    else (grid[x][y] - 2)

                nx, ny = x + dxs[move_dir], y + dys[move_dir]

                # 전파 전에 visited 값을 초기화해줍니다.
                clear_visited()
                # 세기 5에서 시작하여 계속 전파합니다.
                spread(nx, ny, move_dir, 5)
                for i in range(n):
                    print(*coolness[i])
                print('---------------------------------------------------------')
for _ in range(m):
    bx, by, bdir = tuple(map(int, input().split()))
    bx -= 1
    by -= 1

    # 현재 위치 (bx, by)에서
    # bdir 방향으로 나아가려고 했을 때
    # 벽이 있음을 표시해줍니다.
    block[bx][by][bdir] = True

    nx, ny = bx + dxs[bdir], by + dys[bdir]
    # 격자를 벗어나지 않는 칸과 벽을 사이에 두고 있다면,
    # 해당 칸에서 반대 방향(3-bdir)으로 진입하려고 할 때도
    # 벽이 있음을 표시해줍니다.
    if in_range(nx, ny):
        block[nx][ny][3 - bdir] = True

def mix_coolness():
    pass

def boundary_minus():
    pass

def simulate():
    blow()
    # 디버깅 작업


simulate()


