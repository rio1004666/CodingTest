"""
회사 A,B,C가 있다
각 회사 장학금을 줄 수 있는 자산이 X1,X2,X3 이다
학생 N명이 있다
Y1,Y2,Y3...YN 학생들 각각이 장학금을 필ㅇ로 함
각 학생들은 한 회사에게만 장학금을 받을 수 있다
학생은 8명
학생들이 필요로하는 장학금은 100 한도
회사가 장학금으로 줄 수 있는 돈 100 한도

모든회사가 한도내에서 모든 학생들에게 장학금을 줄 수 있는지 여부 YES or NO

이 문제의 특이한점 회사도 3개 학생수도 8개

숫자가 작은것은 풀이에 도움이 된다

풀이에 떠올릴 수 있는 방법은 완전탐색 시작

이 문제에서 봐야하는 경우란.
학생이 누구한테 투자 받는지를 본다
1번학생이 A,B,C 회사 중 하나한테 받고
2번학생이 A,B,C 회사 중 하나한테 받고
3번학생이 A,B,C 회사 중 하나한테 받고...
n번 학생이 A,B,C 회사 중 하나한테 받게 된다면
3가지의 경우각각에 3가지...3가지 라면 3^8이 된다
이렇게 해서 모든 학생이 회사 자산한도내에서 장학금을 받을 수 있는지 체크
재귀함수로 완전탐색 구현

"""
import sys
from typing import List
si = sys.stdin.readline
N,M,K1,K2,K3 = map(int, si().split())
def solve(needs: List[int],idx:int,lefts:List[int]) -> bool:
    """
    needs : 학생이 원하는 장학금
    idx :  이번에 장학금을 수여할 학생 번호 , 0~(idx-1) 학생들은 수여가 완료되었음
    lefts : 회사들의 잔여 장학금
    return : idx ~ (M-1) 학생들에 마저 장학금을 수여할 수 잇으면 True 아니면 False 를 출력한다
    """
    # 이미 모든 학생들에 수여 완료
    if idx == M:
        return True

    possible = False # possible : 장학금을 줄 수 있는가 초기값은 False
    need = needs[idx] # need : 이번에 수여할 학생이 필요로 하는 장학금 액수

    for k in  range(3): # k번 회사가 수여하는 경우 탐색
        if lefts[k] >= need and not possible: # 수여가 가능하고 , 아직 성공한 케이스가 없다면 탐색하고 성공을 이미 햇다면 더 이상 탐색할 필요도 없다
            # 성공여부만 따지기 때문이다
            lefts[k] -= need # K번 회사 남은 액수 감소
            if solve(needs,idx + 1, lefts): # 남은 학생들에 대한 시도가 성공한다면
                possible = True
            lefts[k] += need # k번 회사 남은돈 다시 복구
    return possible


ans = 0
for _ in range(N):
    needs = list(map(int, input().split())) # 학생들의 필요 장학금 쿼리가 주어짐
    if solve(needs,0,[K1,K2,K3]): # 가능하다면
        ans += 1 # 카운팅
print(ans)
