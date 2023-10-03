# BOJ_11004_K번째 수
# 난이도: 실버5
# 풀이 날짜: 23.09.29
# 풀이 시간: 1시간정도

# How to


# Comment
'''
    꽤나 오래 보고 있으나 pivot 구하는 것에 대해서 이해가 되지 않았음..
    pivot == K가 이해가 되지 않음.
    나중에 다시 확인해볼예정
'''

# Code
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

def quick_sort(arr, K):
    pivot = arr[int(len(arr)/2)]
    left, right = [], []
    for e in arr:
        if e < pivot: left.append(e)
        else: right.append(e)
    
    if len(left) >= K:
        return(left[K-1])
    
    new_K = K - len(left)
    if new_K == 1:
        return pivot
    else:
        return quick_sort(right, new_K - 1)

print(quick_sort(nums, K))

## 메모리:  KB, 시간:  ms

# 재귀함수 이용한 코드. 시간초과 발생
'''
import sys
input = sys.stdin.readline

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[int(len(arr)/2)]
    left, mid, right = [], [], []
    for e in arr:
        if e < pivot: left.append(e)
        elif e > pivot: right.append(e)
        else: mid.append(e)
    
    return quick_sort(left) + mid + quick_sort(right)

N, K = map(int, input().split())
nums = list(map(int, input().split()))

print(quick_sort(nums)[K-1])
'''