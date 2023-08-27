# BOJ_11003_최솟값 찾기 1
# 난이도: 플래티넘
# 풀이 날짜: 23.08.27
# 풀이 시간: 약 50분

# How to
"""
1. deque를 사용하여 인덱스와 값을 튜플로 저장한다.
2. D[-1]의 값이 현재 수열의 값보다 크다면 D.pop()한다.
3. D[0]의 인덱스가 i-L보다 작거나 같다면 D.popleft()한다.
"""

# Comment
"""
문제 이해는 바로 한 것 같은데 어떻게 풀어야 할 지는 감이 안왔다.
2중 for 문은 무조건 아닐 것 같았기 때문에..
deque를 사용해야 한다는 힌트를 보고 도전은 해봤지만 결국 교재의 코드를 공부하자로 마인드를 변경했다.
"""

# Code
import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
D = deque()

answer = []
for i, a in enumerate(A):
    while D and D[-1][1] > a:
        D.pop()
    D.append((i, a))
    
    if D[0][0] <= i - L:
        D.popleft()
    print(D[0][1], end=' ')

## 메모리: 755224 KB, 시간: 7304 ms