# <<  남은 1 찾기 >>
# 격자 형태의 이차원 배열(n * n)이 주어진다. 이차원 배열은 각각 0, 1, 2라는 값을 가질 수 있다.
#
# 거리 m이 주어진다. 1 위치에서 m 거리 안에 2가 있으면 삭제하지 않는다. 없으면 삭제한다. 거리는 상하좌우 인접하게 칸으로 이동하면 1로 생각한다.
#
# 남아있는 1의 개수를 출력한다.
#
# 입력은 n, m이 주어지고 n * n으로 이차원 배열이 주어진다.
#
# n -> 100 이하
# 입력 예시 --
# 4 2
# 2 0 0 1
# 2 0 0 1
# 2 0 0 1
# 0 0 0 1
# 출력 예시 --
# 0
#
# 입력 예시 --
# 4 2
# 0 2 0 1
# 0 2 0 1
# 0 0 0 0
# 2 0 0 1
# 출력 예시 --
# 2
#
# 관철 값이 1인 좌표에에서 2가있는 좌표들사이의 거리가 m이하가 하나라도 있다면 그 1은 삭제한다
#
# N  = 100이고 n^2 = 10000이므로 1이 5000개 2가 5000개면  ⇒ 2500만이 최대이므로 가능하다
#
# → 거리가 m이하 ⇒ 포인트 각 1인 좌표들 각각에 대하여 2의 좌표들을 하나씩 체크하며 맨하튼 거리를 체크해서 m이하가 하나라도 있다면 제거대상으로 카운팅을 한다
#
# 전체 갯수에서 삭제할 1의 갯수를 빼면 남아있는 1의갯수가 된다