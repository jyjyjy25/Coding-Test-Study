# BOJ_1167_트리의 지름 구하기
# 난이도: 골드3
# 풀이 날짜: 23.10.09
# 풀이 시간: 약 50분

# How to
"""
distance를 저장하는 리스트를 하나 생성하여 BFS를 수행할 때마다 임의의 노드로부터 해당 노드까지의 거리를 저장한다.
distance에 저장된 값 중 최대값을 가진 노드부터 다시 BFS를 수행한다.
이는 임의의 노드에서 가장 긴 경로로 연결돼있는 노드는 트리의 지름에 해당하는 두 노드 중 하나이기 때문이다.
이후 distance에 저장된 값 중 최대값이 트리의 지름이다.
"""

# Comment
"""
"임의의 노드에서 가장 긴 경로로 연결돼있는 노드는 트리의 지름에 해당하는 두 노드 중 하나이다."가 중요한 아이디어인 것 같다.
"""


# Code
import sys
from collections import deque

N = int(sys.stdin.readline().strip())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [0] * (N+1)

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    node = temp[0]
    data = temp[1:]
    for i in range(0, len(data), 2):
        if data[i] == -1:
            break
        A[node].append((data[i], data[i+1]))


def BFS(v):
    queue = deque()
    visited[v] = True
    queue.append(v)
    while queue:
        node = queue.popleft()
        for i in A[node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                distance[i[0]] = distance[node] + i[1]
                queue.append(i[0])


BFS(1)
max_idx = 1
for i in range(2, N+1):
    if distance[max_idx] < distance[i]:
        max_idx = i

visited = [False] * (N+1)
distance = [0] * (N+1)
BFS(max_idx)

print(max(distance))


## 메모리: 73052 KB, 시간: 652 ms