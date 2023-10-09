# BOJ_1167_트리의 지름
# 난이도: 골드3
# 풀이 날짜: 23.10.09
# 풀이 시간: 1시간

# How to
# 1. n을 받음
# 2. 값들이 들어갈 arr와 방문여부를 파악할 isVisited, 거리를 담을 distance를 만듦
# 3. 입력을 n만큼 받아서 (노드, 거리)순으로 저장되게 함
# 4. bfs를 돌면서 distance를 계산함
# 5. 가장 먼 거리가 나온 노드에서 다시 bfs를 실행하여 지름을 알아 냄

# Comment
# 핵심이 되는 아이디어를 알고 나니 생각보다 수월하게 풀림
# 오히려 배열을 어떻게 받을지가 더 어려웠다

# Code
import sys
from collections import deque
n = int(sys.stdin.readline().strip())
arr = [[] for _ in range(n+1)]
isVisited = [False] * (n+1)
distance = [0] * (n+1)

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
    i = 1
    while i != len(tmp)-1:
        arr[tmp[0]].append([tmp[i], tmp[i+1]])
        i += 2 #두 개씩 뛰어 넘어야 다음 수가 올 수 있음

def bfs(v):
    q = deque()
    q.append(v)
    isVisited[v] = True
    while q:
        node = q.popleft()
        for i in arr[node]:
            if isVisited[i[0]] == False:
                q.append(i[0])
                isVisited[i[0]]=True
                distance[i[0]] = distance[node] + i[1] #i[0]은 node를 경유해야 갈 수 있음음

bfs(1)
second = distance.index(max(distance))
isVisited = [False] * (n+1) #False로 다시 초기화
distance = [0] * (n+1) #0으로 다시 초기화
bfs(second)
print(max(distance))

## 메모리:  76584KB, 시간:  912ms