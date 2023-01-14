# 탑을 세운다
# N명의 사람이 있고 각 사람은 좋아하는 숫자가 있다 2개씩
# 모든사람이 탑에 모든 수를 볼 수 있도록 하고 싶다
# 제일 아래 2를 쓰고 4를 쓰고 3을 썻다면  탑에서
# a번 사람은 2는 원하는층이여서 좋다 a(2,4)이고 b(3,4) c(1,5)인경우 탑을 쌓을때
# 2를 먼저쌓고 그다음 4를 쌓으면 앞에 2를 쌓은사람이 좋아하는수이므로 만족하고
# 그다음 3을 쌓으면 이미 4를 좋아하는 b가 좋아하는 숫자에 3이 있으므로 쌓을 수 있고
# 또 3을 쌀아도 된다 # 같은숫자가 같은사람이 계속 좋아할수도있기때문에 중복은 1번허용되고 그 이후는 탑을 쌓지 않는다 => 가장짧은 탑높이
# 모든 층에서 모든 사람이 좋아하는 숫자를 다 볼 수 있도록 탑을 잘 쌓는다
# 최소층수를 쌓아서 만족하는 탑을 구한다
# 답이 여러개라면 사전순으로 가장 빠른 탑을 구한다 => 1부터 차례로 진행하기에 사전순으로 진행된다
# N = 10


# 코딩하며 설명
import sys
from turtle import back
#입력부
si = sys.stdin.readline
n = int(si())
pref = [list(map(int, si().split())) for _ in range(n)]
# 자료구조 선언부
sat = [[0, 0] for _ in range(n)]  # sat[i][j] := i번 사람이 j번 수를 본 횟수 => 기록해둔다면
# 브랭칭이 가능하다 즉 더이상진행하지 않아도 되는부분에서 효율성을 따질 수 있다

# 모듈화
def is_finish(st: list):
    # stack 의 top 원소까지 고려했을 때, 모두가 만족했다면 True, 아니면 False
    if len(st) == 0:
        return False
    for i in range(n):
        for j in range(2):
            # 어떤사람이 j번수를 본적이 이미 과거에 있다면 통과
            if sat[i][j] != 0: continue
            # 마지막 숫자도 누가 좋아하는 숫자인지 확인이되면 체크한다
            if pref[i][j] == st[-1]: continue
            # 위의 상황이 아니라면 더이상 탑을 쌓을 이유가 없음 조건이 충족이 되지 않음 => 브랜칭
            return False
    return True

# 다음 탑을 쌓아본다
def push(st: list, num: int):
    # stack에 num을 추가로 쌓음으로 인해서, 새롭게 만족한 사람 수
    cnt = 0  # 이번에 최초로 만족한 값이 있는 사람 수
    # 일단 쌓여있다면 체크해본다
    if st:
        # 넣을때도 뺄때도 마지막의 두숫자를 가지고 생각한다.
        a, b = st[-1], num
        # 4가 마지막에 있는 상태에서 3을 넣을때 4가 모든 각각의 사람들마다 4를 좋아하는수이면 +1카운팅해준다
        for i in range(n):
            for j in range(2):
                x = pref[i][j]  # i번 사람이 좋아하는 숫자
                # i번 사람이 좋아하는 숫자가 마지막에 있는 숫자와 같고
                # 현재 넣으려는 숫자가 그 사람이 좋아하는 숫자이면 카운팅 +1 해준다
                # 현재탑에 마지막에 있는 수가 이미 좋아하고 있고, 넣으려는수도 좋아하는수 목록에 있어야한다
                if x == a and b in pref[i]:
                    sat[i][j] += 1
                    # 2개이상이되면 더이상 넣지 않음
                    if sat[i][j] == 1:
                        cnt += 1
    # 탑에 쌓여있는것이 없다면 그냥 넣는다
    st.append(num)
    # cnt는 이번에 넣을 숫자가 어떤 숫자와 맞지 않으면 더이상 탐색할 필요가 없다는걸 나타낸다
    return cnt

# 다른 수를 넣어본다
def pop(st: list):
    # stack에 num을 추가로 쌓음으로 인해서, 새롭게 만족한 사람 수
    # 두개이상 쌓여있어야 마지막 원소와 그 전 마지막원소에서 좋아하는수 카운팅에서 뺀다
    if len(st) >= 2:
        a, b = st[-2], st[-1]
        for i in range(n):
            for j in range(2):
                x = pref[i][j]  # i번 사람이 좋아하는 숫자
                if x == a and b in pref[i]:
                    sat[i][j] -= 1
    st.pop()
    return

# 탐을 샇기 위한 정답스택 리스트입니다.
ans_stack = []

# 완전탐색

def backtracking(st: list, cnts: list):  # st := 이때까지 쌓은 탑, cnts := 각 층에서 새롭게 만족한 사람 수
    # 층을 쌓을때마다 확인해야하는부분들
    global ans_stack
    # 이미 정답스택보다 커진다면 그만둔다
    if ans_stack and len(st) >= len(ans_stack):
        return
    # 정답조건에 충족이 되었을때 최종정답에 저장한다
    if is_finish(st):
        # 정답을 구한다
        ans_stack = st[:]
        #print(ans_stack)
        return
    # 여기서 핵심은 현재 넣으려는 숫자를 넣었는데도 불구하고 해당되는 좋아하는 숫자가 없다면
    # 멈추고 그다음 좋아하는 숫자로 가는 방향이 최고이다 => 브랜칭
    # 1은 이미 좋아해서 1개의 카운팅이됫지만 계속 1을 넣게되면 무한으로 깊이가빠지게 되므로
    # 1을 3개이상 넣은시점에서 멈추고 돌아간다
    if len(cnts) >= 2 and cnts[-1] == 0 and cnts[-2] == 0:

        return
    for num in range(1, 6):  # 이번 층에 쌓아볼 차례
        cnt = push(st, num)
        cnts.append(cnt)
        backtracking(st, cnts)
        cnts.pop()
        pop(st)


_st, _cnts = [], []
backtracking(_st, _cnts)
print(*ans_stack)
# 2
# 2 3
# 1 2
# 정답 1 1 3 2
# 1 1 2 2 3 이면 정답보다 길어짐