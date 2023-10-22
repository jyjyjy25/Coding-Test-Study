# BOJ_1715_카드 정렬하기
# 난이도: 골드4
# 풀이 날짜: 23.10.22
# 풀이 시간: 30분

# How to
# 1. 우선순위 큐를 사용하여 값을 넣으면 알아서 정렬하도록 한다
# 2. 가장 작은 두 수의 합을 sum에 더하면서 큐에 추가해준다(작은 값들 갱신)

# Comment
# 정렬 후 순서대로 더하면 무조건 최소가 된다고 생각해서 좀 헤맸다.

# Code
from queue import PriorityQueue
import sys
n = int(sys.stdin.readline())
q = PriorityQueue()

for _ in range(n):
    q.put(int(sys.stdin.readline().strip()))

sum = 0
for _ in range(n-1):
    tmp = q.get() + q.get()
    sum += tmp
    q.put(tmp)

print(sum)

''' 출력 초과
import sys
n = int(sys.stdin.readline())
arr = list(int(sys.stdin.readline().strip()) for _ in range(n))
arr.sort()

sum = arr[0] + arr[1]
for i in range(2, n):
    sum = sum*2 + arr[i]

print(sum)
'''

## 메모리:  37564KB, 시간:  560ms