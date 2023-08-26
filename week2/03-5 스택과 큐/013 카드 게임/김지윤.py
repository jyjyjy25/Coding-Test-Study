# BOJ_2164_카드 게임
# 난이도: 실버4
# 풀이 날짜: 23.08.27
# 풀이 시간: 약 12분

# How to
"""
1. i가 홀수일 땐 가장 위의 카드를 버린다.
2. i가 짝수일 땐 가장 위의 카드를 가장 아래로 옮긴다.
3. queue의 길이가 1이 될 때까지 반복한다.
"""

# Comment
"""
queue를 사용할 땐 시간 초과를 방지하기 위해 deque 라이브러리를 사용하는 것이 필수적인 것 같다.
queue.insert(0, queue.pop()) -> queue.appendleft(queue.pop())로 바꿨을 뿐인데 시간 초과 문제가 해결됐다.
아 그리고 교재에서는 가장 위의 카드를 버리고 가장 위의 카드를 가장 아래로 옮기는 과정을 한 번에 처리했는데,
길이가 1일 때 가장 위의 카드를 가장 아래로 옮기는 과정은 아무 변화를 주지 않기 때문에 한 번에 처리해도 상관 없는 것 같다.
"""

# Code
import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for i in range(N, 0, -1):
    queue.append(i)

i = 0
while (1):
    if len(queue) == 1:
        break

    i += 1
    if i % 2 == 1:
        queue.pop()
    else:
        queue.appendleft(queue.pop())

print(queue.pop())


## 메모리: 51028 KB, 시간: 364 ms