# BOJ_1744_수 묶기
# 난이도: 골드4
# 풀이 날짜: 23.10.14
# 풀이 시간: 40분

# How to
'''
    1보다 큰 양수, 음수, 1, 0으로 구분하여 저장한다. 이때, 1과 0은 개수만 카운트한다.
    음수의 경우)
        두 수를 곱하면 양수가 되는 것을 이용하여 가장 작은수(절댓값이 큼)들부터 묶는다.
        다만 짝수개가 아닐 경우, 가장큰수(절댓값이 작음)에 대하여 다음 과정을 적용한다.
        - 만약에 음수 하나만 남았고, 0이 존재한다면 0과 묶어서 곱이 0이되도록한다.
        - 만약에 음수가 하나만 남았고, 0이 존재하지 않는다면 그냥 그대로 더한다. 
    1보다 큰 양수의 경우)
        가장 큰 두 수부터 차례대로 묶어주어 합이 크게 한다.
    1의 경우)
        1 두개를 각각 더하면 2가되지만, 둘을 묶어서 더할 경우 1이된다.
        따라서, 무조건 1은 묶지 않고 더한다.
'''

# Comment
'''
    처음에 틀렸던 이유: 1이 여러개 있을 경우, 1끼리 곱하면 손해이다.
    애매하게 25%까지 간 이유가 흔한 케이스가 아니라 그런 듯하다..
    1의 개수도 따로 저장하여 해결하였다.
'''

# Code

import sys
input = sys.stdin.readline

N = int(input())
zero = 0
one = 0
minus = []
plus = []
for _ in range(N):
    tmp = int(input())
    if tmp > 1: plus.append(tmp)
    elif tmp < 0: minus.append(tmp)
    elif tmp == 1: one += 1
    else: zero += 1

minus.sort()
plus.sort()

ANS = one

if len(minus)%2 != 0: # 홀수개 인 경우
    # 음수 중 가장 큰 수를 0이 있다면 0과 묶고, 아니라면 그냥 그대로 정답에 더한다.
    if zero > 0: 
        minus.pop() 
    else:
        ANS += minus.pop()

minus.reverse()
while minus:
    ANS += minus.pop() * minus.pop()

if len(plus)%2 != 0:
    ANS += plus.pop(0)
while plus:
    ANS += plus.pop() * plus.pop()

print(ANS)
    

## 메모리: 31120 KB, 시간: 40 ms

# 25%에서 틀렸습니다
'''
import sys
input = sys.stdin.readline

N = int(input())
zero = 0 
minus = []
plus = []
for _ in range(N):
    tmp = int(input())
    if tmp > 0: plus.append(tmp)
    elif tmp < 0: minus.append(tmp)
    else: zero += 1

minus.sort()
plus.sort()
plus.reverse()

ANS = 0
for i in range(0,len(minus),2):
    if i+1 < len(minus):
        ANS += minus[i] * minus[i+1]
    else:
        if zero > 0: zero -= 1
        else: ANS += minus[i]
for i in range(0,len(plus),2):
    if i+1 < len(plus):
        ANS += plus[i] * plus[i+1]
    else:
        ANS += plus[i]

print(ANS)
'''