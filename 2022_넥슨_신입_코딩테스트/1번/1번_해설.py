
# 포인트:
# 0개 살 수 있는가? 1개 살 수 있는가? 2개 살 수 있는가? ... N개 살 수 있는가?
# 모든 질문에 대한 대답을 찾으면 오래 걸린다
# 다행히 K개를 살 수 있으면 K개 이하는 전부 가능하고, K개를 못 사면 K개 이상은 전부 불가능한 점을 이용해서 parametric search가 가능하다.
# O(log 10억)
import sys
si = sys.stdin.readline
n, m, sell_price, buy_price = map(int, si().split())
def possible(want):  # want 개 만큼을 살 수 있는가?
    if want > n:
        return False
    can_sell = n - want                      # can_sell := 팔 수 있는 개수
    total_money = m + can_sell * sell_price  # 판 뒤에 가진 총 돈
    need_money = want * buy_price            # 필요한 총 돈
    return total_money >= need_money
L, R, ans = 0, n, 0
while L <= R:
    mid = (L + R) // 2
    if possible(mid):
        ans = mid
        L = mid + 1
    else:
        R = mid - 1
