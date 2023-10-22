# BOJ_1744_수 묶기
# 난이도: 골드4
# 풀이 날짜: 23.10.22
# 풀이 시간: 1시간 18분

# How to
# 1. 입력을 1, 1 미만, 1 초과로 나눈다(미만은 최소힙, 초과는 최대힙으로 만든다)
# 2. 1 미만과 1 초과는 안에 값이 없을 때까지 가장 큰 두 값을 곱해 maxSum에 더한다
#    ㄴ 값이 1개일 경우 maxSum에 그냥 더한다
# 3. 1이 들어있는 리스트의 합을 maxSum에 더한다다


# Comment
# 처음엔 여러 경우의 수를 생각해서 만들었는데 보다보니 그냥 1만 분리하면 되는 간단한 일이었다 ㄱ-
# [처음에 생각했던 경우의 수]
# 1. -1, 1, n: -1 + 1 + n > -1 + (1 * n)
# 2. -n, 1, 1: -n + 1 + 1 > -n + (1 * 1)
# 이렇게만 생각해서 0 이하 큐의 마지막, 1 이상 큐에서 마지막 2개 총 3개만 비교하도록 짰는데
# 이러면 1이 3개 이상 있는 경우 적용이 안 된다...
# [최종]
# 1. 1이 끼면 무조건 더하는 게 더 크다

# Code
'''
# oneArr[]를 없애는 게 메모리가 덜 들지 않을까 하고 시도해봤는데 오히려 20KB가 더 들었다 띠용

from queue import PriorityQueue
import sys
n = int(sys.stdin.readline())
underZero = PriorityQueue()
overZero = PriorityQueue()
maxSum = 0

for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp > 1:
        overZero.put((-tmp, tmp))
    elif tmp < 1:
        underZero.put(tmp)
    else:
        maxSum += tmp

while not underZero.empty():
    if underZero.qsize() == 1:
        maxSum += underZero.get()
    else:
        maxSum += (underZero.get() * underZero.get())

while not overZero.empty():
    if overZero.qsize() == 1:
        maxSum += overZero.get()[1]
    else:
        tmp1 = overZero.get()[1]
        tmp2 = overZero.get()[1]
        maxSum += (tmp1 * tmp2)

print(maxSum)
'''
# 코드 중간중간 바꾸는게 짜증나서 걍 첨부터 짬
from queue import PriorityQueue
import sys
n = int(sys.stdin.readline())
underZero = PriorityQueue()
overZero = PriorityQueue()
oneArr = []

for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp > 1:
        overZero.put((-tmp, tmp))
    elif tmp < 1:
        underZero.put(tmp)
    else:
        oneArr.append(tmp)

maxSum = 0
while not underZero.empty():
    if underZero.qsize() == 1:
        maxSum += underZero.get()
    else:
        maxSum += (underZero.get() * underZero.get())

while not overZero.empty():
    if overZero.qsize() == 1:
        maxSum += overZero.get()[1]
    else:
        tmp1 = overZero.get()[1]
        tmp2 = overZero.get()[1]
        maxSum += (tmp1 * tmp2)

maxSum += sum(oneArr)

print(maxSum)


''' 자연수와 0&음수로 분리
from queue import PriorityQueue
import sys
n = int(sys.stdin.readline())
underZero = PriorityQueue()
overZero = PriorityQueue()
comparison = PriorityQueue()

for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp > 0:
        overZero.put((-tmp, tmp))
    else:
        underZero.put(tmp)

maxSum = 0
while not underZero.empty():
    if underZero.qsize() == 1:
        comparison.put(underZero.get())
    else:
        maxSum += (underZero.get() * underZero.get())

while not overZero.empty():
    if overZero.qsize() <= 2:
        comparison.put(overZero.get()[1])
    else:
        tmp1 = overZero.get()[1]
        tmp2 = overZero.get()[1]
        maxSum += (tmp1 * tmp2)

while not comparison.empty():
    if comparison.qsize() >= 2:
        tmp1 = comparison.get()
        tmp2 = comparison.get()
        if tmp1 == 1 or tmp2 == 1:
            maxSum += (tmp1 + tmp2)
        else:
            if comparison.qsize() == 1: #처음에 값이 3개 들어온 경우
                maxSum += tmp1 + (tmp2*comparison.get())
            else:
                if tmp1 <= 0:
                    maxSum += (tmp1+tmp2)
                else:
                    maxSum += (tmp1*tmp2)
    else:
        maxSum += comparison.get()

print(maxSum)
'''

## 메모리:  36820KB, 시간:  96ms