# 10진수가 주어지면 2진수로 바꾸고 그 2진수를 포화이진트리로 바꿀 수 있는가 YES OR NO
# 포화이진트리로 바꾸는것은 정해진 규칙이 필요하다
# 0이 써있으면 더미노드 1이써잇으면 실제노드 이다
# 101(2) 은 세개의 정점이 되고
# 1이 실제로 존재 0은 더미노드
# 실제존재하는 노드가 더미노드 밑에 있다면 말이 안됨
# 즉 그래서 101(2)는 포화이진트리가 되지 않음
# 왼쪽부터 오른쪽으로 읽긴해야한다 이진수를
# 포화이진트리의 크기를 알아야함
# 예를들어 주어진 이진수가 6자리면
# 111011(2) 포화이진트리의 크기는 2^k-1이고
# 노드 3개도 안되고 7개도 안되고
# 그래서 7자리로 맞추기 위해 0을 추가할것이다 앞에
# 크기에 맞게 이진수앞에 0을 패딩한다
# 지레겁먹고 직접트리를 만들필요는없다
# 1이써져야하는위치에 1이 잇어야만 함
# 1이써져잇는곳에서 모든 부모노드가 1이면된다 => 관철
# 1위에 1이 있나

# 우선 루트에 있는 친구는 가운데있는 친구이다
# 0번지부터 6번지까지중 3번지에 있는 친구
# 1이 써져있네 => 조건 충족
# 왼쪽은 0~2번지 오른쪽은 4~6번지
# 그럼 0~2번지 중 또 가운데가 루트노드
# 그래서 루트노드의 또 왼쪽자식 오른쪽자식도 1이써져잇으니 문제가 없다
# 이런식으로 트리를 반씩 쪼개나가면 트리를 구성해나갈 수 있다
# 리프노드에 도달하면 더미노드든 실제노드든 상관이없다
# 이제 구현이 문제이다
# 여기서 2진트리는 어떤 특정한 트리자료구조를 만들어서 조건에 충족해서 포화이진트리냐 아니냐를 판단하는것이 아닌 재귀적인 dfs 알고리즘을 통해서
# 루트노드와 자식노드간의 관계를 파악하는것이 핵심이다.


import sys
si = sys.stdin.readline

def solve(binary : str, L : int , R : int ) -> bool:

    if L == R:
        return True

    mid = (L + R) // 2
    root = binary[mid]
    left_child = binary[ (L + ( mid - 1 )) // 2]
    right_child = binary[ (( mid + 1 ) + R) // 2]
    if left_child == '1' and root == '0':
        return False
    if right_child == '1' and root == '0':
        return False
    # 하나라도 만족하지 못하면 False 를 반환해야합니다.
    return solve( binary , L , mid - 1 ) and solve( binary, mid + 1, R )



Q = int(si())

for _ in range(Q):
    num = int(si())
    binary = bin(num)[2:]
    tree_size = 1
    # 만약 5개뿐이라면 패딩을 하므로 7개로 잡힌다 => 포화이진트리의 특성상 갯수는 1 , 3 , 7, 15...
    while tree_size < len(binary):
        tree_size = tree_size * 2 + 1
    binary = '0' * (tree_size - len(binary)) + binary # 3인경우 2진수로 표현하면 2개이므로 0을 앞에 패딩한다

    if solve(binary,0,len(binary)-1):
        print('Yes')
    else:
        print('No')

# 시간복잡도