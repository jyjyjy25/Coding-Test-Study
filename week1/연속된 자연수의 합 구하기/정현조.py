# BOJ_2018_수들의 합5
# 난이도: 실버5
# 풀이 날짜: 23.08.19
# 풀이 시간:

# How to
# 주어진 수의 절반부터 시작하면 될 것 같아서 halfN을 구함

# Code
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

## 메모리:  KB, 시간:  ms