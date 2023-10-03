# BOJ_2164_카드2
# 난이도: 실버4
# 풀이 날짜: 23.08.27
# 풀이 시간: 19:32

# How to
# 전에 했던거 생각나서 p 구하는 것만 검증 한번 하고 그대로 함
# 또또 시간초과
# [수정] deque로 하는걸로 바꿨더니 성공!

# Comment


# Code
import sys
from collections import deque
n = int(sys.stdin.readline())
card = deque(range(1, n+1))

while len(card) != 1:
    card.popleft()
    card.append(card.popleft())
print(card[0])
## 메모리:  50936KB, 시간:  224ms