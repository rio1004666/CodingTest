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
    """ 유니온 파인드 사용하지 않은 경우 1 """
    def rc2index(r,c):
        return (int(r) - 1) * 50 + int(c) - 1

    def update(p,s):
        old_state = states[p]
        for index in range(length):
            if states[index] == old_state:
                table[index] = s
    def replace(s1,s2):
        for index in range(length):
            if table[index] == s1:
                table[index] = s2
    def merge(p1,p2):
        change = None
        # p1위치의 값이 있고 p2위치의 값이 비어있다면 p1의 값을 가진다
        if table[p1] != 'EMPTY' and table[p2] == 'EMPTY':
            change = table[p1]
        # p1위치의 값이 비어 있고 p2위치의 값이 있다면 p2위치의 값을 가진디
        elif table[p1] == 'EMPTY' and table[p2] != 'EMPTY':
            change = table[p2]
        # p1위치의 값이 있고 p2위치의 값이 있다면 p1위치의 값을 가진다
        elif table[p1] != 'EMPTY' and table[p2] != 'EMPTY':
            change = table[p1]
        # 해당하는 위치의 그룹값을 가져온다
        old_state = states[p2]
        # 그룹값들에 해당하는 것들을 모두 병합한다
        for index in range(length):
            if states[index] == old_state:
                states[index] = states[p1]
        # 병합후
        # change가 변화가 있는 경우에만
        if change:
            for index in range(length):
                if states[index] == states[p1]:
                    table[index] = change
    def unmerge(p):
        old_value = table[p]
        old_state = states[p]
        for index in range(length):
            if states[index] == old_state:
                states[index] = index
                table[index] = 'EMPTY'

        table[p] = old_value
    def print_(p):
        answer.append(table[p])

    def solve():
        for line in commands:
            command, *tokens = line.split()
            if command == 'UPDATE':
                if len(tokens) > 2:
                    update(rc2index(tokens[0],tokens[1]),tokens[2])
                else:
                    replace(tokens[0],tokens[1])
            elif command == 'MERGE':
                merge(rc2index(tokens[0],tokens[1]), rc2index(tokens[2],tokens[3]))
            elif command == 'UNMERGE':
                unmerge(rc2index(tokens[0],tokens[1]))
            elif command == 'PRINT':
                print_(rc2index(tokens[0],tokens[1]))

    length = 2500
    answer = []
    # 2차원배열로 표현하기보다 1차원배열로 표현하여 편하게 구현
    table = ['EMPTY'] * length # 실제 값을 업데이트 및 병합 및 병합해제 하는 1차원 배열
    states = list(range(length)) # 병합하여 같은 그룹인지 나타내는 1차원 배열
    solve()


    return answer
