# BOJ_1377_버블 정렬 프로그램 1
# 난이도: 골드2
# 풀이 날짜: 23.09.05
# 풀이 시간: 약 13 + 

# How to
"""
1. 입력받은 값과 인덱스를 리스트에 튜플로 같이 저장한다.
2. 리스트를 정렬한다.
3. 정렬 후 리스트에서 각각의 요소에 대한 튜플의 1 번째 값(array[i][1])은 정렬되기 이전의 인덱스를 나타내고, 이를 현재 인덱스에서 빼면 정렬 전 index - 정렬 후 index값이 된다.
    예시) 정렬 전 리스트 = [(10,0), (1,1), (5,2), (2,3), (3,4)]
         정렬 후 리스트 = [(1,1), (2,3), (3,4), (5,2), (10,0)]
         현재 인덱스        0       1      2      3      4
4. 정렬 전 index - 정렬 후 index의 최댓값을 구한다.
5. 최댓값에 1을 더한 값이 최종적으로 구하고자 하는 값이다.
"""

# Comment
"""
정렬이 완료됐을 때의 인덱스 + 1이 출력되어야 하는 값이다.
따라서 정렬이 완료된 시점을 찾으려고 했다.
하지만 N의 범위를 고려했을 때 시간초과가 나지 않도록 버블정렬 이외의 다른 방법이 필요해 보였다.
그치만 아이디어가 떠오르지 않아 그냥 교재를 참고했다..ㅜ
또한 교재에서 설명한 아이디어에서 '특정 데이터가 안쪽 루프에서 swap의 왼쪽으로 이동할 수 있는 최대 거리가 1이라는 뜻이다'라는게 무슨 뜻인지 이해되지 않는다..
"""

# Code
import sys
N = int(sys.stdin.readline())
array = [(int(sys.stdin.readline().strip()), i) for i in range(N)]

sorted_array = sorted(array)

max_index = 0
for i in range(N):
    index_sub = sorted_array[i][1] - i
    if max_index < index_sub:
        max_index = index_sub

print(max_index + 1)

## 메모리:  KB, 시간:  ms

"""
=> array.index(a) 부분으로 인해 시간 초과가 난 것으로 짐작한다.

import sys
N = int(sys.stdin.readline())
array = [int(sys.stdin.readline().strip()) for _ in range(N)]

sorted_array = sorted(array)

max_index = 0
for i, a in enumerate(sorted_array):
    index_sub = array.index(a) - i
    if max_index < index_sub:
        max_index = index_sub

print(max_index + 1)
"""