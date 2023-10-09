# BOJ_2178_미로탐색
# 난이도: 실버1
# 풀이 날짜: 23.10.09
# 풀이 시간:

# How to
# 1. n, m, 미로가 되는 값들을 받음

# Comment
# 미로를.. 어케 탐색해야할지 모르겠슴

# Code
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split(' '))
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
print(maze)

def bfs(x, y):
    queue = deque([x, y])

    while queue:
        x, y = queue.popleft()


## 메모리:  KB, 시간:  ms