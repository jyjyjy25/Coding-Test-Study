# BOJ_10986_나머지 합
# 난이도: 골드3
# 풀이 날짜: 23.08.16
# 풀이 시간:

# How to

# 그냥 보이는대로 문제를 풀었을 때 시간초과 오류 발생
# 부분 합 개념을 이용해서 해결(코드 참고)

# Code

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

remain_idx = [0 for _ in range(m)]
remain_idx[0] = 1

total = 0
for i in range(n):
    total += num_list[i]
    remain_idx[total % m] += 1

count = 0
for i in remain_idx:
    count += i * (i - 1) // 2

print(count)

## 메모리: 153780 KB,  시간: 608 ms