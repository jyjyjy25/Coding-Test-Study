# BOJ_2178_미로 탐색하기
# 난이도: 실버1
# 풀이 날짜: 23.10.09
# 풀이 시간:

# How to
"""
문제의 키포인트를 정리하자면,
1. 미로 문제에서 이동을 조작하고 싶을 때 x, y에 대한 변화량을 나타내는 dx, dy를 선언한다.
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    또한 움직임을 적용할 때 미로의 범위를 확인해야 한다.
2. 인접 리스트의 값 자체를 이동 횟수로 저장하면서 탐색을 진행한다. (DP와 유사한 방식)
    (nx, ny) 좌표에 대하여 visited[nx][ny] == False and A[nx][ny] == 1을 만족한다면 이는 방문한 적이 없는 노드임을 뜻한다.
    따라서 (x, y) 값에 +1을 한 값은 현재까지 이동한 거리(깊이)가 된다.
"""

# Comment
"""
- 좌표를 다루므로 이를 인덱스로 편하게 접근하기 위해 리스트의 길이를 1씩 증가시켜 선언하였다.
- 처음에 if ~ elif 문으로 상하좌우를 이동했는데 모든 조건이 적용될 수 있으므로 elif 문을 사용하면 안됨을 깨닫고 모두 if 문으로 변경했다.
    구현하면서 코드가 더러움을 느꼈는데, 교재를 보니까 변화량을 이용해서 for 문을 돌리니 가독성이 좋아지더라..
- 깊이를 구하는 방법은 교재를 참고했다.
"""


# Code
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

A = [[]]
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().strip()))
    temp.insert(0, 0)
    A.append(temp)

visited = []
for _ in range(N+1):
    temp = [False] * (M+1)
    visited.append(temp)


def BFS(v, w):
    queue = deque()
    queue.append((v, w))
    visited[v][w] = True
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]

        if N >= x + 1 and x + 1 > 0 and M >= y and y > 0: # 우
            if not visited[x+1][y] and A[x+1][y] == 1:
                queue.append((x+1, y))
                visited[x+1][y] = True
                A[x+1][y] = A[x][y] + 1
        if N >= x - 1 and x - 1 > 0 and M >= y and y > 0: # 좌
            if not visited[x-1][y] and A[x-1][y] == 1:
                queue.append((x-1, y))
                visited[x-1][y] = True
                A[x-1][y] = A[x][y] + 1
        if N >= x and x > 0 and M >= y - 1 and y - 1 > 0: # 하
            if not visited[x][y-1] and A[x][y-1] == 1:
                queue.append((x, y-1))
                visited[x][y-1] = True
                A[x][y-1] = A[x][y] + 1
        if N >= x and x > 0 and M >= y + 1 and y + 1 > 0: # 상
            if not visited[x][y+1] and A[x][y+1] == 1:
                queue.append((x, y+1))
                visited[x][y+1] = True
                A[x][y+1] = A[x][y] + 1


BFS(1, 1)
print(A[N][M])


## 메모리: 34264 KB, 시간: 76 ms