# BOJ_10986_나머지 합합
# 난이도: 골드3
# 풀이 날짜: 23.08.19
# 풀이 시간:

# How to
# 1. i번째 수부터 j번째 수까지 배열을 잘라 합을 구함
# 2. 그 합이 m으로 나누어 떨어진다면 count +1

# Code
import sys #시간 초과
line1 = sys.stdin.readline().strip().split(' ')
n = int(line1[0])
m = int(line1[1])

number = sys.stdin.readline().strip().split(' ')
number = list(map(int, number))

count = 0
for i in range(n-1):
    for j in range(n, i, -1):
        arr = number[i:j]
        result = sum(arr)
        if(result%m==0):
            count += 1
print(count)

## 메모리:  KB, 시간:  ms