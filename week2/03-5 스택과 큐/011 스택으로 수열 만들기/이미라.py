# BOJ_1874_스택으로 수열 만들기
# 난이도: 실버 3
# 풀이 날짜: 23.01.01
# 풀이 시간: 22분

# How to
"""
1. 입력한 수를 만날 때까지 오름차순으로 push 한다.
2. 입력한 수를 만나면 반복문을 탈출한다.
    cur 이라는 변수를 사용해서 입력한 숫자와 같은지 확인한다.
    -> 이거 간단하게 while문 돌리기 좋은 방법인 것 같음
3. stack의 TOP이 입력한 숫자와 같으면 TOP을 꺼내 수열을 만든다.
    but, TOP이 입력한 수가 아니라면 스택을 만들 수 없다. 
    -> TOP이 num(: 입력한 수)보다 크면 num은 TOP 보다 아래에 위치하기 때문
"""

# Comment
"""
- 3번 부분 예외처리를 생각하지 못해서 애를 조금 먹었다.
"""

# Code

import sys
input = sys.stdin.readline

n = int(input())

stack = []
result = []

flag = 0
cur = 1

for i in range(n):
    num = int(input())

    while cur <= num:
        stack.append(cur)
        result.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        flag = 1
        break               

if flag == 0:
    for i in result:
        print(i)


## 메모리: 32840 KB, 시간: 192 ms