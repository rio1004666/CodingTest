"""
1일 2일 3일 4일 ..... 1000일째 되는 날
바나나 N개
적어도 하루에 하나는 바나낟를 사야한다
각 날에는 바나나의 할인율이 적혀져 있다
그 날에 할인율이 없는 바나나도 있다
N일이 되기전에 바나나를 모두 살 수 있다
바나나의 가격을 최소로 하게 하는 방법은 어떤것인가
모든 바바나를 구매했을 경우 최소비용은?

V,D,P 는 바나나의 가격, 바나나의 할인 날짜 , 바나나의 할인률

어떻게 이 문제를 접근 할 수 있을까???

우선 1일째에 ( 1일째 할인하는 바나나들을 ) 다산다
2일째 할인하지 않는다면 미래에 살 바나나를 하나 끌어와서 산다
그런데 문제가 생긴다 .
1일째 1000월짜리 1% 할인하는 바나나 두개 2일째 할인 없고
3일째 1000원짜리 99% 할인하는 바나나가 있다면
2일째에는 3일째 99% 할인에 살 바나나를 끌어와서 살 수 있다
그러면 최대 할인율이 되는가? 아니다
1일째 1000원짜리 1% 할인되는 바나나를 끌고 와야한다 왜냐 일단 2일째 바나나를 적어도 하나는 사야하기때문에
그렇게 되면 990원 + 1000원 + 10원  => 전체가격이 2000원으로 이게 정답이 된다
즉 1일째날에 할인하는 바나나를 무조건 산다고 해서 이득이 아니라는것
즉 그리디하게 가지만 반드시 정답을 내지는 않는것
그래서 N번째날에 N개의 바나나를 모두 산다고 해서 반드시 이득이 아니다
1일부터 1000일까지 있는데
적어도 모든 날에 적어도 1개를 사야하는가에 대한 대답을 할 수 없어서
1일부터 L일을 마지막으로 잡고 바나나를 모두 살때 이득의 최대를 구한다
L+1 이후에 할인되는 바나나들은 할인의 효과를 받지 못할 것이다
이 애들은 아낄 수 없고 원가로 사야한다
L일 이하로 사는 바나나들은 얼마씩 이득을 볼 수 있는지 관찰한다
1일에 10000원 20% 할인 (2000원할인)/15000  30% 할인 (4500원할인) / 20000 5% 할인 (1000원할인)
그렇다면 1일에 적어도 하나는 이 셋중에 하나는 사야하는데 가장 할인이 큰 15000원짜리 바나나를 사야하는게 이득이라는것을 알 수 있다
이 세개의 바나나를 다른날에 사게 되면 이득을 못보고 다른날에 사야하는 바나나도 이 1일에 산다면
할인을 받을 수 없으므로 그리디하게 가장 할인을 많이 받는 바나나는 무조건 하나 사야한다
즉 1일에 할인율이 가장 큰 바나나를 고정으로 사야함
2일에는 할인하는 바나나가 없다 그럼 어떤 바나나를 적어도 무조건 1개를 사야할까?
모든 바나나 바나나중에서 할인이 가장 작은 바나나를 사는게 이득이다
그 후 그 다음 할인율이 큰 바나나를 1일에 사는것이 최적의 답이다
그리고 그다음에 할인하지 않는날에는 앞서 가장작은 할인율의 바나나 다음의 적은 할인율이 적용된 바나나를 산다
즉 정렬해서 차례대로 할인하지 않는 날에 바나나를 사는것이 이득이다
그러면 그리디가 최적의 정답을 보장한다 즉 더 할인율이 높은 바나나를 할인이 적용하지 않는날에 사는것보다 이득이다


즉 키워드는 sortings / greedy / constructive algorithms


"""

import sys
si = sys.stdin.readline
N = int(input())
items = [[] for _ in range(N+1)]
total_cost = 0

for _ in range(N):
    # 바나나들이 입력으로 주어진다
    V,D,P = map(int,input().split()) # 가격 , 할인되는 날 ,  할인율
    items[D].append((V,P)) # 그 바나나가 D일에 할인한다면 원가 V 할인이
    # 모든 바나나의 원가들을 더한 총합을 구하고 나중에 이득을 가장 많이 본 할인액을 빼주면 정답이 된다
    total_cost += V # 원가들을 모두 더함
    # 최소비용으로 구매가능하

def get_profit(item):
    return item[0] * item[1] // 100 # 할인액수
# 내가 마지막날에 모든 바나나를 다삼 적어도 하루에 하나의 바나나는 무조건 사야함
def solve(last_day): # return maximum profits I get when I buy the whole items in last_day
    profits = []
    saved = 0
    # 매일같이 보면서
    for  d in range(1,N+1):
        # 물건을 살 수 있는 즉 마지막날 이전의 날짜라면
        if d <= last_day: # if d <= last_day, able to buy items with discounted price
            # 할인하는 바나나가 있다면
            if items[d]:
                # 할인하는 바나나의 할인액을 모든다
                ps = [get_profit(item) for item in items[d]]
                # 정렬한다
                ps.sort()
                # 나머지 할인하는 바나나들은 모아둔다
                profits.extend(ps[:-1])
                # 가장 할인 받는 바나나를 사서 이득율을 더한다
                saved += ps[-1]
        # 할인을 못받기때문에 할인으로 보는 할인액이 0원이다
        else: # otherwise, don't able to save the money for these items
            profits.extend([0 for _ in range(len(items[d]))])
    # 위에서 설명했던 할인하지 않는 날에 차례대로 가장 적은 할인을 받는 바나나부터 뽑아오기 위해 정렬한다
    profits.sort() # "IMPORTANT" sort ascending the profits
    cnt_empty = 0 # number of the das that no items are discounted
    # 다시 1일부터 마지막날까지 본다
    for d in range(1,last_day+1):
        # 위에서 설명했듯이 할인하지 않는 날에는 할인율이 적은 바나나부터 사기로 했으므로 카운팅하고
        # 작은 할인율로 적용된 바나나들을 샀을 경우에는 원가로 산다
        if not items[d]:
            cnt_empty += 1
    # saved에 가장 큰 할인을 받는 바나나들을 샀을 경우 확정에다가
    # 추가로 확정된 할인하는 바나나들의 이득을 더해주면 된다/
    # cnt_empty이전의 할인이 적용된 바나나들은 그냥 원가로 산다 즉 할인이 없으으로
    # 그 이후에 할인이 적용되는 바나나들을 샀을 경우 취할 수 있는 이득율을 전부 더한다
    return saved + sum(profits[cnt_empty:]) # Buy the least(cnt_empty) discounted items as its original items

ans = 0

# last_day가 1일인지 2일인지 3일인지 모르니까 모든 Last_day를 정해봄
for last_day in range(1,N+1): # buy whole items in (last_day)-th day <- this is point
    ans = max(ans , solve(last_day))

print(total_cost - ans)