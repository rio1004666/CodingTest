"""
1. 문제이해
   카카오톡에서 이모티콘 무제한 가입자수 증가 목표
   1) 가입자수 최대 증가
   2) 판매액 최대 증가
   1번목표 다음 2번 목표

   이모티콘 할인행사

   - n명의 카카오톡 사용자들에게 이모티콘 m개를 할인하여 판매
   - 이모티콘마다 할인율은 다르다 할인율 10,20,30,40% 중 하나 설정

   카카오톡 사용자 이모티콘 구매 패턴

   - 일정비율 이상 할인하는 산다
   - 구매비용의 합이 일정가격이상이 되면 구매 모두 취소후 무제한에 가입

2. 관찰

   제한조건에 사용자수도 100명 제한
   이모티콘개수가 7개 제한

   완전탐색을 생각해볼 수 있다

   각 이모티콘별로 할인율이 다르게 적용된다 => 10,20,30,40% 중 하나로 적용된다

   각 이모티콘 4^7로 경우의 수를 생각해볼 수 잇따

   예를들어 이모티콘 각각

   이모티콘 할인 경우의 수 1.

   1번 10% / 2번 20% / 3번 30% / 4번 40% / 5번 40% / 6번 20% / 7번 30% 적용한다고 하고



   이모티콘 할인 경우의 수 2.

   또 1번 20% / 2번 20% / 3번 30% / 4번 40% / 5번 40% / 6번 20% / 7번 30% 적용한다고 가정하면

   1번 이모티콘의 할인율이 10%->20%로 변경되고 나머지 그대로여도 경우의 수가 되므로

   각 사용자들이 자신들만의 기준으로 이모티콘을 고른다 (가격일정이상이 되면 서비스에 가입하고 정답에 추가)

   이거 또한 사용자들이 이모티콘을 사서 판매액 계산과 서비스 가입자수를 계산하여
   정답에 업데이트한다 혹은

   모든 경우의 수를 배열에 담아서 정렬할 수 있다 (사용자 가입수, 판매액)형식으로 정렬하면 가장 가입자수가 많    은순서부터 앞에 오고 그다음 판매액이 많은 순서로 정렬되고 가장 앞에 있는 결과가 정답이 된다


   그럼 시간복잡도를 생각해보자

"""
def solution(users, emoticons):

    # 사용자수
    usize = len(users)
    # 이모티콘수
    esize = len(emoticons)
    # 이모티콘 할인율 종류
    discounts = [10,20,30,40]
    # 최종 정답
    answer = [0,0]
    # 증첩함수를 사용하여 불필요한 파라미터 전달을 하지 않도록 한다
    def dfs(cur,emo_collected):
        # 종료조건 : 각 이모티콘의 할인율을 정함
        if cur == esize:
            # 서비스 가입자수 카운팅 변수
            scnt = 0
            # 총 이모티콘 구매 비용
            tmoney = 0
            # 이제 사용자 각자 한명씩 이모티콘을 살지 서비스를 가입할지 여부를 판단하고 판매액도 계산한다
            for i in range(usize):
                ecnt = 0 # 한 사람이 이모티콘을 구매한 개수
                dis = 0 # 한 사람이 이모티콘을 구매했을 때 가격
                for j in range(len(emo_collected)):
                    if emo_collected[j] >= users[i][0]: # 사용자의 할인율 기준이상이 되면 이모티콘을 구매한다
                        ecnt += 1 # 이모티콘을 사서 개수 카운팅합니다.
                        dis += (emoticons[j] - int(emoticons[j] * emo_collected[j] * 0.01)) # 할인하여 계산된 구매비용을 추가합니다.
                # 사용자 각 기준금액 이상이면 서비스에 가입한다
                if users[i][1] <= dis:
                    scnt += 1
                # 기준에 못미친다면 가격을 계산한다
                else:
                    tmoney += dis
            # 여기까지 서비스 가입자 수와 구매액이 계산되었다
            # 이제 최종적으로 정답을 업데이트 한다
            # 이전의 서비스 가입자수보다 크다면 무조건 업데이트 한다
            if answer[0] < scnt:
                answer[0] = scnt
                answer[1] = tmoney
            # 서비스 가입자수가 같다면
            elif answer[0] == scnt:
                # 구매액이 큰것으로 업데이트친다
                if answer[1] <= tmoney:
                    answer[1] = tmoney
            return


        for idx in range(4):
            emo_collected.append(discounts[idx])
            dfs(cur+1,emo_collected)
            emo_collected.pop()

    # 모든 경우의 수를 탐색하는 완전탐색 방법 중 dfs 깊이우선탐색(재귀) 사용한다
    dfs(0,[])


    return answer