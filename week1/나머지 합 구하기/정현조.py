import sys #시간 초과
line1 = sys.stdin.readline().strip().split(' ')
n = int(line1[0])
m = int(line1[1])

number = sys.stdin.readline().strip().split(' ')
number = list(map(int, number))

count = 0
for i in range(n-1):
    for j in range(n, i, -1):
        arr = number[i:j]
        result = sum(arr)
        if(result%m==0):
            count += 1
print(count)