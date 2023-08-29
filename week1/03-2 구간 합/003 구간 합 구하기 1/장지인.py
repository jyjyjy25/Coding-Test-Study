# BOJ_11659_구간 합 구하기 4
# 난이도: 실버3
# 풀이 날짜: 23.08.14
# 풀이 시간: 11분

# How to
'''
이 문제는 책 앞부분에 있는 구간합에 대한 설명을 듣고 풀어서 괜찮았다.
크게 2가지 부분이 문제였는데, 첫번째로는 합배열에서 원하는 구간 i - j를 선택할때, sum[i-2]를 하려다보니
i가 1일 경우 오류가 날 수 밖에 없었다. sum_list 맨 앞에 0을 넣어서 해결했다.
두번째로는 시간초과였는데, 앞의 문제들은 별 일이 안생기길래 sys 라이브러리를 안썻더니 난 오류였다.
앞으로는 그냥 무조건 넣어야하나 싶다.
'''

# Code
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sum_list = [0]
temp = 0

for i in range(N):
    temp += numbers[i]
    sum_list.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i-1])

## 메모리: 41316 KB, 시간: 260 ms