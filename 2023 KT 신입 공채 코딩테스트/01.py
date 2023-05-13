"""
1번문제

1.문제이해

2명의 사람 A,B가 있고 각 사람은 카드를 들고 있다
카드에 적힌 숫자들은 모두 다르다
그리고 매직넘버 K가 주어진다
원하는것 : A가 B가 가지고 있는 카드 모두를 내려 놓아야 하고 원하는 순서대로 내려 놓을 수 있다
맨 처음에는 아무나 카드를 낼 수 있다
두번째부터는 이전보다 큰카드 혹은 이전보다 K 만큼 작은카드를 낼 수 있다

A사람이 카드 1번
B사람이 카드 2번 4번
A사람이 카드 5번 6번 순서로 냈다면

K=3이라면
B가 2번 4번을 내고
A가 1번(K가 3이므로) 5번 6번 낼 수 있다
이와 같은 순서로 카드를 냈을 경우 A에서 B로 바뀌고 B에서 A로 바뀌는
횟수가 제일 적은 방법을 찾는것이 목표 (매직넘버를 적절히 잘 사용해서)
A,B가 가지고 있는 카드의 수는 최대 4장까지 가능
숫자와 K = 100까지 가능

2. 관찰

   우선 카드가 최대 8개뿐이다 => 숫자가 작다 => 완전탐색
   그러면 기본적으로 8! 로 순서있는 줄세우기 하면 될듯?
     8개의 카드를 순서를 고려하여 세우고
   각 카드를 체크하며 이전카드보다 크거나 k만큼 작은지 체크하고 올바른 카드순서라면
   A->B 와 B->A 횟수를 체크하면 된다 이 떄 각 카드가 누구 거인지 같이 저장되어 잇으면 카운팅하기 좋다

"""
import sys

si = sys.stdin.readline
n, m, k = map(int, si().split())
nums = []
a = list(map(int, si().split()))  # A's cards
for x in a:
    nums.append((x, 1))
a = list(map(int, si().split()))  # B's cards
for x in a:
    nums.append((x, 2))
used = [False for _ in range(n + m)]
path = []
ans = n + m


# 순서가 있고, 중복이 허용되지 않는 순열 완전 탐색 수행
def backtracking(idx, last):  # idx := 몇 번째 카드를 놓을 차례?    last := 마지막에 놓은 카드의 크기?
    global ans
    if idx == n + m:  # 모든 카드를 내려놓은 상태!
        turns = 0
        for i in range(1, n + m):
            if path[i][1] != path[i - 1][1]:
                turns += 1

        ans = min(ans, turns)
        return

    # 이번에 내려놓을 카드 결정
    for i in range(n + m):
        if used[i]: continue  # 이미 사용한 카드면 무시
        if nums[i][0] > last or nums[i][0] == last - k:
            used[i] = True
            path.append(nums[i])
            backtracking(idx + 1, nums[i][0])
            used[i] = False
            path.pop()


backtracking(0, -1)
print(ans)