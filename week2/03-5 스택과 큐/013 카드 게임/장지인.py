# BOJ_2164_카드2
# 난이도: 실버4
# 풀이 날짜: 23.08.27
# 풀이 시간: 5분

# How to
'''
1. deque를 선언하고 1부터 N까지의 수를 순서대로 넣어준다.
2. deque의 길이가 1이 될 때까지 다음을 반복한다.
   - popleft()를 통해 하나를 버린다.
   - popleft()를 한번더 함과 동시에 바로 deque에 다시 넣어준다.
3. 마지막으로 남은 수 하나를 print한다.
'''

# Comment
'''
deque를 이용하면 어렵지 않고 간편하게 풀 수 있다.
'''

# Code

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

dq = deque([i for i in range(1, N+1)])

while (len(dq) > 1):
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())

## 메모리: 55100 KB, 시간: 232 ms