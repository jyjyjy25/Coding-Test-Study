# BOJ_11003_최솟값 찾기 1
# 난이도: 플래티넘
# 풀이 날짜: 23.08.27
# 풀이 시간: 46분

# How to
"""
1. 값을 입력받는다.
2. 새로운 원소가 기존의 원소보다 작으면 기존의 원소를 삭제한다.
3. 새로운 원소를 추가한다.
4. 슬라이딩 윈도우 범위를 벗어나는 경우 원소를 삭제한다(맨 앞의 원소 삭제).
"""

# Comment
"""
슬라이딩 윈도우 개념을 문제에 적용하는게 너무 어렵다.
응용 문제를 많이 풀어봐야 할 것 같다.
슬라이딩 윈도우를 이용해 낮은 시간복잡도로 정렬과 같은 효과를 낼 수 있다는 점 유의하자. 
"""

# Code

from collections import deque

import sys
input = sys.stdin.readline
mydeque = deque()

n, l = map(int, input().split())
num = list(map(int, input().split()))

for i in range(n):
    while mydeque and mydeque[-1][0] > num[i]:
        mydeque.pop()

    mydeque.append((num[i], i))

    if mydeque and mydeque[0][1] <= i - l:
        mydeque.popleft()
  
    print(mydeque[0][0], end = " ")


## 메모리: 755244 KB, 시간: 7664 ms