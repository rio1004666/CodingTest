# 두큐의 원소의 합을 같게하도록 하는 최소 횟수
# 어떠한 방법으로도 같게 할 수 없다면 -1 리턴
# 두큐의 길이 30만
# 자료형 롱타입 고려
# 문제 이해 및 입출력 파악 큐원소 갯수 30만개 원소값 10억
# 유형 => 아이디어 구현
# 완전탐색 생각 나이브하게
# 두원소가 같게 되도록 한큐에서 한개를 빼고 다른큐에 붙여보고 같은지확인
# 두원소의 합이 같다는것은 반반이라는뜻이기때문에 전체원소의 합을 일단 구하자
# 두 큐의 길이는 같으므로 나이브하게 빼고 넣었다가 하다가 절반의 값이 넘어가면 스톱하고
# 두개씩 빼고 다시 넣어봄
# 혹은 각 큐의 합을 구해서 큰쪽에서 작은쪽으로 하나 넘기고 두 큐의 값이 반반인지 확인한다 이때
# 30만개의 모든 수의 합을 일일이 구하면 시간초과이므로 합을 기록했다가 빼거나 넣엇을때 계산한다
from collections import deque

MAX_SIZE = 300000  # 하드코딩영역


def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    q1sum = sum(queue1)
    q2sum = sum(queue2)
    half_sum = (q1sum + q2sum) // 2  # 절반의 값을 기록한다
    # 어느 한쪽의 큐의 합이 절반보다 큰경우에는 계속 빼고 그다음 작은쪽에서 받아서 또 빼서 상대큐로 넣어주게되면 시간적으로 거의 신경쓰지 않게 된다 while문으로 반복할것이다
    # 어차피 값이 큰상태에서 하나씩 빼고 상태방한테서 뺏어봣자 또 커지므로
    # 원소를 빼면서 작아지는 시점에서 상대방원소에서 가져와서 계산해보는것이 좋다
    # 순서대로 빼고 넣어보는것이므로
    if q1sum == half_sum:
        return 0
    # 30만개가 최대이고 30만개를 다빼도 점수가 다르다면 -1을 반환한다
    q1cnt, q2cnt = 0, 0

    # 둘중에 하나라도 다시 돌아오게 되면 벗어납니다
    while q1 and q2 and q1cnt <= MAX_SIZE and q2cnt <= MAX_SIZE:
        if q1sum == q2sum:
            break
        if q1sum < q2sum:
            while q2sum > half_sum:
                cur_num = q2.popleft()
                q2sum -= cur_num
                q1.append(cur_num)
                q1sum += cur_num
                answer += 1
                q2cnt += 1
        else:
            while q1sum > half_sum and q1:
                cur_num = q1.popleft()
                q1sum -= cur_num
                q2.append(cur_num)
                q2sum += cur_num
                answer += 1
                q1cnt += 1

    # 문제는 시간초과나는 케이스를 생각해야하는데
    # 한번씩 주고받는것이기때문에 절반보다 작아지면 바로 멈추고 다른큐에 붙이는 방식으로햇다
    # 그런데 이방식은 무한루프를 돌게되는경우가 있따 둘다 30만개인데 넣었다붙엿다를 반복하면서 계속 같아지지도 않고 빈큐가되지도 않기 떄문인데
    # 예외처리 부분
    # 한큐가 비어버리면 같을 수 없다고 판정이나고 -1 리턴
    if len(q1) == 0 or len(q2) == 0:
        answer = -1
    # 다시 원복되므로 -1리턴
    if q1cnt > MAX_SIZE or q2cnt > MAX_SIZE:
        answer = -1
    return answer