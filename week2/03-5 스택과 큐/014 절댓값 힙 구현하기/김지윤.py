# BOJ_11286_절댓값 힙 구현하기
# 난이도: 실버1
# 풀이 날짜: 23.08.27
# 풀이 시간: 약 26분

# How to
"""
1. PriorityQueue()를 이용한다.
2. (우선순위, 값) 형태로 큐에 저장한다.
    우선순위는 절댓값을 기준으로 하기 위해 정렬 기준을 새로 정의한다.
"""

# Comment
"""
절댓값이 가장 작은 값을 배열에서 제거하는 걸 제일 고민 많이 한 부분인데.. 우선순위 큐를 사용하면 이러한 고민을 할 필요가 없었다.
어쩐지.. 배열의 처음이나 마지막 요소를 제거하는 거면 몰라도 특정 인덱스의 값을 제거하고 이를 업데이트 한 배열을 계속 재사용한다는 게 말이 안됐다.
PriorityQueue() 문법을 찾아보면서 하느라 코드가 책과 거의 똑같다.
"""

# Code
import sys
from queue import PriorityQueue

heap = PriorityQueue()

N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap.empty():
            print(0)
        else:
            print(heap.get()[1])
    else:
        heap.put((abs(x), x))  # 정렬 순위 1) 절댓값 2) 음수

## 메모리: 44036 KB, 시간: 288 ms