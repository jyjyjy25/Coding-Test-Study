# BOJ_1546_평균 구하기
# 난이도: 브론즈1
# 풀이 날짜: 23.08.17
# 풀이 시간: 약 6분

# How to
'''
1. 최고점을 찾는다.
2. 각각의 과목에 대해 계산 후 평균을 구한다.
'''

# Code
import sys

N = int(sys.stdin.readline())
score_list = list(map(int, sys.stdin.readline().split()))

max_score = max(score_list)
sum_score = 0
for i in score_list:
    sum_score = sum_score + (i / max_score * 100)

print(sum_score / N)

## 메모리: 31256 KB, 시간: 40 ms