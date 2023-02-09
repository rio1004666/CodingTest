"""
팩맨문제
일단 이 문제의 특이한점은
복제가 일어난다는점
그리고 4x4 2차원 격자에 턴수가 25턴이고 작다
또 몬스터수가 복제되므로 100만마리를 이동하려고 하다보면 시간초과가 생길 수 있다 10마리에서 출발한다고 하더라도
자료구조 설계는 4차원배열을 생성한다
우선 턴수마다 각각 2차원 격자를 정의하기 위한 3차원에다가 그 각각의 격자안에 있는 각각의 칸들에 대해 방향마다 몬스터수가 몇마리 있는지 파악하기 위해서이다
그리고 몬스터 시체의 카운팅을 하기위해 또 카운팅하는 2차원격자에 각각의 칸에 3턴을 표현하기 위해 3차원 배열을 선언해준다
이렇게 한 후 시뮬레이션 진행하면서 함수화해나가면 된다
팩맨이 3번이동하면서 가장 몬스터를 많이 먹을 수 있는 경로를 정하는것은 dfs탐색을 사용해도 된다


"""
MAX_T = 25
MAX_N = 4
DIR_NUM = 8
P_DIR_NUM = 4
MAX_DECAY = 2

n = 4
m,t = map(int, input().split())
px,py = map(int, input().split())
px -= 1
py -= 1
monster = [
    [
        [
            [0] * DIR_NUM
            for _ in range(n)
        ]
        for _ in range(n)
    ]
    for _ in range(MAX_T + 1)
]
dead = [
    [
        [0] * (MAX_DECAY+1)
        for _ in range(n)
    ]
    for _ in range(n)
]

dxs = [-1, -1,  0,  1, 1, 1, 0, -1]
dys = [ 0, -1, -1, -1, 0, 1, 1,  1]

p_dxs = [-1,  0, 1, 0]
p_dys = [ 0, -1, 0, 1]


def move_monster():








def simulate():
    move_monster() # 몬스터가 움직인다
    move_packman() # 팩맨이 움직인다
    decay_monster() # 몬스터가 죽은 곳에 카운트를 센다
    add_monster() # 직전의 턴에서 몬스터들이 복제한 알들이 부화해서 다음턴에 더해진다 각 방향을 가진 몬스터의 수가 더해짐









for _ in range(m):
    mx,my,md = map(int, input().split())
    monster[0][mx-1][my-1][md-1] += 1

tnum = 1

while tnum <= t:
    simulate()
    tnum += 1
print(count_monster())
