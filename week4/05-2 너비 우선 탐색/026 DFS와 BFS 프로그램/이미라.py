# BOJ_1260_DFS와 BFS
# 난이도: 실버 2
# 풀이 날짜: 23.10.08
# 풀이 시간: 35 분

# How to
"""
1. 값을 입력받는다.
2. 데이터를 저장할 data_list, 노드 방문 여부를 저장할 visited_list를 초기화 한다.
3. 각 노드를 graph로 연결해준다.
4. DFS()를 실행한다.
5. BFS()를 실행한다.
"""

# Comment
"""
- 책을 참고해서 풀었는데, 이상하게 BFS에서 원하는대로 출력되지 않았다. 그래서 다른 방법 찾아보면서 풀었는데 그냥 변수 설정 오류였다.. ㅎㅎ
- 새로운 풀이를 찾으면서 알아낸 새로운 방법이므로 적용해보았다. 이렇게 할 경우 책의 sort() 과정을 거칠 필요가 없어지는 장점이 있다.
    그래프 선언 참고 (https://kill-xxx.tistory.com/entry/Python-DFSBFS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1260-%EA%B7%B8%EB%A6%BC-%ED%92%80%EC%9D%B4)
    실행 결과, 책의 코드가 더 효율적인 것 같다...ㅎㅎ (메모리: 34184 KB, 시간: 76 ms)
"""

# Code
from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def DFS(v):
    print(v, end = ' ')
    visited_list[v] = True

    for i in range(1, n + 1):
        if not visited_list[i] and graph[v][i] == 1:
            DFS(i)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited_list[v] = True

    while queue:
        new_v = queue.popleft()
        print(new_v, end = ' ')

        for i in range(1, n + 1):
            if not visited_list[i] and graph[new_v][i]:
                queue.append(i)
                visited_list[i] = True

n, m, start = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited_list = [False] * (n + 1)
DFS(start)
print()
visited_list = [False] * (n + 1)
BFS(start)

## 메모리: 39576 KB, 시간: 160 ms



# 책의 풀이
from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m, start = map(int, input().split())
data_list = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    data_list[a].append(b)
    data_list[b].append(a)

for i in range(n + 1):
    data_list[i].sort()

def DFS(v):
    print(v, end = ' ')
    visited_list[v] = True

    for i in data_list[v]:
        if not visited_list[i]:
            DFS(i)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited_list[v] = True

    while queue:
        new_v = queue.popleft()
        print(new_v, end = ' ')

        for i in data_list[new_v]:
            if not visited_list[i]:
                queue.append(i)
                visited_list[i] = True

visited_list = [False] * (n + 1)
DFS(start)
print()
visited_list = [False] * (n + 1)
BFS(start)