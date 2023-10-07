# BOJ_11724_연결 요소의 개수
# 난이도: 실버2
# 풀이 날짜: 23.10.8
# 풀이 시간: 30분

# How to
'''
    1. 요소를 matrix에 넣는다. (양방향 그래프이므로, 양쪽에 넣는다)
    2. 맨 앞 요소부터 깊이 우선 탐색을 수행한다.
       연결 요소의 단위만큼 DFS가 실행되므로, DFS가 실행되는 횟수를 반환한다.
'''

# Comment
'''
    연결 요소가 무슨 뜻인지 처음에 몰라서 검색해보았다.
    어쨋든 간선으로 이어진 노드들의 집합을 연결 요소라고 하는 듯 하다.

    연결 요소가 무엇인지만 알면, DFS가 몇번 수행되는지만으로 정답을 구할 수 있었다.

    문제를 풀었는데도 런타임에러(RecursionError)가 나타나서 보니.. 
    백준 내에서 기본 재귀 제한을 1000정도로 잡아두었기에, 이 제한을 문제에 맞게 크게 늘려줘야했다.
    `sys.setrecursionlimit(10**6)`
'''

# Code
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

matrix = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    matrix[u].append(v)
    matrix[v].append(u)

visited = [ False for _ in range(N+1)]

def DFS(e):
    global visited, matrix

    visited[e] = True
    for node in matrix[e]:
        if visited[node] == False:
            DFS(node)

count = 0

for i in range(1,N+1):
    if visited[i] == False:
        DFS(i)
        count += 1

print(count)

## 메모리: 65304 KB, 시간: 664 ms