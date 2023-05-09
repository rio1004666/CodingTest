"""

n개의 카드
각 카드마다 가격이 있다
+50 / x3 / x6 / +60 / 식도 적혀 있다
예산 : money
어떻게 예산안에서 어떤 순서로 카드를 사야 숫자를 최대한 크게 만들 수 있는가
시작할 때는 숫자가 S
N <= 10
가격 예산 <= 10억
S <= 1만

관찰 : n이 10뿐이다  => 완전탁샘 가능
     또 순서가 결과에 영향을 미침 => 순열 가능
     N! 가능하다
만약 n이 크다면
다이나믹 프로그래밍 생각해볼 수 있고
관찰은 더하기를 먼저하는게 무조건 이득이다

"""

import sys
si = sys.stdin.readline
n,s,m = map(int,si().split())
cards = []
for _ in range(n):
    value, equation = map(int, input().split())
    cards.append((int(value),equation))
ans = s
used = [False for _ in range(n)]
def apply(val,equation):
    if equation[0] == '+':
        return val + int(equation[1:])
    else:
        return val * int(equation[1:])
def func(val,money): # 현재 가지고 있는 수 val 와 money
    global ans
    ans = max(ans,val)
    for i in range(n):
        if used[i]:
            continue

        if cards[i][0] > money:
            continue
        used[i] = True
        func(apply(val,cards[i][1], money - cards[i][0]))
        used[i] = False
func(s,m)
print(ans)