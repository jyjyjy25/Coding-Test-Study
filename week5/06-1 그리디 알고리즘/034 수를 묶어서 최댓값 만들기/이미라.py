# BOJ_1744_수 묶기
# 난이도: 골드 4
# 풀이 날짜: 23.10.15
# 풀이 시간: 63 분

# How to
"""
1. n을 입력받는다.
2. n개의 데이터를 입력받을 때, 양수는 posPQ, 음수는 negPQ, 1은 count1, 0은 count0에 저장한다.
    이때 우선순위 큐를 사용하므로 내림차순 정렬을 위해 양수는 * -1 하여 저장해준다.
3. posPQ.qsize() > 1 일 때,
    1, 2번째 값을 곱해서 sum에 더한다.
4. posPQ.qsize() > 0 일 때 (posPQ가 홀수 일 때 나머지 값을 그냥 더한다.),
    posPQ의 마지막 값을 * -1 하여 sum에 더한다.
5. negPQ.qsize() > 1 일 때,
    1, 2번째 값을 곱해서 sum에 더한다.
6. negPQ.qsize() > 0 일 때 (negPQ가 홀수 일 때),
    zero == 0이라면, (zero가 하나도 없다면 그대로 나머지 값을 더한다.)
    posPQ의 마지막 값을 sum에 더한다.
    + 만약 zero가 0이 아니라면 남은 값과 곱하면 0이 되므로 더할 필요가 없다.
"""

# Comment
"""
- 교재를 참고했다.
- 그리디 너무 어렵다...
"""

# Code
from queue import PriorityQueue

n = int(input())
posPQ = PriorityQueue()
negPQ = PriorityQueue()
count1 = 0
count0 = 0

for i in range(n):
    data = int(input())

    if data > 1:
        posPQ.put(data * -1)
    elif data == 1:
        count1 += 1
    elif data == 0:
        count0 += 1
    else:
        negPQ.put(data)

sum = 0

while posPQ.qsize() > 1:
    first = posPQ.get() * -1
    second = posPQ.get() * -1
    sum += first * second

if posPQ.qsize() > 0:
    sum += posPQ.get() * -1

while negPQ.qsize() > 1:
    first = negPQ.get()
    second = negPQ.get()
    sum += first * second

if negPQ.qsize() > 0:
    if count0 == 0:
        sum += negPQ.get()

sum += count1

print(sum)

## 메모리: 37884 KB, 시간: 100 ms
