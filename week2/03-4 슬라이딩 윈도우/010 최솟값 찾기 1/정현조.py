# BOJ_11003_최솟값 찾기
# 난이도: 플레5
# 풀이 날짜: 23.08.26
# 풀이 시간: 2:15:26

# How to
# 1st 도전 때는 투포인터로 해보려고 했는데 시간초과 남
# 다른 방법은 생각이 안나서 책에 있는 코드를 이해하는 식으로 진행함
# 그래서 책이랑 코드 똑같음

# Code
import sys
from collections import deque
N, L = map(int, sys.stdin.readline().strip().split(' '))
aList = list(map(int, sys.stdin.readline().strip().split(' ')))

minDeque = deque()
for i in range(N):
    while minDeque and minDeque[-1][0] > aList[i] : #이 부분이 잘 이해가 안되는듯
        minDeque.pop()
    minDeque.append((aList[i], i))
    if minDeque[0][1] <= i-L:
        minDeque.popleft()
    print(minDeque[0][0], end=' ')
## 메모리:  755336KB, 시간:  7444ms

# Comment
# 까먹고 있던 저 print 방식을 오랜만에 봐서 오. 했다
# 확실히 deque가 편한거 같긴하다 애용해야지