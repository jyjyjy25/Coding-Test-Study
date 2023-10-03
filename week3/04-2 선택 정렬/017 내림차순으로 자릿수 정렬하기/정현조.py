# BOJ_1427_소트인사이드
# 난이도: 실버5
# 풀이 날짜: 23.08.29
# 풀이 시간: 16:23

# How to
# maxIdx를 잘 조절해서 조건에 맞을때 swap 시킴


# Comment


# Code
import sys
numList = list(map(int, sys.stdin.readline().strip()))

for i in range(len(numList)):
    maxIdx = i
    for j in range(len(numList)-i-1):
        if numList[maxIdx] < numList[i+j+1]:
            maxIdx = i+j+1
            
    numList[i], numList[maxIdx] = numList[maxIdx], numList[i]

result = ''.join(map(str, numList))
print(result)


## 메모리:  31256KB, 시간:  44ms