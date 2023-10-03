# BOJ_1517_버블 정렬 프로그램 2
# 난이도: 플래티넘
# 풀이 날짜: 23.10.02
# 풀이 시간: 약 60분

# How to
"""
버블 정렬이 수행될 때마다
result += 버블 정렬을 수행할 요소의 인덱스(rp) - 남은 앞쪽 데이터 개수
를 계산한다.
"""

# Comment
"""
버블 정렬을 수행할 요소의 인덱스(rp)에서 남은 앞쪽 데이터 개수를 빼야하는데 남은 앞쪽 데이터 수를 어케 구해야할지 모르겠다 ~..
"""


# Code
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
result = 0


def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)

    return merge(arr, left, right)

    
def merge(arr, left, right):
    global result
    mid = (left + right) // 2
    lp, rp = left, mid + 1
    tmp = []
    while lp <= mid and rp <= right:
        if arr[lp] >= arr[rp]:
            tmp.append(arr[rp])
            # result += (rp - )
            rp += 1
        else:
            tmp.append(arr[lp])
            lp += 1
    
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
print(result)


## 메모리:  KB, 시간:  ms