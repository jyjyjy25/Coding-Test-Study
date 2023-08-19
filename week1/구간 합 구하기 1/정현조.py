import sys #시간초과..
line1 = sys.stdin.readline().strip().split(' ')
n = int(line1[0])
m = int(line1[1])

number = sys.stdin.readline().strip().split(' ')
number = list(map(int, number))

for i in range(m):
    rangeline = sys.stdin.readline().strip().split(' ')
    start = int(rangeline[0])
    end = int(rangeline[1])+1

    sum = 0
    for j in range(start, end, 1):
        sum += number[j-1]
    print(sum)