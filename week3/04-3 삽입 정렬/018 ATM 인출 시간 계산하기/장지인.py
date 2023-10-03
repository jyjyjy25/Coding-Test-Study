# BOJ_11399_ATM
# 난이도: 실버4
# 풀이 날짜: 23.09.29
# 풀이 시간: 20분

# How to
'''
    1. 손님의 개수를 N으로 받는다. 각 손님이 걸리는 시간을 리스트로 저장한다.
    2. 삽입정렬을 이용하여 리스트를 정렬한다.
    3. 모든 손님이 기다리는 시간을 합산하여 반환한다.
'''

# Comment
'''
    문제는 그냥 정렬만 하면 될것같지만 챕터에 맞게 삽입정렬을 사용하였다.
    마지막에 모든 손님이 기다린 시간을 합산하는데,, 합배열 생각이 안나서 그냥 직접 했다.
    오랜만에 하니 역시 많이 까먹는다. 따로 정리해야할 필요성을 느끼는 중
'''

# Code
import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

for i in range(1, N):
    idx = i
    for j in range (i, 0, -1):
        if nums[j-1] > nums[i]:
            idx = j-1
    if idx != i:
        nums.insert(idx, nums.pop(i))

result = 0
for i in range(N):
    result += sum(nums[:i+1])

print(result)

## 메모리: 31256 KB, 시간: 128 ms