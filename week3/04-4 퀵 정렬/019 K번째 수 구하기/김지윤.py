# BOJ_11004_K번째 수 구하기
# 난이도: 실버5
# 풀이 날짜: 23.10.02
# 풀이 시간: 셀 수 없음

# How to
"""
1. sort()로 정렬한다.
2. K번째 수를 출력한다.
"""

# Comment
"""
등호를 붙여야할지 말아야할지 등호 수난시대를 겪었다..
겨우 퀵정렬을 이해했더니 시간초과 ^^;;
교재 코드가 이해가 가지 않는다. 왜 pivot == K이면 K번째 수를 찾은 걸까...
책에서는 대체 왜 쉬운 문제를 이렇게 어렵게 풀고 있는거지?
"""

# Code
import sys
N, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))


"""
호어 분할 방식을 통해 첫 번째 요소를 피벗으로 지정하는 퀵 정렬
"""
def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    i = start + 1
    j = end
    while i <= j:
        while i <= end and arr[i] <= arr[pivot]:
            i += 1
        while j > start and arr[j] >= arr[pivot]:
            j -= 1
        if i > j:
            arr[j], arr[pivot] = arr[pivot], arr[j]
        else:
            arr[i], arr[j] = arr[j], arr[i]
    
    quick_sort(arr, start, j - 1)
    quick_sort(arr, j + 1, end)


"""
호어 분할 방식을 응용하여 마지막 요소를 피벗으로 지정하여 퀵 정렬을 구현해 보았다.
"""
def quick_sort2(arr, start, end):
    if start >= end:
        return

    pivot = end
    i = start
    j = end - 1
    while i <= j:
        while i < end and arr[i] <= arr[pivot]:
            i += 1
        while j >= start and arr[j] >= arr[pivot]:
            j -= 1
        if i > j:
            arr[i], arr[pivot] = arr[pivot], arr[i]
        else:
            arr[i], arr[j] = arr[j], arr[i] 
    quick_sort2(arr, start, i - 1)
    quick_sort2(arr, i + 1, end)


quick_sort2(num_list, 0, N-1)
print(num_list[K-1])


## 메모리:  KB, 시간:  ms
## 시간초과