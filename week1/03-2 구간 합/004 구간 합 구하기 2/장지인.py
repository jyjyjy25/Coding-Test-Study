# BOJ_11660_구간 합 구하기 5
# 난이도: 실버1
# 풀이 날짜: 23.08.15
# 풀이 시간: 45분

# How to
'''
교재를 통해서 힌트를 얻기는 했지만, 합배열을 이해하는 것부터가 너무 오래 걸렸다.
세삼 내가 숫자에 매우매우 약하다는 것을 다시 깨닫게 해주는 문제였다.
sum_list[x][y]는 numbers[0][0] ~ numbers[x][y]의 합이 되도록 만들었다.

개인적으로 구간 합 문제들을 풀다보니 느끼는게 무조건 앞에 0을 두고 1번 인덱스부터 하는 것이 좋을 것 같다.
'''

# Code
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = [[0] for _ in range(N+1)]
sum_list = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    numbers[i] = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(1, N+1):
        sum_list[i][j] = sum_list[i][j-1] + sum_list[i-1][j] - sum_list[i-1][j-1] + numbers[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum_list[x2][y2] - sum_list[x1-1][y2] - sum_list[x2][y1-1] + sum_list[x1-1][y1-1])

## 메모리: 106028 KB, 시간: 1044 ms