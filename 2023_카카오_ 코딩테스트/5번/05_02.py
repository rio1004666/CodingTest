"""
1. 문제이해

   표 편집 프로그램

   표의 크기는 50 x 50 고정

   1) 모든 셀 비어있음 초기화
   2) 각 셀 문자열 값 가질 수 있다
   3) 다른 셀과 병합 가능
   4) 행 : r , 열 : c

   기능 구현(명령어)

   UPDATE r c value (특정값 입력 or 변경)
   UPDATE value1 value2 (특정값 모두 변경)
   MERGE r1 c1 r2 c2 (병합)
   UNMERGE r c (병합해제)
   PRINT r c (값 출력)

2. 관찰

   우선 50 x 50 으로 상당히 셀수가 적다 (핵심)
   그렇다면 셀하나씩 정보를 관리하는것은 어떨까? 총 2500개의 셀
   또 명령어도 1000개로 아주 작다 (핵심)

   핵심은 Merge와 unmerge를 어떻게 표현할 것인가????
   union-find가 가장 이상적이긴하지만 수가 매우 적으므로 굳이 안써도 된다
   그럼 merge된것은 한 그룹이라는 표시를 적어주어야한다

   2차원격자로 그대로 표현하게 된다면 어떤것이 합병됬는지 unmerge할 때 문제가 된다
   병합된셀이라는 표시를 하기 위해 merged[][] 2차원 배열을 만든다
   셀이 같은 값이라면 병합되었다고 표시하는게 맞는데

   그런데 같은값이라고 해서 병합되었다고 볼 수 없다고 생각하여 이 생각을 접었는데...?

   아 역시 문자열이 같다고 하면 키가 될 수 없기때문에 (i,j) 위치를 키로 잡아서 병합시키면 된다
   그리고 merge & unmerge를 할때마다 2차원 전체격자를 돌 때가 있는데 2500개가 최대이며
   모든 명령어를 merge한다고 하더라도 충분히 시간안에 들어올 수 있다

3. 시간복잡도 계산

   명령문 1,000개 x 2,500(50x50개의 격자) = 2,500,000


"""
def solution(commands):
    """    유니온 파인드 사용하지 않은 경우 2"""
    answer = []
    R,C = 51,51
    # value table
    board = [["EMPTY"  for c in range(C)] for r in range(R)]
    # merged value table
    merged = [[(r,c) for c in range(C)] for r in range(R)]

    def update(rt,ct,value):
        for i in range(R):
            for j in range(C):
                if merged[i][j] == (rt,ct):
                    board[i][j] = value
    def replace(value1,value2):
        for r in range(R):
            for c in range(C):
                if board[r][c] == value1:
                    board[r][c] = value2
    def merge(r1,c1,r2,c2):

            # r2,c2를 r1,c1에 병합합니다.
        rt,ct = merged[r1][c1]
        rt2,ct2 = merged[r2][c2]

        if board[rt][ct] == "EMPTY":
            board[rt][ct] = board[rt2][ct2]

        for r in range(R):
            for c in range(C):
                if merged[r][c] == (rt2,ct2):
                    merged[r][c] = (rt,ct)
    def unmerge(sr,sc,rt,ct,v):
        for r in range(R):
            for c in range(C):
                if merged[r][c] == (rt,ct):
                    merged[r][c] = (r,c)
                    board[r][c] = 'EMPTY'

        board[sr][sc] = v
    def output(rt,ct):
        answer.append(board[rt][ct])

    for command in commands:
        data = str(command).split(' ')
        cmd = data[0]
        if cmd == 'UPDATE':
            # 좌표와 값이 주어진다면 해당 셀을 업데이트 친다
            if len(data) == 4:
                r,c,value = int(data[1]), int(data[2]), data[3]
                rt,ct = merged[r][c] # 병합된 좌표들만 관리한다
                # board[rt][ct] = value # 그 값만 변경하면 나머지 병합된 셀들의 값들도 같이 불러온다
                # 셀하나를 선택했을 경우 병합된셀 모두가 선택된다
                update(rt,ct,value)
            # 값 두개를 준다면 지정한 값의 셀들에 새로운 값을 업데이트한다
            else:
                value1,value2 = data[1],data[2]
                replace(value1,value2)
        # 병합하라고 하면
        elif cmd == 'MERGE':
            r1,c1,r2,c2 = int(data[1]), int(data[2]), int(data[3]), int(data[4])
            if r1 == r2 and c1 == c2:
                continue
            merge(r1,c1,r2,c2)

        elif cmd == 'UNMERGE':
            sr,sc = int(data[1]),int(data[2])
            rt,ct = merged[sr][sc]
            v = board[rt][ct]
            unmerge(sr,sc,rt,ct,v)

        elif cmd == 'PRINT':
            r,c = int(data[1]), int(data[2])
            rt,ct = merged[r][c]
            output(rt,ct)

    return answer
