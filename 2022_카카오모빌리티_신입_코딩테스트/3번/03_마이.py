# 첫 저축을 시작한 시각 문자열 s
# 다음 저축까지 걸린 기간을 담은 문자열 times 가 주어지면 1일 1저축과
# 저축기간 마지막저축날 - 첫저축나라
# 윤년은 없고 모든 달은 30일이 마지막날
# 1년 360일
# 딕셔너리에 몇일에 저금을 했음을 기록한다
from collections import defaultdict


def solution(s, times):
    answer = []
    time_dict = defaultdict(int)

    # 일단 시작 날짜를 분리해서 관리한다
    start = list(map(int, s.split(':')))
    start_backup = list(map(int, s.split(':')))
    # 그 다음 시간을 하나씩 차례대로 불러온다=
    # 첫 저축을 딕셔너리에 기록 날짜
    # 이게 같은날에 두번이상 저축을 하는건 하나로 치기때문에 키를 년도+월+날로 계산해야함
    oneday = ''.join(list(map(str, start[:3])))  # 1일1저축을 알기 위해 키값을 이렇게 정한다
    # 저축기간은 그냥 빼기 계산만 하면된다
    # 년도도 바뀌고 달도 바뀔 수 있기때문이다

    time_dict[oneday] = 1

    for time in times:
        next_time = list(map(int, time.split(':')))
        # 60초가 넘어가면 분 + 1
        start[4] += ((start[5] + next_time[3]) // 60)
        start[5] = (start[5] + next_time[3]) % 60
        # 60분이 넘어가면 시 + 1
        start[3] += ((start[4] + next_time[2]) // 60)
        start[4] = (start[4] + next_time[2]) % 60
        # 24시가 넘어가면 일 + 1
        start[2] += ((start[3] + next_time[1]) // 24)
        start[3] = (start[3] + next_time[1]) % 24
        # 30일이 넘어가면 월 + 1
        start[1] += ((start[2] + next_time[0]) // 30)
        start[2] = (start[2] + next_time[0]) % 30
        # 12월이 넘어가면 년 + 1도 되야한다
        if start[1] > 12:
            start[0] += 1  # 년도 +1
            start[1] = start[1] - 12
        oneday = ''.join(list(map(str, start[:3])))
        time_dict[oneday] = 1

    # 최종적으로 저축기간을 구한다
    # 해가 다른경우 해가같은 경우로 나누어서 처리해야한다
    sy, sm, sd = start_backup[:3]
    ey, em, ed = start[:3]
    total_day = 0
    if sy == ey:
        first = ((sm - 1) * 30) + sd
        second = ((em - 1) * 30) + ed
        total_day = second - first + 1
    if sy < ey:
        y_differ = ey - sy - 1  # 중간에 360일풀로 계산되는 해수
        first_differ = 360 - (((sm - 1) * 30) + sd) + 1  # 첫해 날수 계산
        second_differ = ((em - 1) * 30) + ed  # 마지막해 날수 계산
        total_day = (y_differ * 360) + first_differ + second_differ
    if total_day == len(time_dict):
        answer.append(1)
    else:
        answer.append(0)
    answer.append(total_day)

    return answer