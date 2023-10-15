# BOJ_11047_동전 개수의 최솟값 구하기
# 난이도: 실버3
# 풀이 날짜: 23.10.15
# 풀이 시간: 약 10분

# How to
"""

"""

# Comment
"""
남은 동전을 갱신할 때 나머지 연산을 사용하는 게 더 깔끔한 것 같다.
"""

# Code
import sys

N, K = map(int, sys.stdin.readline().split())
coin_list = [int(sys.stdin.readline().strip()) for _ in range(N)]

cnt = 0
rest_money = K
for c in coin_list[::-1]:
    cnt += rest_money // c
    rest_money -= (c * (rest_money // c))
    if rest_money == 0:
        break

print(cnt)


## 메모리: 31120 KB, 시간: 44 ms
