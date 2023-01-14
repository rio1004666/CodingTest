# 지도가 주어짐
# 도시가 주어짐
# 도로마다 거리가 존재
# 각 도시마다 빵을 사고 싶어하는 사람의 숫자가 주어짐
# 제한조건 1. 사람마다 이동할 수 있는 최대거리 D가 주어짐
# 제한조건 2. L이 주어지는데 정점 두개를 결정해서 편의점을 설치
# 각 편의점에 매입되는 빵의 개수가 L개씩 유입이 됨
# 목적은 편의점 두개를 잘 설치해서 제일 많은 사람이 빵을 살 수 있도록 함
# 도시수 N = 50 나머지도 50제한
# 사고를 많이 해야함


# N이 작으므로 편의점 설치가 가능한 모든 조합을 다 생각함
# 최대 빵 개수 계산.......계속해서 모든 조합의 경우의 수에 대해 각각에 대해 문제를 푼다
# N^2으로도 가능한가 접근시도
# 최대 빵 개수 구하기는
# 편의점 두개를 설치했다고 가정하고
# 모든 도시마다
# 모든 도시마다 갈 수 있는 편의점이 있고 못가는 편의점이 존재
# D가 제한이기때문에
# D를 넘어서는 도시까지의 거리는 못간다라고 생각할 수 있다
# 최대한 많은 빵을 사게하고 싶다
# 그리디 하게
# 1. 아무 편의점도 못가는 도시는 무시해야 한다 - 직관 1
# 2. 두개의 편의점 중 하나만 갈 수 있는 도시들이 있다 - 최대한 그 편의점으로 가서 팔린 빵 개수 카운팅 직관 2
# 3. 두개의 편의점 모두 갈 수 있는 도시는 남아있는 빵을 모두 살 수 있는지 판단 - 도시의 사람수와 빵의 개수 중 더 작은 값이 팔린 빵의 개수이다 - 직관 3
# 이런걸 맥시멈 매칭이라고 한다
# 구현은 그나마 간단
# 플로이드 워셜 = N의 개수가 작을 떄 최단거리 계산
# v1,v2에 편의점 설치
# solve 함수에서 최대한 많은 빵을 살수 있는 갯수 업데이트
# cnt 4가지 표현 - 비트연산으로 표현
# 아무도 갈 수 없는 경우 = -
# v1 편의점만 갈 수 있는 경우 = 1
# v2 편의점만 갈 수 있는 경우 = 2
# v1,v2 편의점 둘 다 갈 수 있는 경우 = 3
import sys

si = sys.stdin.readline
MAX = sys.maxsize
n, m, D, L = map(int, si().split())
dist = [[MAX for _ in range(n + 1)] for _ in range(n + 1)]
users = [0] + list(map(int, si().split()))
for i in range(1, n + 1): dist[i][i] = 0
for _ in range(m):
    u, v, d = map(int, si().split())
    dist[u][v] = d
    dist[v][u] = d
# floyd-warshall, O(N ^ 3)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


# return the maximum mathing
def solve(tgts):
    cnt = [0, 0, 0, 0]  # cnt[bit] := num of users who can reach {bit} CVSs
    for i in range(1, n + 1):
        flag = 0  # flag = 0 -> nowhere, 1 -> only can reach first target, 2 -> only can reach second target, 3 -> can reach both targets
        for bit, t in enumerate(tgts):
            if dist[i][t] <= D:
                flag |= 1 << bit
        if flag > 0:
            cnt[flag] += users[i]  # users in the area {i} can reach {flag} targets.
    # match the users who only can reach one target as a top priority
    ret = 0
    left = [L, L]
    for k in range(2):
        matched = min(left[k], cnt[1 << k])
        ret += matched
        left[k] -= matched

    # match the users who can reach to the both targets
    matched = min(sum(left), cnt[3])
    ret += matched
    return ret


ans = 0
for v1 in range(1, n + 1):
    for v2 in range(v1 + 1, n + 1):
        # assume that the CVS are v1 and v2.
        ans = max(ans, solve((v1, v2)))
print(ans)