# BOJ_1920_원하는 정수 찾기
# 난이도: 실버 4
# 풀이 날짜: 23.10.15
# 풀이 시간: 약 40분

# How to
"""
이진 탐색 알고리즘 그대로 코드를 구현하면 된다.
데이터를 정렬한 뒤 타겟 데이터를 중앙값과 <, >, = 비교하여 범위를 줄여나간다.
"""

# Comment
"""
시도 1에서 시간초과가 났다.
알고리즘은 제대로 구현했지만, 리스트 슬라이싱을 하는 과정에서 시간을 많이 소요한 것으로 추정한다.
리스트 슬라이싱의 시간 복잡도는 O(k)로, a[i:j]를 수행할 경우 j-i+1이 k이다. 즉 k개를 조회하므로 시간복잡도가 k인 것이다.
앞으로는 리스트가 아닌 인덱스를 업데이트하면서 반복문을 하든.. 재귀를 돌리든 해야겠다.
"""

# Code
import sys
import time

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
X = list(map(int, sys.stdin.readline().split()))


def binary_search(x):
    global A, EXIST
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == x:
            EXIST = 1
            break
        elif A[mid] > x:
            end = mid - 1
        elif A[mid] < x:
            start = mid + 1
    

A.sort()

EXIST = 0
for x in X:
    EXIST = 0
    binary_search(x)
    print(EXIST)


"""
# 시도 1. 시간 초과
# 시간을 재보니 0.0001010894775390625초 나온다. 반면 위의 정답 코드는 9.775161743164062e-05초이다.

import sys
import time

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
X = list(map(int, sys.stdin.readline().split()))


def binary_search(A, x):
    if len(A) < 1:
        print(0)
        return

    mid = len(A) // 2
    if A[mid] == x:
        print(1)
        return
    elif A[mid] > x:
        binary_search(A[:mid], x)
    elif A[mid] < x:
        binary_search(A[mid+1:], x)
    

A.sort()

for x in X:
    binary_search(A, x)

"""
## 메모리: 47424 KB, 시간: 460 ms