# BOJ_1920_수 찾기
# 난이도: 실버4
# 풀이 날짜: 23.10.14
# 풀이 시간:

# How to


# Comment


# Code
import sys
n = int(sys.stdin.readline().strip())
AList = list(map(int, sys.stdin.readline().strip().split(' ')))
m = int(sys.stdin.readline().strip())
targetList = list(map(int, sys.stdin.readline().strip().split(' ')))

AList.sort()

for i in range(m):
    isFound = False
    target = targetList[i]
    s = 0
    e = len(AList)-1

    while s <= e:
        midI = (s+e)//2
        midV = AList[midI]
        if midV > target:
            e = midI - 1
        elif midV < target:
            s = midI + 1
        else:
            isFound = True
            break
    
    if isFound:
        print(1)
    else:
        print(0)

''' 1st try(시간 초과) - 재귀 함수로 해서 오래걸린듯
import sys
n = int(sys.stdin.readline().strip())
AList = list(map(int, sys.stdin.readline().strip().split(' ')))
m = int(sys.stdin.readline().strip())
targetList = list(map(int, sys.stdin.readline().strip().split(' ')))

AList.sort()

def binarySearch(arr, target):
    tmp = arr
    if target < arr[0] or target > arr[len(arr)-1]:
           return 0
    
    if tmp[len(tmp)//2] > target:
            tmp = tmp[0:len(tmp)//2]
            binarySearch(tmp, target)
    elif tmp[len(tmp)//2] < target:
            tmp = tmp[len(tmp)//2:len(tmp)-1]
            binarySearch(tmp, target)
    else:
           return 1

for i in range(m):
    if binarySearch(AList, targetList[i]) == 0:
          print(0)
    else:
          print(1)
'''

## 메모리:  KB, 시간:  ms