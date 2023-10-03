# BOJ_11004_K번째 수
# 난이도: 실버5
# 풀이 날짜: 23.09.17
# 풀이 시간:

# How to


# Comment
# 너무 오래전에 풀어서 뭐가 문제였는지 기억이 안 남.. 다음주까지 알아내서 고쳐볼게요

# Code
''' 책에 있는 방법 - 시간 초과(1%)
import sys
n, k = list(map(int, sys.stdin.readline().strip().split()))
arr = list(map(int, sys.stdin.readline().strip().split()))

def quick_sort(start, end, k):
    pivot = partition(start, end)
    if pivot == k:
        return
    elif k < pivot:
        quick_sort(start, pivot-1, k)
    else:
        quick_sort(pivot+1, end, k)

def partition(start, end):
    global arr
    if start+1 == end:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        return end
    
    M = len(arr)//2
    arr[start], arr[M] = arr[M], arr[start]
    pivot = arr[start]
    low = start +1
    high = end

    while low <= high:
        while arr[low] < pivot and low < len(arr)-1:
            low += 1
        while arr[high] > pivot and high > 0:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    
    arr[low] = arr[high]
    arr[high] = pivot

    return high

quick_sort(0, n-1, k-1)
print(arr[k-1])
'''

'''
def pivotIdx(arr):
    return math.floor(len(arr)/2)

def arrSort(arr, fullArr):
    pivot = pivotIdx(arr)
    low = 0
    high = len(arr)-1
    while low != high:
        if arr[low] < arr[pivot]:
            low += 1
        if arr[high] > arr[pivot]:
            high -= 1
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
    if arr[low] >= arr[pivot]:
        arr.insert(low-1, arr[pivot])
        arr.pop(arr[pivot])
'''



## 메모리:  KB, 시간:  ms