import sys #시간 초과
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().strip().split(' ')))

arr = []
good = 0
for i in range(n-1):
    for j in range(i+1, n, 1):
        tmp = numbers[i]+numbers[j]
        if(max(numbers) >= tmp and arr.count(tmp) == 0):
            arr.append(tmp)
print(arr)

for i in range(len(arr)):
    if(numbers.count(arr[i])!=0):
            good += numbers.count(arr[i])

print(good)