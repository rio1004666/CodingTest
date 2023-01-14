# 각 날짜별로 카카오페이를 이용해 물품을 구매한 고객들의 id가 문자열 형태로 담긴 배열
# 고객 한명당 받을 수 있는 최대 쿠폰수 k가 매개변수
# 각 고객이 할인쿠폰을 몇장받았는지 기록하는 딕셔너리?
# 아이디가 알파벳 대문자나 이름이므로
# 같은날에 여러번구입해도 한번만취급하게 하는것은 셋트 자료구조로 털자
from collections import defaultdict
def solution(id_list, k):
    answer = 0
    id_dict = defaultdict(int)
    for record in id_list:
        person_list = record.split()
        person_set = set(person_list)
        for person in person_set:
            if id_dict[person] < k:
                id_dict[person] += 1
    for name , coupon in id_dict.items():
        answer += coupon
    return answer