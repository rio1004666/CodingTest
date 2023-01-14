
# 여기 해설에서는 날수만으로 계산하였다
# 1일1저축이 깨지는 순간의 기준은 일과 일사이에 2일이상이 차이난다면 깨지는것으로 하였고
# 이렇게 날수만으로 체크하면 굳이 연도별로 계산해주지 않아도 된다
# 총일수가 계속 계산이 된다


import sys
from typing import List

si = sys.stdin.readline
S = si().strip()
N = int(si())


def parse_start_date(T: str) -> List[int]:
    # Y:M:D:H:m:S 로 구성된 시간에서 [D, H, m, S] 를 파싱하는 함수
    v = list(map(int, T.split(':')))
    return v[2:]


S = parse_start_date(S)
days = [S[0]]  # 저축한 날의 D 값을 나열한 배열. 시작은 S[0]일에 시작
for _ in range(N):
    delta = list(map(int, si().split(':')))  # 다음 저축일까지의 시간을 [D, H, m, S] 형태로 변환
    for i in range(4):
        S[i] += delta[i]

    S[2] += S[3] // 60  # 60초를 넘으면 1분 증가시키고 60초 미만으로 변환
    S[3] %= 60
    S[1] += S[2] // 60  # 60분을 넘으면 1시간을 증가시키고 60분 미만으로 변환
    S[2] %= 60
    S[0] += S[1] // 24  # 24시를 넘으면 1일을 증가시키고 24시 미만으로 변환
    S[1] %= 24
    days.append(S[0])  # 새로운 저축일의 D 값을 저장
interval_length = days[-1] - days[0] + 1  # (제일 마지막 날 - 처음 날 + 1) 기간만큼 저축
flag = True
for i in range(1, N + 1):
    if days[i] - days[i - 1] > 1:  # 두 저축 시각 사이에 2일 이상 벌어졌다면, 연속이 깨짐
        flag = False
print(1 if flag else 0, interval_length)