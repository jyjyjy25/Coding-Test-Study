# BOJ_17298_오큰수
# 난이도: 골드4
# 풀이 날짜: 23.08.27
# 풀이 시간: 34:25

# How to
# 1st try
# 시간 초과... 책에 적힌대로 N이 너무 커져서 그런듯듯

# Comment


# Code
import sys
N = int(sys.stdin.readline())
aList = list(map(int, sys.stdin.readline().strip().split(' ')))

printStack = []
for i in range(N):
    j = i+1
    while j != len(aList)+1:
        if j == len(aList):
            printStack.append(-1)
            break
        if aList[i] >= aList[j]:
            j += 1
            continue
        printStack.append(aList[j])
        break
    print(printStack[i], end = ' ')
    

## 메모리:  KB, 시간:  ms