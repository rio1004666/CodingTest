# 1번 루트 노드부터 1,2,3 숫자 하나중 떨어뜨린다
# 리프노드까지 간다
# 실선 즉 갈 수 있는 단방향 간선을 타는데 갈 수 있는 자식 노드 번호 중 가장 작은 번호의 자식노드로 떨어진다
# 번호를 떨어뜨리고 난 후 의 경로들을 다시 그보다 큰 노드번호로 재설정합니다.


import sys

si = sys.stdin.readline
# 입력부
n = int(si())
people = list(map(int, si().split()))
children = [[] for _ in range(n)]
for _ in range(n - 1):
    par, child = map(int, si().split())
    # index based on zero
    par -= 1
    child -= 1
    # 단방향일 경우 그래프 트리 생성하기
    children[par].append(child)
# 자식들이 순서대로 입력받지는 않으므로 정렬 필요 -> 경로가 바귈때 그다음 큰 자식노드를 설정하기 위해서
# 전처리부 ( 자료구조 선언부 )
for i in range(n):
    children[i].sort()
# 구슬이 가는 방향을 각 노드마다 그 다음 노드로 가는곳을 가리키는 리스트
road = [0 for _ in range(n)]
# 한번씩 떨어뜨릴때마다 도착하는 노드를 기록하는 리스트
arrive = []  # 도착하는 마을 순서 기록
# 필요한 각 누적점수를 만족해야하는 노드들의 갯수
unsatisfied_count = 0  # 아직 사람이 더 필요한 마을 수
# 마을마다 도착하는 횟수
arrive_count = [0 for _ in range(n)]  # 마을마다 도착한 횟수
# 총 누점점수를 만족해야하는 리프노드들의 갯수
for i in range(n):
    if people[i] > 0:
        unsatisfied_count += 1
# 만족해야하는 노드들을 다 채워야한다면 계속 구슬을 떨어뜨림
# 최대 3을 떨어뜨렸을경우 만족한다면 만족한다고 체크하고 순서를 기록하고 갯수를 저장함 -> 각각의 만족해야하는 노드들을
# 모든 리프노드에 쌓이는 누적점수가 만족될때까지 계속 방문하게 된다 -> 경로가 계속 바귀기 때문이다
while unsatisfied_count:
    x = 0
    while children[x]:
        next_x = children[x][road[x]]
        road[x] = (road[x] + 1) % len(children[x])
        x = next_x

    arrive.append(x)
    arrive_count[x] += 1
    # 3을 떨어뜨렷을 경우 만족하면 만족하는 노드 갯수에서 -1 차감된다
    if (arrive_count[x] - 1) * 3 < people[x] and arrive_count[x] * 3 >= people[x]:
        # x번 마을에 대해 만족된 순간
        unsatisfied_count -= 1
ans = []
# 이제 도착하는 마을 순서들을 돌면서 조정해나간다 => 원래 3으로 다 넣어보고 방문순서를 정했지만 3이 아닌 더 적은수로 채울 수 있기때문이다
for x in arrive:
    # 현재 도착한 마을은 x 번 마을이다
    cnt = 0
    # 문제의 조건에서 가장 적은숫자를 사용하여 그 노드의 누적점수를 만족시키게하는 최소점수를 나열하기 위해 1부터 떨어뜨려본다
    for t in [1, 2, 3]:
        visit = arrive_count[x]  # 남아있는 방문 횟수
        need = people[x]  # 남아있는 사람 수
        last = need - t  # 갔다고 치면 last 사람이 더 필요함

        # visit-1 번 동안 last 만큼의 사람을 보낼 수 있는 지? => 있다면 바로 선택하고 없으면 그 다음 구술을 떨어뜨린다 즉 증가시킨다
        # 위의 경로를 정할때와 마찬가지로 만족하는지 체크하기
        if (visit - 1) * 1 <= last <= (visit - 1) * 3:
            cnt = t
            break
    # 방문 횟수는 아직 남았지만 이미 충족한경우 넘치므로 만족할 수 없음을 의미 => 애초에 경로설정이 되어있음 모두 충족시키기 위해 여러번 방문되기도 하기때문에 즉\
    # 한번만 방문해도 될것을 여러번 방문하게 해서 이미 충족했는데도 초과방문하여서 더 점수를 누적시키게하므로 만족할수없는 점수로 되버림
    if cnt == 0:
        print(-1)
        break
    ans.append(cnt)
    arrive_count[x] -= 1
    people[x] -= cnt
print(*ans)