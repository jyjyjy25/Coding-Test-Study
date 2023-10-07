# BOJ_13023_ABCDE
# 난이도: 골드5
# 풀이 날짜: 23.10.8
# 풀이 시간: 20분

# How to
'''
    깊이 우선 탐색으로 풀기.
    탐색 밖으로 나오면 vsitied를 False로 돌려 놓는 것에 주의하며 그래프를 순환한다.
    깊이가 5를 달성하면 문제의 조건을 만족하므로 1을 출력한다.
'''

# Comment
'''
    확실히 비슷한 문제를 여러번 푸니까 익숙해져서 잘 푸는 것 같다.
    나름.. 이전 문제들보다 빠르게 풀 수 있었다.
'''

# Code
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

matrix = [[] for _ in range(N)]
visited = [False for _ in range(N)]
result = 0
for _ in range(M):
    u, v = map(int, input().split())
    matrix[u].append(v)
    matrix[v].append(u)

def DFS(e, depth):
    global visited, matrix, result

    if depth == 5:
        result = 1
        return
        
    visited[e] = True
    for node in matrix[e]:
        if visited[node] == False:
            DFS(node, depth + 1)
    
    visited[e] = False

for i in range(N):
    DFS(i, 1)
    if result == 1:
        break

print(result)


## 메모리: 31256 KB, 시간: 1520 ms