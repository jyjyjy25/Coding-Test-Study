# BOJ_13023_친구 관계 파악하기
# 난이도: 골드5
# 풀이 날짜: 23.10.09
# 풀이 시간: 약 45분

# How to
"""
이 문제의 핵심은 깊이가 5에 도달하는 경우가 있는지 여부를 확인하는 것이다.
또한 친구 관계는 방향성이 없기 때문에 재귀에서 탈출할 경우 재탐색이 가능하도록 visited를 초기화해줘야 한다.
"""

# Comment
"""
visited를 왜 초기화헤줘야하는지 이해하는게 오래걸렸다.
이런 기법을 백트래킹이라고 한다더라.
"""

# Code
import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())

A = [[] for _ in range(N)]
visited = [False] * (N)
EXIST = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)


def DFS(i, depth):
    global EXIST
    visited[i] = True
    depth += 1
    
    if depth == 5:
        EXIST = 1
        return

    for k in A[i]:
        if not visited[k]:
            DFS(k, depth)
    visited[i] = False

for i in range(N):
    DFS(i, 0)
    if EXIST:
        break

print(EXIST)

"""
3차 시도. 시간초과
마지막에 문제에서 제시한 친구관계를 찾았을 경우 for 문을 빠져나오는 코드를 추가했다.

import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())

A = [[] for _ in range(N)]
visited = [False] * (N)
EXIST = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)


def DFS(i, depth):
    global EXIST
    visited[i] = True
    
    if depth == 5:
        EXIST = 1
        return

    for k in A[i]:
        if not visited[k]:
            DFS(k, depth + 1)
    visited[i] = False

for i in range(N):
    DFS(i, 1)
    if EXIST:
        break

print(EXIST)
"""

"""
2차 시도. 실패
처음 재귀를 시작할 때 이미 depth에 1을 넣어준 상태로 실행했기 때문에 재귀함수에 들어가면 바로 또 1을 더해주게 된다.
따라서 재귀함수를 시작하자마자 depth에 1을 더해주면 안되고, 재귀함수를 실행시킬 때 1을 더해줘야 했다.
아니면 depth를 0으로 시작하던지..

import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())

A = [[] for _ in range(N)]
visited = [False] * (N)
EXIST = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)


def DFS(i, depth):
    global EXIST
    visited[i] = True
    depth += 1
    
    if depth == 5:
        EXIST = 1
        return

    for k in A[i]:
        if not visited[k]:
            DFS(k, depth)
    visited[i] = False

for i in range(N):
    depth = 1
    if not visited[i]:
        DFS(i, depth)

print(EXIST)
"""

"""
1차 시도. 실패
백트레킹을 안 해서 실패한 것 같다.

import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())

A = [[] for _ in range(N)]
visited = [False] * (N)
EXIST = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)


def DFS(i, depth):
    global EXIST
    visited[i] = True
    depth += 1
    
    if depth == 5:
        EXIST = 1
        return

    for k in A[i]:
        if not visited[k]:
            DFS(k, depth)

for i in range(N):
    depth = 1
    if not visited[i]:
        DFS(i, depth)

print(EXIST)
"""

## 메모리: 31256 KB, 시간: 716 ms