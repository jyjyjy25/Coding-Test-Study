# BOJ_11660_구간 합 구하기 2
# 난이도: 실버1
# 풀이 날짜: 23.08.19
# 풀이 시간: 약 38분

# How to
'''
1. 구간 합 배열을 생성한다.
2. 주어진 구간에 대한 합을 계산한다.
'''

# Code
import sys

N, M = map(int, sys.stdin.readline().split())

num_list = []
s = []
s.append([0 for _ in range(N+1)])
for i in range(N):
    num_list.append(list(map(int, sys.stdin.readline().split())))
    # 구간 합 배열 생성
    temp_list = [0]
    for k, n in enumerate(num_list[i]):
        temp_list.append(temp_list[k] + n)
    s.append(temp_list)

for i in range(M):
    sum = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for k in range(x1, x2+1):
        sum = sum + s[k][y2] - s[k][y1 - 1]
    print(sum)

## 메모리:  KB, 시간:  ms
## 시간 초과