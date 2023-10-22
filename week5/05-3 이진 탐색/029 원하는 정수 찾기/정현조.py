# BOJ_1920_수 찾기
# 난이도: 실버4
# 풀이 날짜: 23.10.14
# 풀이 시간: 30분

# How to
# 1. 값을 받는다
# 2. AList를 오름차순으로 정렬한다
# 3. targetList를 돌며 target을 지정한다
# 4. 투 포인터를 사용하여 범위를 좁혀가며 이진탐색을 수행한다

# Comment
# 첫 시도엔 나름 간략하게 해보려고 재귀함수를 짰는데 시간 초과가 떴다
# 그래서 그냥 일반 반복문으로 짰다
# 문제 방식 생각하는 건 별로 안 어려웠는데 인덱스랑 값을 헷갈린다거나 반복문 탈출을 안 시켜준다거나 하는 사소한 실수들이 있었다

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

## 메모리:  46728KB, 시간:  772ms