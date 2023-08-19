# BOJ_11720_숫자의 합
# 난이도: 골드1
# 풀이 날짜: 23.08.17
# 풀이 시간:

# How to


# Code

import sys

n = int(input())
num = list(map(int, input()))

result = 0

for i in num:
    result += i

print(result)

## 메모리: 31256 KB, 시간: 44 ms