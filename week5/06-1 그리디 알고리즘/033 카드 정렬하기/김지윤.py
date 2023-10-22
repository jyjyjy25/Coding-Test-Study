# BOJ_1715_카드 정렬하기
# 난이도: 골드4
# 풀이 날짜: 23.10.15
# 풀이 시간: 약 25분

# How to
"""
시간 복잡도를 줄이기 위헤 heapq를 사용해야 한다.
또한 해당 문제의 주요 포인트는 "합친 두 카드 묶음을 카드 리스트에 넣고 다시 정렬을 수행해야 한다"는 점이다.
"""

# Comment
"""
이 문제 10달 전에도 풀어봤던데.. 똑같이 풀어서 틀렸다 ㅋㅋ;
heapq를 사용하는 법을 알면 금방 풀 수 있는 것 같다.
"""

# Code
import sys
import heapq

N = int(sys.stdin.readline().strip())

cards = []
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    heapq.heappush(cards, x)

cnt = 0
while len(cards) >= 2:
    temp_card = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, temp_card)
    cnt += temp_card

print(cnt)

"""
# 시도 1: 시간 초과

import sys

N = int(sys.stdin.readline().strip())
cards = [int(sys.stdin.readline().strip()) for _ in range(N)]

cnt = 0
while len(cards) >= 2:
    cards.sort()
    cnt += cards[0] + cards[1]
    cards.append(cards[0]+cards[1])
    cards = cards[2:]

print(cnt)
"""

## 메모리: 33972 KB, 시간: 184 ms