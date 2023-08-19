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