# BOJ_2178_미로 탐색
# 난이도: 실버1
# 풀이 날짜: 23.10.8
# 풀이 시간: 1시간 30분

# How to
'''
    0,0 좌표부터 시작하여 너비우선탐색을 진행하였다.
    현재 위치에서 갈 수 있는 사방면을 살펴보고, 지금까지 걸린 횟수를 더한다.
    최종적으로 M,N의 좌표에는 해당 위치까지 도달하는데 걸린 횟수가 저장되게된다.
'''

# Comment
'''
    좀 많이 헤멨다.
    헤메다가 상하좌우를 살피는 부분은 책을 참고하여 작성하였다.

    제일 오래걸렸던 이유는, matrix 라는 2차원 리스트에 저장할 때, 
    (x,y)좌표가 matrix[y][x]에 저장되어있다는 것이였다...

    현재는 삭제했지만, 일일히 매 반복 시의 matrix를 프린트하고 new_x와 new_y를 모니터링하며 오류를 발견하였다.

'''

# Code
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

matrix = [[] for _ in range(N)]
visited = [ [False] * M for _ in range(N)]

for i in range(N):
    line = input().strip()
    for ch in line:
        matrix[i].append(int(ch))

queue = deque()

queue.append((0,0))
visited[0][0] = True

while queue:
    # up, down, left, right
    x_list = [0, 0, -1, 1]
    y_list = [-1, 1, 0, 0]
    x, y = queue.popleft()

    for i in range(4):
        new_x = x + x_list[i]
        new_y = y + y_list[i]

        if new_x < 0 or new_y < 0 or new_x >= M or new_y >= N:
            continue

        if not visited[new_y][new_x] and matrix[new_y][new_x] > 0:
            
            matrix[new_y][new_x] += matrix[y][x]
            visited[new_y][new_x] = True
            queue.append((new_x,new_y))

print(matrix[N-1][M-1])

    

## 메모리: 34140 KB, 시간: 84 ms