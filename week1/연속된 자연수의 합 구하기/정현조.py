import sys #타입에러
n = int(sys.stdin.readline())

halfN = 0
if(n%2==1):
    halfN = int(n/2+0.5)
else:
    halfN = n/2

count = 0
for i in range(halfN, 0, -1):
    tmp = n
    while n!=0:
        tmp -= i
        if(tmp < 0):
            break
        elif(tmp == 0):
            count += 1
print(count+1)