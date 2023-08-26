# BOJ_2164_카드2
# 난이도: 실버4
# 풀이 날짜: 23.08.27
# 풀이 시간: 19:32

# How to
# 전에 했던거 생각나서 p 구하는 것만 검증 한번 하고 그대로 함
# 또또 시간초과과

# Comment


# Code
import sys
n = int(sys.stdin.readline())
card = list(range(1, n+1))

p=0
while len(card) != 1:
    p = p % len(card)
    card.pop(p)
    p += 1
print(card[0])
## 메모리:  KB, 시간:  ms