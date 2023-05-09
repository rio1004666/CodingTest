"""
1. 문제이해

   택배를 배달하면서 수거한다

2. 관찰 및 전략

   1) 배달 및 수거함 택배상자가 남은 가장 먼 집부터 택배를 배달 및 수거
   2) 트럭이 물류창고에서 출발해 가장 먼 집으로 이동할 때는 배달만 하고, 다시 물류창고로 돌아올 때는 수거만 한다
   3) 트럭이 물류창고에서 출발해 이동할 때는 최대 택배를 배달하고 다시 물류창고로 돌아올 때는 최대 빈상자를 수거한다

3. 자료구조 및 알고리즘

   스택자료구조 활용
   그리디 알고리즘 ( 가장 이득이 되는 전략 / 우선순위큐 , 순서, 정렬 등 전략 활용 )

4. 시간복잡도

   O(N^2) 으로 하면 터진다
   N으로 줄여보자
   일직선이므로 가장 먼곳인 N-1번째 집을 방문하면서 다른 N-1번째 이하의 집들까지 방문할 수 있다는점에 주목한다
   한번 배달할 때 최대한 많이 배달해준다


5. 구현과정

   1. 집 번호와 해당 집에 배달할 택배 개수를 집 번호가 작은 순서대로 배달 스택에 담습니다.
   2. 집 번호와 해당 집에 수거할 빈 택배 개수를 집 번호가 작은 순서대로 수거 스택에 담습니다.
   3. 배달 스택에서 가장 위에 위치한 원소의 집 번호와 수거 스택에서 가장 위에 위치한 원소의 집 번호를 비교해 큰 값의 두 배만큼 answer에 더합니다. 이때, 두 배를 더하는 이유는 트럭이 물류창고부터 가장 먼 집까지 왕복하기 때문입니다.
   4. 이번에 배달 가능한 개수가 0이 되거나 배달 스택이 빌 때까지 배달 스택에서 남은 배달을 처리합니다.
   5. 이번에 수거 가능한 개수가 0이 되거나 수거 스택이 빌 때까지 수거 스택에서 남은 수거를 처리합니다.
   6. 배달 스택과 수거 스택이 모두 빌 때까지 3, 4, 5 과정을 반복합니다.

"""

"""

    무조건 관찰이 중요하다 
    관찰에서 모든 실마리가 풀리고 어떤 자료구조를 사용해야할지 알고리즘을 사용해야할지 보인다 
    여기서 관찰은 가장 먼거리부터 배달 및 수거를 모두 해야만 
    이동하는 거리가 최소가 됨을 알 수 잇따 
    그래야 다시 먼거리로 오지 않기 때문이다 
    그러면 가장 먼거리에 있는 집부터 방문하게 된다면 뒤에 있는 원소를 방문하여 꺼내게 된므로
    스택을 활용한다 
    그렇게하면 시간복잡도 O(N)에 해결할 수 있다 

    그리고 배달할 택배가 있는 집만 스택에 담습니다.
         수거할 빈상자가 있는 집만 스택에 담습니다. 

"""


def solution(cap, n, deliveries, pickups):
    answer = 0

    # 배달할 택배가 있는 집의 번호와 갯수를 담습니다. 리스트 컴프리핸션
    d_stack = [[idx, d] for idx, d in enumerate(deliveries, start=1) if d > 0]
    p_stack = [[idx, p] for idx, p in enumerate(pickups, start=1) if p > 0]
    # 모든 배달과 수거를 마칠때까지 반복한다
    while d_stack or p_stack:
        deliv, pick = 0, 0  # 해당 집의 배달해야하는 택배수와 수거수
        deliv_no, pick_no = 0, 0  # 해당 집의 번호 (거리를 계산하기 위해)
        if d_stack:
            deliv = d_stack[-1][1]
            deliv_no = d_stack[-1][0]
        if p_stack:
            pick = p_stack[-1][1]
            pick_no = p_stack[-1][0]
        max_dist = max(deliv_no, pick_no)  # 배달할 택배가 있는 집번호와 수거할 택배가 있는 집번호와 비교
        answer += (2 * max_dist)  # 그 중 가장 큰것이 먼집이므로 거리를 정답에 누적한다
        # print(deliv,pick,max_dist)
        # print(answer)
        deli_cap = cap
        pick_cap = cap

        while deli_cap > 0 and d_stack:
            if deli_cap >= d_stack[-1][1]:
                deli_cap -= d_stack[-1][1]
                d_stack.pop()
            else:
                d_stack[-1][1] -= deli_cap
                deli_cap = 0

        while pick_cap > 0 and p_stack:
            if pick_cap >= p_stack[-1][1]:
                pick_cap -= p_stack[-1][1]
                p_stack.pop()
            else:
                p_stack[-1][1] -= pick_cap
                pick_cap = 0

    return answer