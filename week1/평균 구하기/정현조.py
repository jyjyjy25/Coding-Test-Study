# BOJ_1546_평균
# 난이도: 브론즈1
# 풀이 날짜: 23.08.19
# 풀이 시간:

# How to
# 파일 포맷을 못 봐서 다양하게 풀어봄
# 1. for문 돌면서 각 배열 값을 바꿔준다
# 2. sum() 함수를 이용해서 합을 구한다
# 3. 합을 n으로 나눠 평균을 구한다.

# Code
import sys
n = int(sys.stdin.readline())
number = sys.stdin.readline().strip().split(' ')
number = list(map(int, number))

maxNum = max(number)

for i in range(n):
    number[i] = number[i]/maxNum*100

sum = sum(number)

print(sum/n)

## 메모리:  31388KB, 시간: 44ms
""" 48ms
import sys
n = int(sys.stdin.readline())
number = sys.stdin.readline().strip().split(' ')
number = list(map(int, number))

maxNum = max(number)

sum = 0
for i in range(n):
    num = number[i]/maxNum*100
    sum += num

print(sum/n)
"""

""" 44ms
import sys
n = int(sys.stdin.readline())
number = sys.stdin.readline().strip().split(' ')
number = list(map(int, number))

maxNum = max(number)

for i in range(n):
    number[i] = number[i]/maxNum*100

sum = sum(number)

print(sum/n)
"""

# import sys
# import numpy
# n = int(sys.stdin.readline())
# number = sys.stdin.readline().strip().split(' ')
# number = list(map(int, number))

# maxNum = max(number)

# for i in range(n):
#     number[i] = number[i]/maxNum*100

# average = numpy.mean(number)

# print(average)

""" 164ms
import sys
import statistics
n = int(sys.stdin.readline())
number = sys.stdin.readline().strip().split(' ')
number = list(map(int, number))

maxNum = max(number)

for i in range(n):
    number[i] = number[i]/maxNum*100

average = statistics.mean(number)

print(average)
"""