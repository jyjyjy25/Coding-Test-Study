# BOJ_11659_구간 합 구하기1
# 난이도: 실버3
# 풀이 날짜: 23.08.19
# 풀이 시간: 약 15분

# How to
'''
1. 구간 합 배열을 생성한다.
2. 주어진 구간에 대한 합을 계산한다.
'''

# Code
import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

s = [0]
for i, n in enumerate(num_list):
    s.append(s[i] + n)

for i in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(s[j] - s[i-1])


## 메모리: 41316 KB, 시간: 260 ms