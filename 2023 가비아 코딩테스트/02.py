"""
메이플 스토리
랭킹 페이지
페이지네이션 되어 있고
1페이지에는 1등부터 k등까지만 보임
1등 레벨 255
2등 레벨 254
3등 레벨 253
4등 레벨 251...

이벤트로 아이디와 레벨이 주어지면
어떤 아이디 가진 사람이 어떤 레벨을 달성하여 랭킹표에 있다
이벤트가 최대 1000번 까지 들어옴
1페이지에 몇번이나 변동이 생기는지 구하기
1페이지에 레벨이 보이지 않고 이름만 보인다고 함
k <= 100
k와 이벤트수가 값이 작기 때문에
의도하는바는 이벤트가 들어올 때마다 정렬을 매번한다 nlogn
이전상태 정렬결과와 새로운 랭킹결과와 비교해서 아이디가 다른게 존재하는지 확인하면 끝

굳이 전체를 정렬하나? 라는 생각이 들 수 있다

k명만 알면되니까 1등부터 N등까지 다 구해서 k등만 가져와도 되지만
k등까지만 정렬하고 나머지는 정렬안해도 됨 -> 힙정렬하기
n자체가 충분히 작기떄문에 굳이 힙정렬안해도 되긴한다

"""
import sys

si = sys.stdin.readline
Q, K = map(int, si().split())
ans = 0
topK = []
records = dict()  # key: 이름, value: (달성 순서, 최고 점수)
for i in range(Q):
    name, score = si().split()
    score = int(score)
    prev_score = 0
    if name in records:
        prev_score = records[name][1]
    if prev_score < score:  # 더 높은 점수를 얻었다면 갱신하기
        records[name] = (i, score)
    arr = sorted([(v[1], -v[0], k) for k, v in records.items()], reverse=True)  # 점수 내림차순, 같으면 달성한 순서 오름차순 정렬하기

    new_topK = [v[2] for v in arr[:K]]
    if topK != new_topK:  # 기존 랭킹과 새로운 랭킹 비교하기
        ans += 1

    topK = new_topK  # 기존 랭킹 업데이트하기
print(ans)