# BOJ_1260_DFS와 BFS 프로그램
# 난이도: 실버2
# 풀이 날짜: 23.10.09
# 풀이 시간: 약 40분

# How to
"""

"""

# Comment
"""
이번에도 출력할 때 %가 같이 출력되어서 join()을 이용했다.. 짲응..
"""

# Code
import sys
from collections import deque
sys.setrecursionlimit(10000)

N, M, V = map(int, sys.stdin.readline().split())

A = [[] for _ in range(N+1)]
dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)
dfs_route = []
bfs_route = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)

for i in range(N+1):
    A[i].sort()


def DFS(v):
    dfs_visited[v] = True
    dfs_route.append(v)
    for i in A[v]:
        if not dfs_visited[i]:
            DFS(i)


def BFS(v):
    global dq
    bfs_visited[v] = True
    dq.append(v)
    while dq:
        node = dq.popleft()
        bfs_route.append(node)
        for i in A[node]:
            if not bfs_visited[i]:
                dq.append(i)
                bfs_visited[i] = True


dq = deque()
DFS(V)
BFS(V)

print(' '.join(map(str, dfs_route)))
print(' '.join(map(str, bfs_route)))


## 메모리: 34184 KB, 시간: 76 ms