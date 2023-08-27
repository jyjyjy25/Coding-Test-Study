# BOJ_11659_구간 합 구하기4
# 난이도: 실버3
# 풀이 날짜: 23.08.19
# 풀이 시간:

# How to
# testCase마다 반복문 돌고 그 안에서 다시 반복문으로 합을 구함함

# Code
import sys #시간초과..
line1 = sys.stdin.readline().strip().split(' ')
n = int(line1[0])
m = int(line1[1])

number = sys.stdin.readline().strip().split(' ')
number = list(map(int, number))

for i in range(m):
    rangeline = sys.stdin.readline().strip().split(' ')
    start = int(rangeline[0])
    end = int(rangeline[1])+1

    sum = 0
    for j in range(start, end, 1):
        sum += number[j-1]
    print(sum)

## 메모리:  KB, 시간:  ms