# 지도가 주어지는데 수직선이다
# 1번 부터 N번도시까지 인접한 도시사이에는 도로가 있다
# 각 도로마다 이동시간이 주어진다
# 이 도로를 어떻게 이동하는지에 따라 이동시간이 달라진다
# A,B,C,D타입이 주어지면
# 각각의 타입으로 이동할 때 걸리는 시간이 주어진다
# 제한조건 1. 몇몇 도로는 C타입을 이용할 수 없음
# 목적은 1번도시에서 N번도시까지 제일 빠르게 이동하고 싶다
# 1번방법 A타입으로만 가는경우
# 2번방법 B or D타입으로만 가는 경우
# 3번방법 C or D타입으로만 가는 경우
# 4번방법 D 타입으로만 가는 경우
# 제한조건 2. MaxD이 주어져서 D타입으로는 연속으로 이 거리이상으로 이동할 수 없다 조건
# N은 10000 이하 나머지는 int제한
# 제일 쉬운 방법인 A,D타입 각각으로만 이동하기
# 어려운 부분은 B or D / C or D 타입으로 가는 경우
# B or D 와  C or D 는 같은 맥락이다
# 두가지 타입을 이동할 수 있을 때 최단시간을 구하는 방법
# 완전탐색으로 구한다고 치면 모든 도로마다 두가지의 조건중 하나를 선택하므로
# 2^10000이 되므로 불가
# 완전탁색 불가
# 다이나믹 프로그래밍
# 테이블 정의 - 도로에 번호를 매김
# dp[i][0] = i번도로까지 이동 후 마지막은 D타입으로 이동한 경우의 수 중  최단거리
# dp[i][1] = i번도로까지 이동 후 마지막은 B or C타입으로 이동한 경우의 수 중 최단거리
# 왜 이렇게 되냐 b 나 c는 연속으로 타도 상관없지만 d는 제한이 있기때문에 2차원으로 나눈다
# 마지막에 i번 도로를 b or c 타입의 도로를 타는 경우를 생각해보자
# i-1번째 도로까지 최단거리 + i번째 도로에 b or c 타입의 도로를 탓을 때 걸리는 이동시간
# 즉 min(dp[i-1][0],dp[i-1][1]) + min(a[i][b] , a[i][c])

# 이제 남은 dp[i][0] 이 문제다
# i번 도로를 d 타입으로 이동한 것중에 최단시간을 구하고 싶다
# 가능한 파티션을 나눠 본다
# i-1까지 b or c 로 이동 후 i번째 d 타입을포 이동
# i-2까지 b or c 로 이동 후 i-1번째 도로부터 i번째까지 d 타입으로 이동
# i-3까지 b or c 로 이동 후 i-2번째 도로부터 i번째까지 d 타입으로 이동
# 각 파티션에 대한 최단거리를 쓸 수 있고
# TD가 maxD 이하인 경우에 대해서만 필터링도 해야함

import sys

si = sys.stdin.readline
MAX = sys.maxsize
n, m = map(int, si().split())
# 0번지부터 시작하는것이 아닌 1번지부터 시작하였다
a = [[]] + [list(map(int, si().split())) for _ in range(n)] # 각도로마다 a,b,c,d타입에 따른 이동시간을 입력받는다

# A타입의 경로를 이용하여 도로를 이동하는 경우
def use_A_only():
    ret = 0
    for i in range(1, n + 1):
        ret += a[i][0] # 0번이 A타입의 이동시간이므로 그냥 더한다
    return ret

# 타입이 1이면 B를 타입이 2면 C를 사용해서 푼다
def use_B_or_C(type: int):
    # 다이나믹 프로그래밍 테이블을 정의
    dp = [[MAX, MAX] for _ in range(n + 1)]  # (D, B or C)
    # 0번도로까지는 둘다 0분이면 갈 수 있다고 하고 초기화한다
    dp[0] = [0, 0]
    # 1번도로부터 푼다
    # 1번도로부터 b or c 타입부터 이용한다고 하면 가능한가?
    # 가능하다면 직전도로까지 제일 빠르게 이동하고 이 도로의 타입을 이동한다
    for i in range(1, n + 1):
        # (B or C)-ing the i-th inveral
        if a[i][type] != -1:  # if enable
            dp[i][1] = min(dp[i - 1]) + a[i][type]
        # use D in the i-th interval - D도로를 타는 경우
        D_length = 0
        # j는 뒤에서부터 앞으로 이동하는 식으로 하는것이 좋다 - 문워크기법
        for j in range(i, 0, -1):  # D-ing from j-th to the i-th interval
            D_length += a[j][3]
            # D타입으로 연속해서 이동했는데 M보다 커진다면 멈춘다 ( d타입을 한번이라도 이동해서 maxDfmf sjadjrksms ruddn wjqsmsek )
            if D_length > m: break  # exceed the limit
            # 만약에 이 경우도 있다 j-1번까지 잘 온 후 D타입으로 가는건데 j-1번까지 이동할 수 없는 경우도 제외해야한다
            if min(dp[j - 1]) == MAX: continue  # it is impossible to pass the (j - 1)-th interval
            dp[i][0] = min(dp[i][0], min(dp[j - 1]) + D_length)
   # 이 구역까지 돌리면 D타입으로만 이동하는 경우도 자연스럽게 구해진다 연속된구간으로 이동했을 경우 최대이동을 넘느냐도 같이 체크하면서 최솟값을 업데이트 한다
    return min(dp[n])


print(min(use_A_only(), use_B_or_C(1), use_B_or_C(2)))