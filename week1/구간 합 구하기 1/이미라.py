# BOJ_11659_구간 합 구하기 1
# 난이도: 실버 3
# 풀이 날짜: 23.08.23
# 풀이 시간: 17분

# How to

"""
1. 처음 입력받은 리스트의 누적 합을 구한다.
    ex. prefix_sum[2] = 0 ~ 3 번째 숫자의 합
2. 입력받은 범위만큼 계산해서 출력한다.
    ex. 2 4 -> prefix_sum[4] - prefix_sum[1] : 1 ~ 4 번째 숫자의 합

- 입력받은 범위만큼 반복문을 돌려 인덱스에 해당하는 값을 더했을 때 시간 초과 오류 발생
- 구간 합 구하는 방법을 이용해 해결
"""

# Code

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

prefix_sum = [0]
temp = 0

for i in num:
    temp += i
    prefix_sum.append(temp)

for i in range(m):
    first, last = map(int, input().split())
    print(prefix_sum[last] - prefix_sum[first - 1])


# 시간 초과 오류 발생

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

result = 0


for i in range(m):
    first, last = map(int, input().split())

    for j in range(first - 1, last):
        result += num[i]    
    print(result)

## 메모리: 41316 KB,  시간: 300 ms