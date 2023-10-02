# BOJ_1517_버블 소트
# 난이도: 플레티넘5
# 풀이 날짜: 23.09.29
# 풀이 시간: 1시간 이상

# How to


# Comment
'''
    앞의 버블정렬 스왑 횟수를 구하는 문제와 착각하여 실패함.
    분할정복 알고리즘 자체가 아직 이해가 되지 않아서 풀기가 매우 어렵다..

    스터디 모임 시간에 분할정복에 대해 이해를 한 뒤에 풀 수 있을 것 같음
'''

# Code

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

arr = []
for i in range(N):
    arr.append([nums[i], i])

arr.sort()
print(arr)
result = 0
for i in range(N):
    n = arr[i][1] - i
    
    if result < n:
        result = n

print(result+1)

## 메모리:  KB, 시간:  ms