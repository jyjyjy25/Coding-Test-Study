# BOJ_문제번호_문제명
# 난이도: 실버5
# 풀이 날짜: 23.01.01
# 풀이 시간:

# How to


# Comment
# 병합정렬로 풀어보려 했는데 어딘가 잘못된듯

# Code (type error)
import sys
n = int(sys.stdin.readline())
arr = list(int(sys.stdin.readline()) for _ in range(n))
print(arr)

def merge(arr, low, high):
    temp = []
    mid = (low + high)//2
    s1, s2 = low, mid+1

    while s1 <= mid and s2 <= high:
        if arr[s1] <= arr[s2]:
            temp.append(arr[s1])
            s1 += 1
        else:
            temp.append(arr[s2])
            s2 += 1
    
    while s1 <= mid:
        temp.append(arr[s1])
        s1 += 1
    
    while s2 <= high:
        temp.append(arr[s2])
        s2 += 1

    for i in range(low, high+1):
        arr[i] = temp[i-low]

    return arr

def merge_sort(arr, low, high):
    if low >= high:
        return
    
    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)

    result = merge(arr, low, high)
    return result

arr = merge_sort(arr, 0, n-1)
for i in range(n):
    print(arr[i])

## 메모리:  KB, 시간:  ms