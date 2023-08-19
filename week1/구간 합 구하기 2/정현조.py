import sys #시간초과..
line1 = sys.stdin.readline().strip().split(' ')
n = int(line1[0])
m = int(line1[1])

arr = [0]*n
for i in range(n):
    ele = sys.stdin.readline().strip().split(' ')
    ele = list(map(int, ele))
    arr[i] = ele

for i in range(m):
    position = sys.stdin.readline().strip().split(' ')
    position = list(map(int, position))
    
    sum = 0
    for j in range(position[0]-1, position[2]): #x
        for k in range(position[1]-1, position[3]): #y
            sum += arr[j][k]
    print(sum)