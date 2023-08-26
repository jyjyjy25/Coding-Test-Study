# BOJ_11003_최솟값 찾기
# 난이도: 플레티넘5
# 풀이 날짜: 23.08.22
# 풀이 시간: 총 1시간 40분
'''
1차적으로 50분 고민하다 못품
2차적으로 30분정도 추가로 풀었으나 시간초과를 해결하지 못함.
3차적으로 책의 풀이를 그냥 보고 이해하고 멈추었다.. 20분정도.
'''

# How to
'''
1. 순서대로 deque에 인덱스와 값을 넣어준다.
2. 새로운 값이 들어올 때마다 최솟값을 기준으로 정렬되게끔 한다. 
   - 새로운 값보다 큰 수는 pop해버리고 값을 넣는다.
   - 인덱스를 초과하는 수가 있다면 pop 해준다.
3. 맨 앞의 수를 출력한다.(최솟값이니까)
'''

# Comment
'''
deque를 이용하여 최솟값과 관련된 인덱스들에 대해서만 정렬된 채로 유지하는것이 핵심이였다.

우선 내가 생각한 방식대로 풀어보았는데, 맨 밑의 코드는 시간초과가 날 줄 알면서 그냥 풀었다
두번째로 푼 코드는 조건에 따라 순회하지 않아도 되도록 하였지만 여전히 시간초과를 면할 수는 없었다.

마지막으로 그냥 책을 보고 풀었다.
다만 알고리즘을 이해하는거와 별개로 나를 헷갈리게 한 부분은 다음과 같다.
책에서는 (인덱스, 값) 순으로 deque에 넣어놓고, 코드에서는 (값, 인덱스) 순으로 넣어놨다. (일부런가..;;)
'''

# Code
from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
numbers = list(map(int, input().split()))
dq = deque()

for i in range(N):
    while dq and dq[-1][0] > numbers[i]:
        dq.pop()
    dq.append((numbers[i], i))
    if dq[0][1] <= i - L:
        dq.popleft()
    print(dq[0][0], end=' ')

## 메모리: 756276 KB, 시간: 7764 ms

'''
# 최솟값을 기억하고 최솟값이 탈락되지 않는 이상 매번 찾지 않도록함. 또한, 새로들어갈 값이 최솟값보다 작으면 업데이트 하도록 하였음.
# 3% 쯤에서 시간초과 발생함. 아무래도 find_min함수로 소모되는 시간이 많아서 그럴 듯 하다.
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
numbers = list(map(int, input().split()))

def find_min(i):
    if i < L:
        return min(numbers[:i] + numbers[i-L:])
    
    else:
        return min(numbers[i-L:i])

D = ""
minimum = find_min(1)
D += str(minimum)+ " "
for i in range(2,N+1):
    # 이번에 제외되는 부분이 minimum과 같다면 다시 찾는다.
    if minimum == numbers[i-L-1]:
        minimum = find_min(i)
    if minimum > numbers[i-1]:
        minimum = numbers[i-1]
    D += str(minimum)+ " "

print(D)
'''

'''
# 시간초과가 나지만 가장 간단한 방법으로 풀어본 버전.
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
numbers = list(map(int, input().split()))

def find_min(i):
    if i < L:
        return min(numbers[:i] + numbers[i-L:])
    
    else:
        return min(numbers[i-L:i])

D = ""

for i in range(1,N+1):
    D += str(find_min(i))
    D += " "

print(D)
'''


