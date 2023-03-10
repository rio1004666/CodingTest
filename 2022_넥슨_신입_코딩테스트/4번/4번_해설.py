"""

이문제를 풀정도면 통찰력이 좋다
수열이 주어지면 최대한 쪼갤것이다
최대한 쪼개서 쪼개진 각각의 부분수열들이 있을것이다
각각 수열끼리 정렬했을 때 다시 전체를 이어 붙였을때 결과와
전체에서 정렬을 해서 구한 결과와 같은 결과가 나올떄까지
최대한 많이 쪼개고 싶다 ( 최대 몇번 쪼갤수 있느냐 )

예를들어

2 1 3 2 4 4 5 8 7 7 이라는 수열이 있다면
2 1 / 3 2 / 4 / 4 / 5 / 8 7 7 이렇게 6개로 쪼개면 각각 수열을 정렬한것과 전체 정렬했을 때의 결과가 같다

그럼 정답은 6개이다 N <= 10만 이다
각 원소의 범위도 10만

문제이해

관찰 - i 와 i+1을 쪼갤 수 있냐 없냐를 관찰
그게 합법일까? 어떤 곳을 쪼갤때
왼쪽과 오른쪽은 완전 다른 배열로 되서 정렬이기 때문에
그럼에도 불구하고 전체가 정렬된다는것과 같다는것은
왼쪽애들은 정렬을 하더라도 이동하는 인덱스가 i보다 작거나 같아야한다
즉 정렬하게 되면 오른쪽으로 넘어가는 친구가 하나라도 있으면 못자른다
1 7 3 5 8 이라는 배열이 있으면
1 7 3 /  5 8 로 쪼개본다고 가정하자
이것이 되려면 왼쪽정렬은 1 3 7이고 오른쪽은 5 8 인데
일단 전체를 정렬해보면 그렇게 비교를 해보면된다 3과 5사이를 잘라버리면
7은 내가 자른선을 건너야 자기자리로 갈 수 있기때문에 성립하지 않음을 알 수 있다
또 5도 자신의 자리로 갈려면 넘어가야하기때문에 3과 5사이는 절대로 자를 수 없음을 알 수 있다
내가 어딘가를 자를 수 있냐 없냐를 어떻게 결정하느냐
원래 수열 a를 a*로 만들려면 각각의 원소가 어디로 가는지 가리키는 작업을 수행한다
- 이미 정렬된 배열과 비교하며 자르는 기준을 세우자

원소 하나씩 보면서 이떄까지 가장 큰값을 기억하고 있다가 큰 값보다
작으면 그것을 포함해서 자른다
인덱스가 최댓값과 같아지면 그때 자른다
왜냐면 이때까지 최댓값이 현재 내가 바라보고 있는 인덱스와 같아진다면
이때까지 등장했던 원소들은 오른쪽으로 건너갈 일이 없으므로
자르고 정렬해도 된다라는 의미이다

여기서 핵심은 인덱스의 이동이다
정렬전의 인덱스와 정렬후의 인덱스 매칭하여 기록해놓았다가
최댓값을 갱신하면서 자른다


자료구조 알고리즘

구현


"""