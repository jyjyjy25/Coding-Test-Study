# BOJ_11720_숫자의 합
# 난이도: 브론즈 5
# 풀이 날짜: 23.08.17
# 풀이 시간: 약 5분

# How to
'''
1. 한 줄의 입력을 리스트로 받아오기
2. for 문 돌려서 합산하기
'''

# Code
import sys

N = int(sys.stdin.readline())
num_list = list(sys.stdin.readline().strip())

sum = 0
for i in range(N):
    sum = sum + int(num_list[i])
print(sum)

## 메모리: 31256 KB, 시간: 44 ms