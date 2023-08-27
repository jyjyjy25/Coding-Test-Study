# BOJ_2164_카드게임
# 난이도: 실버 4
# 풀이 날짜: 23.08.27
# 풀이 시간: 14분

# How to
"""
1. 값을 입력받는다.
2. mydeque의 원소가 1개보다 많을 때,
    a. 맨 앞 원소를 버린다.
    b. 그 다음 원소를 맨 마지막으로 보낸다.
3. 값을 출력한다.
"""

# Comment
"""
- deque를 이용하여 쉽게 풀 수 있었다.
"""

# Code

from collections import deque

n = int(input())
mydeque = deque([i for i in range(1, n + 1)])

while len(mydeque) > 1:
    mydeque.popleft()
    mydeque.append(mydeque.popleft())

print(mydeque[0])

## 메모리: 55008 KB, 시간: 228 ms