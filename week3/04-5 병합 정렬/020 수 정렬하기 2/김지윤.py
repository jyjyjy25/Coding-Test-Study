# BOJ_2751_수 정렬하기 2
# 난이도: 실버5
# 풀이 날짜: 23.10.02
# 풀이 시간: 약 70분

# How to
"""
1. 병합 정렬 알고리즘을 이용하여 수를 정렬한다.
2. 정렬한 수를 출력한다.
"""

# Comment
"""
열심히 공부했다..
"""

# Code
import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]


def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)

    return merge(arr, left, right)

    
def merge(arr, left, right):
    mid = (left + right) // 2
    lp, rp = left, mid + 1
    tmp = []
    while lp <= mid and rp <= right:
        if arr[lp] <= arr[rp]:
            tmp.append(arr[lp])
            lp += 1
        else:
            tmp.append(arr[rp])
            rp += 1
    
    while lp <= mid:
        tmp.append(arr[lp])
        lp += 1

    while rp <= right:
        tmp.append(arr[rp])
        rp += 1

    for k in range(left, right + 1):
        arr[k] = tmp[k - left]

    return arr


merge_sort(nums, 0, N-1)
for n in nums:
    print(n)


## 메모리: 83896 KB, 시간: 4684 ms