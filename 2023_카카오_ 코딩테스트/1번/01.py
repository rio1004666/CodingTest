"""

이 문제를 푸는 방법

딕셔너리 , int() 함수 => 문자를 함수로 변경

문자열로 들어오는 숫자들은 보통 일수로 변경한다 ( 관찰 )

달수로 계산하면 개꼬인다

2021.05.02 =>  (2021 * 12 * 28) + (5 * 28) + 2
"""
# 년월일을 일수로 변환하는 함수 ( 2000년을 빼주는 작업 )
def myDays(ymd):
    y,m,d = ymd.split('.')
    y = int(y)
    m = int(m)
    d = int(d)
    y -= 2000
    return (y*12*28) + (m*28) + d

def solution(today, terms, privacies):
    answer = []
    myterms = {}
    today = myDays(today)
    for term in terms:
        t,months = term.split(' ')
        myterms[t] = int(months) * 28
    for idx in range(0,len(privacies)):
        ymd, t = privacies[idx].split()
        days = myDays(ymd)
        if days + myterms.get(t) <= today:
            answer.append(idx + 1)
    return answer