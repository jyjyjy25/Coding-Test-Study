# BOJ_11047_동전 0
# 난이도: 실버3
# 풀이 날짜: 23.10.15
# 풀이 시간: 10분

# How to


# Comment
# 그리디의 개념 자체가 이해가 잘 안 가서 블로그 찾아봤는데
# 놀랍게도 그리디를 설명하는 예시로 동전 문제를 들어줘서 흐름을 잡기 좋았다

# Code
import sys
n, k = map(int, sys.stdin.readline().strip().split(' '))
arr = list(int(sys.stdin.readline()) for _ in range(n))

count = 0
for i in range(n-1, -1, -1):
    if arr[i] <= k:
        count += k//arr[i]
        k %= arr[i]

print(count)

## 메모리:  31120KB, 시간:  40ms