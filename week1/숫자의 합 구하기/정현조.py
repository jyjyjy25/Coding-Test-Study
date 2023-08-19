import sys
n = int(sys.stdin.readline())
number = list(sys.stdin.readline().strip())

sum = 0
for i in range(n):
    sum += int(number[i])

print(sum)
