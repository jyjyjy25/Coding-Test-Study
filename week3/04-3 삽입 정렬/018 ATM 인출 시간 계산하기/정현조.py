# BOJ_11399_ATM
# 난이도: 실버3
# 풀이 날짜: 23.09.17
# 풀이 시간:

# How to
# 이중 for문으로 선택 정렬을 구현하고
# 인덱스 슬라이싱을 통해 누적합을 계산함

# Comment


# Code
import sys
n = int(sys.stdin.readline().strip())
timeList = list(map(int, sys.stdin.readline().strip().split(' ')))

minTime = 0
for i in range(len(timeList)):
    for j in range(i+1, len(timeList)):
        if timeList[i] > timeList[j]:
            timeList[i], timeList[j] = timeList[j], timeList[i]
        j += 1
    minTime += sum(timeList[0:i])
    i += 1

minTime += sum(timeList)
print(minTime)
    
## 메모리:  31256KB, 시간:  140ms