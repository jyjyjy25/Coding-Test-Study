# BOJ_11286_절댓값 힙 구현하기
# 난이도: 실버 1
# 풀이 날짜: 23.08.27
# 풀이 시간: 27분

# How to
"""
1. n 값을 입력받는다.
2. 반복문을 돌면서 값을 입력받아 heappush()한다.
    이때 튜플 타입이 heapq(최소 힙) 특성에 따라 첫 번째 요소를 기준으로 heap이 정렬된다.
    즉, 튜플의 첫 번째 요소를 절댓값으로 입력하면 절대값을 기준으로 heap을 정렬 할 수 있다.
3. 힙이 비어있는 상태에서 heappop()을 하려고 하면 오류가 발생한다.
    try-except 문으로 에러 발생 시 0을 출력한다.
"""

# Comment
"""
- 우선순위 알고리즘 heap que를 사용했다.
    https://docs.python.org/ko/3/library/heapq.html
    - heappush(heap, item) : 힙 불변성을 유지하면서 item을 heap으로 푸시한다.
    - heappop(heap) : heap에서 가장 항목을 pop 하고 반환한다.
"""

# Code

import sys
import heapq

num = int(input())
heap = []

for _ in range(num):
    num = int(sys.stdin.readline())

    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)


## 메모리: 39960 KB, 시간: 148 ms