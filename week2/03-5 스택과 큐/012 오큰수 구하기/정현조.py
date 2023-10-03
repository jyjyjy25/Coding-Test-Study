# BOJ_17298_오큰수
# 난이도: 골드4
# 풀이 날짜: 23.08.27
# 풀이 시간: 34:25

# How to
# 1st try
# 시간 초과... 책에 적힌대로 N이 너무 커져서 그런듯
# 2nd try
# ansList를 미리 -1로 해서 조건문을 하나 줄였는데 한 30퍼?까진 되더니 시간초과 뜸
# 3rd try
# 이번엔 조건문을 >=에서 <로 바꿔봄 한 46퍼까진되더니 시간초과 뜸
# 최종 try
# 전~혀 생각 안나서 지윤이꺼랑 지인언니꺼 참고함.. 거의 똑같을듯듯

# Comment
# 값이 아니라 인덱스를 이용해야한다는게 잘 머릿속에서 안 그려짐..

# Code
import sys
N = int(sys.stdin.readline())
aList = list(map(int, sys.stdin.readline().strip().split(' ')))

ansList = [-1 for _ in range(N)]
stack = []
for i in range(N):
    while stack and aList[stack[-1]] < aList[i]:
        ansList[stack.pop()] = aList[i]
    stack.append(i)
print(*ansList)

'''
[1st try]
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

[3rd try(2nd 땐 조건문을 뒤집음)]
import sys
N = int(sys.stdin.readline())
aList = list(map(int, sys.stdin.readline().strip().split(' ')))

ansList = [-1 for _ in range(N)]
for i in range(N):
    j = i+1
    while j != len(aList):
        if aList[i] < aList[j]:
            ansList[i] = aList[j]
            break
        j += 1
        continue
print(*ansList)
'''

## 메모리:  155576KB, 시간:  1112ms