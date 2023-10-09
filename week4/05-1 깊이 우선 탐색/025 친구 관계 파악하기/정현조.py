# BOJ_13023_ABCDE
# 난이도: 골드5
# 풀이 날짜: 23.10.09
# 풀이 시간:

# How to
# 1. n, m을 받음
# 2. 인접 리스트랑 방문요소 배열을 만듦
# 3. 한 점에서 dfs를 돌 때 다음 노드로 갈 때마다 깊이가 +1 되도록 하고 그 값이 5가 되면 1이 출력되게 함
# 4. 다음 수에서 또 써야하므로 방문 요소를 다시 False로 돌려둠

# Comment
# 첨에 문제를 이해 못해서 고생 좀 함 ㅎ..
# 연결 요소 개수 구하기에서 공부했던 걸 활용함
# 근데 어떻게 1과 0을 출력해야할지 모르겠음

# Code
import sys
sys.setrecursionlimit(10000000)
n, m = map(int, sys.stdin.readline().strip().split(' '))
nearList = [[] for _ in range(n+1)]
isVisited = [False] * (n+1)

def DFS(node, depth):
    if depth == 5:
        print(1)
        return
    isVisited[node] = True
    for i in nearList[node]:
        if not nearList[i]:
            depth += 1
            DFS(i, depth)
    isVisited[node] = False #리셋 시킴

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    nearList[a].append(b)
    nearList[b].append(a)

for i in range(n):
    if not isVisited[i]:
        DFS(i, 1)
## 메모리:  KB, 시간:  ms