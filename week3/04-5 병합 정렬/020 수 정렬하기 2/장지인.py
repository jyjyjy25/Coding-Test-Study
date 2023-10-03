# BOJ_2751_수 정렬하기2
# 난이도: 실버5
# 풀이 날짜: 23.09.29
# 풀이 시간: 30분

# How to
'''
    분할정복 알고리즘을 사용하였다.
    1. 충분한 크기가 되기 전까지는 계속 반씩 나눈다.
    2. 원소가 2개 이하일 경우 정렬한다
    3. 정렬된 두 배열을 정렬이 유지되도록 합친다.
    4. 상위 배열에 대해 반복한다.
'''

# Comment
'''
    직접 입력한 작은 수에 대해서는 풀리지만 틀렸습니다가 뜬다.
    어느 부분이 만족하지 않는지 알 수 없다.
'''

# Code
import sys
input = sys.stdin.readline
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

def dc(arr):
    if len(arr) <= 2:
        return sorted(arr)
    
    m = int(len(arr)/2)

    left = dc(arr[:m])
    right = dc(arr[m:])
    # print(left, right)
    l_id, r_id = 0, 0
    result = []
    for i in range(len(arr)):
        # print('rem',i, result)
        if left and l_id >= len(left):
            result.extend(right[r_id:])
            break
        elif right and r_id >= len(right):
            result.extend(left[l_id:])
            break
        else:
            if left[l_id] < right[r_id]:
                result.append(left[l_id])
                l_id += 1
            else:
                result.append(right[r_id])
                r_id += 1
    # print('result:', result)
    return result

print(dc(nums))

## 메모리:  KB, 시간:  ms