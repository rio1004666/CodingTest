# 포인트
# i 번째 원소가 없다고 생각했을 때의 총 계산 결과 = (i 왼쪽 계산 결과) + (i 오른쪽 계산 결과)
# 왼쪽과 오른쪽은 전처리로 계산해두면 된다.
# O(N)
import sys

si = sys.stdin.readline
n = int(si())
a = list(map(int, si().split()))
left = [0 for _ in range(n)]  # left[i] := a[0 ... i] 에 대한 계산 결과
right = [0 for _ in range(n)]  # right[i] := a[i ... n] 에 대한 계산 결과
flag = 1
for i in range(n):
    if i == 0:
        left[i] = a[i]
    else:
        left[i] = left[i - 1] + a[i] * flag
    flag = -flag
for i in range(n - 1, -1, -1):
    if i == n - 1:
        right[i] = a[i] * flag
    else:
        right[i] = right[i + 1] + a[i] * flag
    flag = -flag
ans = []
for i in range(n):
    l, r = 0, 0
    if i > 0:
        l = left[i - 1]  # i 의 왼쪽 결과
    if i < n - 1:
        r = right[i + 1]  # i 의 오른쪽 결과

    if l + r == 0:
        ans.append(i + 1)
print(len(ans))
print(*ans)
'''
4
2 5 3 1
=>
2
2 4
6
2 5 6 7 8 4
=>
2
3 5
'''