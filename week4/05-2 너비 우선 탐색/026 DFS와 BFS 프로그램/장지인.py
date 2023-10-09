# BOJ_1260_DFS와 BFS
# 난이도: 실버2
# 풀이 날짜: 23.10.8
# 풀이 시간: 50분

# How to


# Comment
'''
    72%에서 런타임 에러 발생한다.
    어디서 문제인지 잘 모르겠습니다..
'''

# Code
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

def DFS(n):
    global matrix, visited

    print(n, end=' ')
    visited[n] = True

    for v in matrix[n]:
        if not visited[v]:
            DFS(v)

def BFS(n):
    global matrix, visited
    queue = deque()
    queue.append(n)
    visited[n] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in matrix[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M, V = map(int, input().split())

matrix = [[] for _ in range(N+1)]
visited = [ False for _ in range(N+1)]
queue = deque()

for _ in range(M):
    u, v = map(int, input().split())
    matrix[u].append(v)
    matrix[v].append(u)

for i in range(N+1):
    matrix[i].sort()

DFS(V)
print()
visited = [ False for _ in range(N+1)]
BFS(V)



## 메모리: 34184 KB, 시간: 80 ms