# BOJ_2178_미로 탐색
# 난이도: 실버 1
# 풀이 날짜: 23.10.08
# 풀이 시간: 79 분

# How to
"""
1. 값을 입력받는다.
2. 데이터를 저장할 graph, 노드 방문 여부를 저장할 visited_list를 초기화 한다.
3. BFS()를 실행한다.
    앞서 정의한 방향에 따라 움직일 방향을 정한다.
    움직일 좌표가 graph 내에 존재하는지 확인한다.
    울직일 좌표가 움직을 수 있는지, visited_data에 속하는지 확인한다.
4. 결과를 출력한다.
"""

# Comment
"""
- 참고 (https://jokerldg.github.io/algorithm/2021/03/24/maze.html)
"""

# Code
from collections import deque

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

visited_list = [[False] * m for _ in range(n)]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited_list[x][y] = True

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]    

            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue
            
            if graph[new_x][new_y] == 1 and not visited_list[new_x][new_y]:
                graph[new_x][new_y] = graph[x][y] + 1
                queue.append((new_x, new_y))
                visited_list[x][y] = True

BFS(0, 0)
print(graph[n - 1][m - 1])

## 메모리: 34176 KB, 시간: 76 ms
