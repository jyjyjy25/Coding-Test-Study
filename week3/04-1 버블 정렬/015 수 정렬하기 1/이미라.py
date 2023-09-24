# BOJ_2750_수 정렬하기
# 난이도: 브론즈 1
# 풀이 날짜: 23.09.23
# 풀이 시간: 7 분

# How to
"""
1. N(입력받을 개수)와 num(N개의 수)를 입력받는다.
2. num을 sort() 함수로 정렬한다.
"""

# Comment
"""

"""

# Code

N = int(input())
num = []

for _ in range(N):
    num.append(int(input()))

num.sort()
for i in num:
    print(i)

## 메모리: 31256 KB, 시간: 92 ms