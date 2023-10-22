# BOJ_1715_카드 정렬하기
# 난이도: 골드 4
# 풀이 날짜: 23.10.15
# 풀이 시간: 28 분

# How to
"""
1. n, pq를 입력받는다.
2. pq에 값이 하나 남을 때까지 반복문을 실행한다.
    PriorityQueue의 자동 정렬에 따라 2개의 카드를 뽑을 수 있다.
    2개의 카드의 값을 더하고 더한 값을 다시 pq에 저장한다.
3. 결과를 출력한다.
"""

# Comment
"""
- 교재를 참고했다.
- 사용된 코드 정리
    - PriorityQueue: 우선순위 큐, 내부는 heap으로 구성,
        데이터가 들어오면 데이터의 우선순위를 결정하고 우선순위가 높은대로 데이터가 먼저 나가는 자료구조,
        설정이 없으면 오름차순으로 정렬됨, 튜플(우선순위, 값) 형태로 저장 가능 
    - pq.put(): PriorityQueue의 원소 추가 함수
    - pq.get(): PriorityQueue의 원소 삭제 함수 (pop과 비슷하게 삭제하면서 원소를 리턴함)
"""

# Code
from queue import PriorityQueue

n = int(input())
pq = PriorityQueue()

for _ in range(n):
    pq.put(int(input()))

data1 = 0
data2 = 0
sum = 0

while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()

    sum += data1 + data2
    pq.put(data1 + data2)
    
print(sum)

## 메모리: 37692 KB, 시간: 4692 ms
