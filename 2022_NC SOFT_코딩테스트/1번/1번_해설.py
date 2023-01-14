# 1. 이상한 나라에는 소문자 알파벳 존재 - 이 알파벳은 이 나라에서 정해주는 알파벳 순서가 있다
#    단어가 주어졌을때 이상한 나라의 알파벳 순서에 맞게 사전순으로 정렬하는 것
# 예를 들어 이상한 나라에서 정해주는 알파벳 순서는 첫번째가 p 두번째가 d 세번째가 u .... 이런 방식으로 원래는 a,b,c,d...가 순서지만 P가 a에 해당하는 첫번째순서라는것
# 그래서 여기서 해설자는 p를 a로 바꿔주고 d를 b로 바꿔주고 u를 C로 바꿔주면
# 정렬했을때 사전순으로 정렬되므로 다시 그 변환된것을 되돌려주면 이상한 나라에서 정해준 알파벳 순서가 된다!

import sys
si = sys.stdin.readline
alphabets = si().split()
n = int(si())
words = [si().strip() for _ in range(n)]
new_words = []
mems = list('abcdefghijklmnopqrstuvwxyz')
def convert(alphabets, x):  # O(1)
    # 이상한 나라에서의 x 문자가, 현재 세상에서는 어떤 문자랑 같은 지 알려주는 함수
    for a, b in zip(alphabets, mems):
        if a == x:
            return b
def rollback(alphabets, x):
    # 현재 세상에서 x 문자가, 이상한 나라에서 어떤 문자랑 같은 지 알려주는 함수
    for a, b in zip(alphabets, mems):
        if b == x:
            return a
for word in words:
    new_word = ""
    for c in word:
        new_word += convert(alphabets, c)
    new_words.append(new_word)
new_words.sort()
for new_word in new_words:
    for c in new_word:
        print(rollback(alphabets, c), end='')
    print()