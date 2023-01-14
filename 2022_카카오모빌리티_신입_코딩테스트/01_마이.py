# 꽃이 피고 지는 시간이 주어짐
# 적어도 한종류의 꽃이 피어있는 기간 구하기
# 관찰
# 각 꽃이 지는 시간
# 꽃의 개수 100이하
# 꽃이 피는 날짜 지는날짜 365 이하
# 365로 전체 배열 하나 잡고
# 각 꽃을 체크 해보면서
# 피어 있는 날짜 2일부터 5일 미만까지 배열에 체크
# 꽃이 피는기간 배열 하나 생성
# 범위는 1이상 100이하
def solution(flowers):
    answer = 0
    arr = [0 for _ in range(366)]
    for flower in flowers:
        # 각 꽃마다 피기 시작한 시간 지는시간 범위로 체크해주고
        start = flower[0]
        end = flower[1]
        for i in range(start,end):
            arr[i] += 1
    # 1년 365일 순회하면서 피어있는 수가 1이상이면 정답 추가
    for i in range(1,366):
        if arr[i] > 0:
            answer += 1
    return answer