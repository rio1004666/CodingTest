"""
2차원 배열을 뒤집는 행위
좌우반전   행 : i 열 : n-1-j
상하반전   행 : n-1-i 열 : j

보통 같은 행위 동작은 함수를 사용한다
"""

import sys
si = sys.stdin.readline
n = int(si())
a = [list(map(int, si().split())) for _ in range(n)]

def lr_flip(a): # 좌우반전
    b = [[0 for _ in range(n)] for _ in range(n)] # 뒤집을 배열 저장
    for i in range(n):
        for j in range(n):
            b[i][n-1-j] = a[i][j]
    return b
def ud_flip(a): # 상하반전
    b = [[0 for _ in range(n)] for _ in range(n)]  # 뒤집을 배열 저장
    for i in range(n):
        for j in range(n):
            b[n-1-i][j] = a[i][j]
    return b

a1 = a
a2 = lr_flip(a)
a3 = ud_flip(a)
a4 = lr_flip(a3)

for i in range(n):
    print(*(a1[i]+a2[i]))
for i in range(n):
    print(*(a3[i] + a4[i]))