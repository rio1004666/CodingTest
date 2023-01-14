from collections import deque
import sys
si = sys.stdin.readline
ans = 0
def solution(que1,que2):
    global ans
    queSum = sum(que1) + sum(que2)
    # 정확히 반반점수가 아니라면 동일하게 점수를 만드는것은 불가능함
    if queSum % 2:
        return -1
    target = queSum // 2
    n = len(que1) # 경계선의 시작
    start = 0 # 투포인터중 첫번째 포인터
    end = n - 1 # 투포인터중 두번째 포인터 => 정확히 반부터 시작한다
    cur = sum(que1)
    que3 = que1 + que2
    while cur != target:
        if cur < target:
            end += 1
            # 끝까지 연산을 해도 같아지는 오른쪽큐가 비어버린다면 목표값에 도달할수없으므로 -1을 리턴
            if end == n*2:
                return -1
            cur += que3[end]
        else:
            cur -= que3[start] # 먼저 점수를 까고
            start += 1 # 인덱스를 이동한다
        ans += 1 # 한번의 연산후 정답 카운팅한다

solution([1, 2, 1, 2],[1, 10, 1, 2]	)
print(ans)