# BOJ_11724_연결 요소의 개수 구하기
# 난이도: 실버5
# 풀이 날짜: 23.10.08
# 풀이 시간: 약 30분

# How to
"""
1. 입력받은 엣지를 이용하여 인접 리스트를 생성한다.
2. 노드를 순회하면서 방문하지 않은 노드일 경우 cnt를 1 증가시키고, DFS를 수행한다.
    DFS가 끝날 때까지 탐색한 모든 노드의 집합이 하나의 연결 요소가 된다.
"""

# Comment
"""
처음에 스택으로 풀고 시간 초과가 나서 스택 사용이 문제인 줄 알고 교재대로 재귀로 변경했다.
근데 시도 2는 왜 메모리 초과가 나는지 진짜 모르겠다.
교재랑 다른게 없는데;; 그래서 그냥 교재 코드를 똑같이 입력했더니 이건 통과과 되더라.. 대체 왜????????
"""


# Code
import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)


def dfs(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            dfs(i)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        count+=1
        dfs(i)

print(count)

"""
시도 2. 메모리 초과

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)


def DFS(i):
    visited[i] = True
    for k in A[i]:
        if visited[k] == False:
            DFS(i)

cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        cnt += 1
        DFS(i)

print(cnt)
"""


"""
시도 1. 시간초과

import sys
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())

adjacent_list = [[] for _ in range(N+1)]
visited_list = [False] * (N+1)
stack = []
cnt = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)


def DFS(i):
    visited_list[i] = True
    for k in adjacent_list[i]:
        if not visited_list[k]:
            stack.append(k)
    while stack:
        i = stack.pop()
        DFS(i)


for i in range(1, N+1):
    if not visited_list[i]:
        cnt += 1
        DFS(i)

print(cnt)
"""

## 메모리: 65144 KB, 시간: 660 ms