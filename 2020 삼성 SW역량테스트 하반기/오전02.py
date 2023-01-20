"""
원자 충돌 실험
m개의 원자는 각각 질량,방향,속력,초기위치 가지고 있다
방향은 상하좌우/대각선
모든 행,열은 각각 끝과 끝이 연결

실험 진행
1. 모든 원자는 1초가 지날 때마다 자신의 방향으로 자신의 속력만큼 이동
2. 이동이 모두 끝난 뒤에 하나의 카네 2개 이상의 원자가 있는 경우에는 다음과 같은 합성이 일어남
   a. 같은 칸에 있는 원자들은 각각의 질량과 속력을 모두 합한 하나의 원자로 합쳐짐
   b. 이후 합쳐진 원자는 4개의 원자로 나눠짐
   c. 나누어진 원자들은 모두 해당칸에 위치하고 질량과 속력, 방향은 다음 기준을 따라 결정됨
      - 질량은 합쳐진 원자의 질량에 5를 나눈 값이다
      - 속력은 합쳐진 원자의 속력에 합쳐진 원자의 개수를 나눈 값이다
      - 방향은 합쳐지는 원자의 방향이 모두 상하좌우 중 하나이거나 대각선 중에 하나이면,
        각각 상하좌우의 방향을 가지며 그렇지 않다면 대각선 네 방향의 값을 가진다
      - 편의상 나눗셈과정에서 생기는 소숫점 아래의 수는 버린다
  d. 질량이 0인 원소는 소멸됩니다
3. 이동 과정 중에 원자가 만나는 경우는 합성으로 고려하지 않습니다.

시뮬레이션
원자들의 정보가 주어짐
격자에 원자들을 관리하기로 함
한칸에 여러개의 원자가 있을 수 있으므로


"""

n,m,k = tuple(map(int,input().split()))

# 현재 원자들의 위치를 기억하기 위한 격자
graph = [
    [[] for _ in range(n)]
    for _ in range(n)
]

# 원자가 이동한 위치를 저장하기 위한 격자
next_graph = [
    [[] for _ in range(n)]
    for _ in range(n)
]
dx = [-1, -1, 0, 1, 1,  1,  0, -1]
dy = [ 0,  1, 1, 1, 0, -1, -1, -1]
for _ in range(m):
    x,y,g,s,d = tuple(map(int,input().split()))
    graph[x-1][y-1].append((g,s,d))
# 원자들이 이동하는 함수 생성

# 해당방향 d로  속력 s만큼 x,y에서 출발해서 이동할건데 무작정 반복문으로 이동하면 시간초과다 수학을 사용한다
def next_pos(x,y,v,move_dir):
    # 이 부분이 핵심이다
    # 움직인 이 후 값이 음수가 되는 경우, 이를 양수로 쉽게 만들기 위해서는
    # n의 배수이며 더했을 때 값을 항상 양수로 만들어 주는 수인 nv를 더해주면 된다
    nx = (x + dx[move_dir] * v + n * v) % n
    ny = (y + dy[move_dir] * v + n * v) % n

    return nx,ny
def move_all():
    # 모든 격자를 순회하며 원자가 있는것들을 이동시킨다
    for i in range(n):
        for j in range(n):
            for g,v,move_dir in graph[i][j]:
                nx,ny = next_pos(i, j, v, move_dir)
                next_graph[nx][ny].append((g,v,move_dir))

# 2개 이상이라면 4개로 분리하는 함수
def split(x, y):
    sum_of_mass, sum_of_velocity = 0, 0
    num_of_dir_type = [0, 0]

    for w, v, move_dir in next_graph[x][y]:
        sum_of_mass += w
        sum_of_velocity += v
        num_of_dir_type[move_dir % 2] += 1

    start_dir = -1
    # 전부 상하좌우 방향이거나, 전부 대각선 방향으로만 이루어져 있다면
    # 각각 상하좌우 방향을 갖습니다.
    if not num_of_dir_type[0] or not num_of_dir_type[1]:
        start_dir = 0
    # 그렇지 않다면, 각각 대각선 방향을 갖습니다.
    else:
        start_dir = 1

    atom_cnt = len(next_graph[x][y])

    # 각 방향 갖는 원자를 추가해줍니다.
    for move_dir in range(start_dir, 8, 2):
        # 질량이 0보다 큰 경우에만 추가합니다.
        if sum_of_mass // 5 > 0:
            graph[x][y].append(
                (sum_of_mass // 5,
                 sum_of_velocity // atom_cnt,
                 move_dir)
            )


def compound():
    # 이동을 시킨후 다시 원래 현재 그래프로 합성이 일어나도록 하기위해 기존의 것은 초기화 시킨다
    for i in range(n):
        for j in range(n):
            graph[i][j] = list()
    for i in range(n):
        for j in range(n):
            # 이동한 원자들이 있는 칸에 2개이상이라면 4개로 분리한다 다 합쳐서
            if len(next_graph[i][j]) > 1:
                split(i,j)
            # 원자가 1개잇는 칸은 그대로 붙인다
            elif len(next_graph[i][j]) == 1:
                graph[i][j].append(next_graph[i][j][0])

# k초 동안 시뮬레이션함
def simulate():

    for i in range(n):
        for j in range(n):
            next_graph[i][j] = list() # 초기화 해주고 이동해야한다

    move_all() # 원자 이동한다

    compound() # 합성이 일어난다


for _ in range(k):
    simulate()

ans = sum([
    weight
    for i in range(n)
    for j in range(n)
    for weight, _ , _ in graph[i][j]
])
print(ans)