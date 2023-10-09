# BOJ_13023_ABCDE
# 난이도: 골드 5
# 풀이 날짜: 23.10.07
# 풀이 시간: 36분

# How to
"""
1. 데이터를 저장할 data_list, 노드 방문 여부를 저장할 visited_list를 초기화 한다.
2. 값을 입력받는다.
3. 각 노드는 양방향으로 연결되므로 각각 append() 해준다.
4. DFS를 진행한다.
    총 5번의 친구 관계가 생성되어야 하는 것을 깊이(depth)으로 표시하였다. depth == 5인 경우 바로 1을 출력하고 함수를 빠져나온다.
    그렇지 않은 경우, 계속해서 DFS()를 실행한다.
5. 모든 경우를 탐색 후(다섯 관계가 나타나지 않은 경우), 0을 출력한다.
"""

# Comment
"""
- 재귀함수를 호출하는 DFS 특성 상 정답(depth == 5)을 return 값을 주면 어디선가 꼬일 수도 있을 것 같아 exit() 하였다.
"""

# Code
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
data_list = [[] for _ in range(n + 1)]
visited_list = [False] * (n + 1)

def DFS(index, depth):
    if depth == 5:
        print(1)
        exit()

    visited_list[index] = True
    for i in data_list[index]:
        if not visited_list[i]:
            DFS(i, depth + 1)
    visited_list[index] = False

for _ in range(m):
    a, b = map(int, input().split())
    data_list[a].append(b)
    data_list[b].append(a)
    
for i in range(n):
    DFS(i, 1)

print(0)


## 메모리: 31388 KB, 시간: 724 ms