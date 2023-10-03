# BOJ_1517_버블 소트
# 난이도: 플레티넘 5
# 풀이 날짜: 23.09.24
# 풀이 시간: 132분

# How to
"""
1. N, arr을 입력받는다.
2. 그룹을 두개로 나누어서 재귀함수 형태로 실행한다.
3. 양쪽 그룹의 index가 가리키는 값을 비교하여 더 작은 수를 선택해 리스트에 저장한다.
4. 선택된 데이터의 index 값을 오른쪽으로 한 칸 이동한다.
5. 로직을 수행하면서 오른쪽이 더 큰 경우, swap이 일어나게 되므로 앞쪽 그룹의 데이터 개수만큼 결과값에 더한다.
"""

# Comment
"""
- 와 진짜 너무 어려웠고, 런타임 에러를 해결하는게 너무 어려웠다...
- 트리 사용해서 문제를 푸는 방법을 더 공부해야 할 것 같다.
- 전체적인 코드는 교재를 참고하였다.
"""

# Code

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = 0

def merge_sort(start, end):
    global answer, arr

    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        temp = []
        x, y = start, mid + 1

        while x <= mid and y <= end:
            if arr[x] <= arr[y]:
                temp.append(arr[x])
                x += 1
            else:
                temp.append(arr[y])
                y += 1
                answer += (mid - x) + 1

        if x <= mid:
            temp = temp + arr[x:mid + 1]
        if y <= end:
            temp = temp + arr[y:end + 1]
        for i in range(len(temp)):
            arr[start+i] = temp[i]

merge_sort(0, N - 1)
print(answer)

## 메모리: 86700 KB, 시간: 2360 ms