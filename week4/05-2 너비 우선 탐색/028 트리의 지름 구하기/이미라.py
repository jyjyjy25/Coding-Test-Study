# BOJ_1167_트리의 지름
# 난이도: 골드 3
# 풀이 날짜: 23.10.08
# 풀이 시간: 79 분

# How to
"""
1. 값을 입력받는다.
2. 데이터를 저장할 graph, 노드 방문 여부를 저장할 visited_count를 초기화 한다.
    이때, tmp[0]은 연결된 노드를 의미하고 tmp[len(tmp)-1]은 완료 여부를 나타내므로 안쪽에 있는 ` 연결된 노드 `만 초기화 해야 한다.
3. DFS()를 실행한다.
    탐색하지 않은 노드라면, 탐색하기까지 걸린 간선의 거리를 저장한다.
    재귀 DFS()를 실행한다.
4. 노드 1에 대해 결과를 출력하고 visited_count에서 가장 긴 노드에 대해 한 번 더 DFS 탐색한다.
5. 결과를 출력한다.
"""

# Comment
"""
- 하나의 노드에서 시작하여 끝까지 탐색했을 때 가장 긴 경로를 가지는 두 노드의 거리가 트리의 지름이다.
- 노드 1에 대해서만 탐색을 수행했을 때 예제는 풀 수 있었는데 제출했을 때 틀렸다는 결과가 나왔다. 반례가 있을 것으로 추정되어 가장 긴 노드에 대해 한 번 더 해봤더니 정답이라고 출력되었다.
"""

# Code
from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# dfs 탐색
def dfs(x, y):
    for a, b in graph[x]:
        if visited_count[a] == -1:
            visited_count[a] = b + y
            dfs(a, b + y)


n = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(tmp) - 2, 2):
        graph[tmp[0]].append([tmp[j], tmp[j + 1]])


visited_count = [-1] * (n + 1)
visited_count[1] = 0
dfs(1, 0)

new_max = visited_count.index(max(visited_count))
visited_count = [-1] * (n + 1)
visited_count[new_max] = 0
dfs(new_max, 0)

print(max(visited_count))

## 메모리: 75800 KB, 시간: 872 ms
