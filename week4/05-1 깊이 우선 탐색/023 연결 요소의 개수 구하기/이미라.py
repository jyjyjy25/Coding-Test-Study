# BOJ_11724_연결 요소의 개수
# 난이도: 실버 5
# 풀이 날짜: 23.10.07
# 풀이 시간: 12분

# How to
"""
1. 데이터를 저장할 data_list, 노드 방문 여부를 저장할 visited_list를 초기화 한다.
2. 값을 입력받는다.
3. 각 노드는 양방향으로 연결되므로 각각 append() 해준다.
4. DFS를 진행한다.
    이때 1 ~ n+1 만큼 반복해야 한다.(첫 번째는 세지 않으므로)
    visited_list[i] == False 이면 탐색하지 않았음을 의미하므로 count++ 하고 DFS()함수를 호출한다.
5. count를 출력한다. 
"""

# Comment
"""

"""

# Code
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
data_list = [[] for _ in range(n + 1)]
visited_list = [False] * (n + 1)

def DFS(v):
    visited_list[v] = True
    for i in data_list[v]:
        if not visited_list[i]:
            DFS(i)

for _ in range(m):
    a, b = map(int, input().split())
    data_list[a].append(b)
    data_list[b].append(a)

count = 0

for i in range(1, n + 1):
    if not visited_list[i]:
        count += 1
        DFS(i)

print(count)


## 메모리: 65168 KB, 시간: 672 ms