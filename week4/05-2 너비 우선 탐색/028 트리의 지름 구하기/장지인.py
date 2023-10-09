# BOJ_1167_트리의 지름
# 난이도: 골드2
# 풀이 날짜: 23.10.9
# 풀이 시간:

# How to


# Comment
'''
    지름을 구하는 방법에 대해서는 교제의 문제해결하기를 참고하였다.
    '임의의 한 정점에서 제일 먼 정점이 지름을 결정하는 정점 중 하나일 것이다'

'''

# Code

# matrix 출력 용 함수
def print_matrix():
    global matrix
    for row in matrix:
        for e in row:
            print(e, end=' ')
        print()

import sys
input = sys.stdin.readline
from collections import deque

V = int(input())
matrix = [[] for _ in range(V+1)]
visited = [ False for _ in range(V+1)]

for _ in range(V):
    nums = list(map(int, input().split()))
    idx = nums[0]
    for i in range(1,len(nums), 2):
        if nums[i] == -1:
            break
        matrix[idx].append([nums[i], nums[i+1]])

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        node = queue.popleft()
        for n, d in matrix[node]:
            pass

    #40분쯤 고민하고 포기함 ㅎㅎ

    

## 메모리:  KB, 시간:  ms