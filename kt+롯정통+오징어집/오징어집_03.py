"""
수열이 주어진다
길이가 N

30 10 20 15 25 10 6
k값이 주어진다
이 수열에서 연속한 k개를 선택한다
선택해볼때마다
Q개의 구간이 주어지는데 고정되어있다
5-13
10-15
20-25
30-31
이렇게 4개의 구간이 존재한다
이 선택된 k개의 숫자들이
이 4개의 구간을 커버해야한다
만약 k=4이고
30 10 20 15 를 선택했다면
커버가능
만약 10 20 15 50 을 선택했다면
두개의 구간인 10-15와 20-25를 선택하면
커버 가능하다
연속한 K개를 잘 선택해서 필요한 구간의 수를 최소화하도록
한다
구간끼리 겹칠 수 있다
N <= 5000
Q <= 10000
숫자의 범위는 20억 이하

눈치를 채보는건데
수열의 특성이 없다 특정한 조건이 붙지 않앗음
k개를 선택해는 방법은 꼼수부리지 말고 다 봐야한다
적당히 몇개의 선택지만 스킵할 수 있지 않을까? 의미없다
브루트포스로 찍어본다 연속된 K개를 일단 다 본다

k개의 숫자가 주어지면 모든 수를 커버하는데
필요한 구간의 수(최소)
k개중 숫자가 30이 있다면
구간에서 어떤 구간은 짧은 구간이고 긴구간이고 ...
무슨 구간을 선택하는것이 이 30을 커버하면서
최소를 만족할까?
이렇게 무턱대로 구간을 고르면 대답할 수가 없다

K개중에 아무거나 잡지 말고 모든수를 커버해야하므로
제일 왼쪽숫자부터 하나씩 커버해보자

이 숫자도 여러개의 구간에의해서 커버가 가능할테지
어차피 왼쪽숫자부터 커버를 해야하기때문이다
왼쪽에는 숫자가 없다라는 사실때문에 가능하다
제일 긴 구간을 고르는게 최선의 답이 아니다

수를 선택하고 오른쪽 증가하는 방향으로 구간을 정하는것이 유리하다
즉 왼쪽방향의 구간은 쓰잘데기 없는 구간이다
커버하지도 않는다

그 뒤에 조금이라도 이득을 볼것이다 그리디하게
그렇게 오른쪽방향으로 가장 긴 구간을 선택하면
나머지 남아있는 원소들이 이 구간에 포함될 가능성이 높아지기 때문이다
물론 가능성은 잇지만 항상 그렇지는 않다
즉 자기자신만 커버된다고하더라도 최선을 선택한것이기때문에
그것으로 정답에 도출하는데 최선임이 자명하다
이러한 부분을 K개숫자 반복해주면 된다

이러한 과정이 어떻게해야 구간의 필요한 최소갯수를 구하는 방법이다
전형적인 그리디 어려운 문제

어떤 구간을 선택할지 빠르게 구해야만 한다라는 과제가 남아있다
x를 정할때마다 모든 구간을 순회해버리면
N^3이 되서 시간초과가 난다
O(KLogK + K + Q)

k개를 정렬하는것이 필요하다
즉 가장 왼쪽숫자부터 커버하려고 하기때문에
정렬해야한다
정렬하기전에 구간들도 정렬한다 (정렬기준은 시작점 기준으로 정렬할것이다)
구간들이 알아서 정렬되어 있을것이다
구각의 시작점기준으로 정렬한다(전처리)
왼쪽부터 차례대로 보면서 x를 정하고
x부터 k개를 선택하여 정렬한다 (KLogK)
이제 정렬된 첫번째구간을 포인터 p로 가리킨다
1번숫자를 타겟으로 결정함
1번x보다 온쪽에 있는 구간들을 전부 선택한다
p번구간이 시작점이 x보다 왼쪽에 있더라
이 친구는 r까지 커버가 되더라
p는 다음으로 가리킨다
내가 기억하고 있는 r보다 짧으니 필요가 없더라(갱신되지 않음)
그다음 P가 가리킨다 어 내가 기억하고 있는 r보다 크네?
갱신한다
근데 나를 포함하지 않는구간은 버린다 이제
그렇게 반복하다보면 r이라는 구간을 선택하게 된다
이제 x다음 원소인 두번째원소를 선택하고
r보다 크나? 작으면 더이상구간을 선택할 필요가 없더라
그당 원소도 본다 r보다 커? 크면 새로운 구간을 하나 필요로 하므로
위의 과정을 반복한다
이렇게 반복하면서 앞의 구간들은 볼 필요가 없다
현재 가리키고있는 p포인터가
구간을 기억하고 있기때문에
불필요한 구간을 보지 않도록 한다


"""

import sys

si = sys.stdin.readline
N, K, Q = map(int, si().split())  # N: 수 개수, K: 연속 부분 수열 길이, Q: 구간 개
a = list(map(int, si().split()))  # N 개의 수 입력
intervals = [tuple(map(int, si().split())) for _ in range(Q)]  # 구간 입력
intervals.sort()  # 구간 정렬 => 핵심이다


def solve(nums):  # nums 를 모두 커버하는 최소 구간 개수, O(K + Q)
    R = nums[0] - 1  # 이전에 커버된 제일 오른쪽 위치
    P = 0  # 탐색을 시작할 구간의 번호 => 포인터 활용 => tle 줄이기
    ret = 0  # 선택한 구간 개수
    for x in nums:  # O(K)
        if x <= R:  # 이미 x가 커버된 상태야?
            continue
        # 숫자 x를 포함하는 구간을 찾는 반복문
        while (P < Q and  # 구간이 남아있어?, O(Q)
               intervals[P][0] <= x and  # 구간이 x 이하에서 시작해?
               R < x):  # 아직 x가 커버 안됐어?
            R = max(R, intervals[P][1])  # 커버되는 제일 오른쪽 위치 갱신하기
            P += 1  # 다음에 보아야 하는 구간 번호 가리키기
        ret += 1  # 구간 한 개 더 사용했다고 표시하기

    return ret


ans = Q
for i in range(N - K + 1):
    new_nums = sorted(a[i: i + K])  # O(K log K) => 핵심이다
    ans = min(ans, solve(new_nums))  # O(K + Q) => 이미 커버된 숫자는 건너뛰고 쿼리문도 시작숫자가 현재숫자보다 작다면 건너뛰므로 K+Q가 된다
print(ans)  # O(N * (K * logK + K + Q))