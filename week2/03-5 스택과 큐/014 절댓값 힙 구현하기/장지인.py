# BOJ_11286_절댓값 힙
# 난이도: 실버1
# 풀이 날짜: 23.08.27
# 풀이 시간: 1시간

# How to
'''
1. 우선순위 큐에 절댓값을 기준으로 정렬하고, 숫자 크기대로 정렬하도록 한다.
2. x가 무엇인지에 따라 다음같이 수행한다.
   - x == 0: 우선순위 큐의 맨 앞의 내용을 출력한다. 만약 큐가 비어있으면 0을 출력한다.
   - x != 0: 우선순위 큐에 넣는다.
'''

# Comment
'''
30분가량 고민 후 교재를 보고 풀었다.
내가 생각했던 건 매번 정렬하면서 queue에 넣는거였는데,, 정렬을 어떻게 하느냐가 쉽지 않았다.
또 음수를 저장하는 queue와 양수를 저장하는 queue를 나누는 것도 고려했으나....

우선순위 큐를 처음봐서 매우 생소했다.
이해하기로는 0번 인덱스에 들어가는 값이 우선순위이고, 1번 인덱스가 값이다.
우선순위를 기준으로 정렬하도록 할 수 있으며, 기본적으로도 숫자의 순서대로 들어가는 것 같다.
조건이 여러개면 어떤가 궁금해서 맨 밑에 실험을 해보았다.
'''

# Code

from queue import PriorityQueue
import sys
input = sys.stdin.readline
N = int(input())

queue = PriorityQueue()

for _ in range(N):
    x = int(input())

    if x == 0:
        if queue.empty(): print(0)
        else: print(queue.get()[1])

    else:
        queue.put((abs(x), x))

## 메모리: 44032 KB, 시간: 284 ms

# 우선순위 큐에 관하여,,
'''
from queue import PriorityQueue

queue = PriorityQueue()

queue.put((0, 5, 1))
queue.put((2, 3, 5))
queue.put((2, 3, 4))
queue.put((1, 4, 2))
queue.put((2, 1, 8))
queue.put((2, 1, 1))

while(queue.not_empty):
    print(queue.get())

# print 결과

# >> (0, 5, 1)
# >> (1, 4, 2)
# >> (2, 1, 1)
# >> (2, 1, 8)
# >> (2, 3, 4)
# >> (2, 3, 5)
# item의 개수에 상관 없이 정렬을 해주는 것을 확인할 수 있었다.
'''