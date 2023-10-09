# BOJ_11724_연결 요소의 개수
# 난이도: 실버5
# 풀이 날짜: 23.10.09
# 풀이 시간: 30분

# How to
# 1. 인접 리스트와 방문여부 리스트 생성
# 2. 방문 여부 T/F만 파악하면 되므로 for문을 돌면서 False면 DFS로 보냄

# Comment
# DFS 함수 어떻게 짜야할 지 감이 잘 안 와서 책 참고함
# 그냥 돌렸더니 RecursionError가 떠서 검색해보니까 백준 채점시스템에선 최대 재귀 깊이를 1000으로 해놓고 이 에러는 그걸 초과해서 나는 거라고 함
# 그래서 sys.setrecursionlimit로 제한을 풀어줌

# Code
import sys
sys.setrecursionlimit(100000)
n, m = map(int, sys.stdin.readline().strip().split(' '))
nearList = [[] for _ in range(n+1)]
isVisited = [False] * (n+1)

def DFS(node):
    isVisited[node] = True
    for i in nearList[node]:
        if not isVisited[i]:
            DFS(i)

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    nearList[a].append(b)
    nearList[b].append(a)

count = 0
for i in range(1, n+1):
    if not isVisited[i]:
        count += 1
        DFS(i)

print(count)


## 메모리:  65192KB, 시간:  712ms