# BOJ_1260_DFS와 BFS
# 난이도: 실버2
# 풀이 날짜: 23.10.09
# 풀이 시간:

# How to
# 1. n,m,v를 받고 각각의 방문요소 배열을 만듦
# 2. dfs, bfs를 돌림

# Comment
# BFS, DFS 함수는 맞게 짠거 같은데 예시 2번 답이 틀리게 나와서 당황중

# Code
import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().strip().split(' '))
nearList = [[] for _ in range(n+1)]
dfsVisited = [False] * (n+1)
bfsVisited = [False] * (n+1)

def DFS(node):
    dfsVisited[node] = True
    print(node, end=" ")
    for i in nearList[node]:
        if not dfsVisited[i]:
            DFS(i)

def BFS(v):
    queue = deque([v])
    bfsVisited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in nearList[v]:
            if not bfsVisited[i]:
                bfsVisited[i] = True
                queue.append(i)

for i in range(m):
    s, e = map(int, sys.stdin.readline().strip().split(' '))
    nearList[s].append(e)
    nearList[e].append(s)

DFS(v)
print()
BFS(v)

## 메모리:  KB, 시간:  ms