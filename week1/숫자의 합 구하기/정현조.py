# BOJ_11720_숫자의 합
# 난이도: 브론즈5
# 풀이 날짜: 23.08.19
# 풀이 시간:

# How to
# for문 돌리면서 sum 변수에 하나씩 더하는 방식

# Code
import sys
n = int(sys.stdin.readline())
number = list(sys.stdin.readline().strip())

sum = 0
for i in range(n):
    sum += int(number[i])

print(sum)

## 메모리:  31256KB, 시간:  44ms
