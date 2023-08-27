# BOJ_10986_나머지 합 구하기
# 난이도: 골드3
# 풀이 날짜: 23.08.20
# 풀이 시간: 약 25분

# How to
'''
1. 구간 합 2차원 배열을 생성한다.
2. 2차원 배열을 순회하며 M으로 나누어 떨어지는 요소를 카운팅한다.
'''

# Code
import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

s = []
for i in range(N-1):
    arr = num_list[i:]
    temp_list = [0 for _ in range(i+1)]
    for k, a in enumerate(arr):
        temp_list.append(temp_list[k+i] + a)
    s.append(temp_list)

cnt = 0
for i in range(N-1):
    for n in s[i]:
        if (n != 0 and n % M == 0):
            cnt += 1

print(cnt)

## 메모리:  KB, 시간:  ms
## 메모리 초과