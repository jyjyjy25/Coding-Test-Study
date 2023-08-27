# BOJ_17298_오큰수 구하기
# 난이도: 골드 4
# 풀이 날짜: 23.08.27
# 풀이 시간:

# How to
"""
1. 값을 입력받는다.
2. 정답 수열을 -1로 초기화 한다.
3. 현재 수열이 스택 TOP 보다 클 경우 정답 리스트에 오큰수를 삽입한다.
"""

# Comment
"""
1. 값을 입력받는다.
2. 현재 수열이 스택 TOP 보다 클 경우 정답 리스트에 오큰수를 삽입한다.
3. 만약 수열을 다 돌았는데 스택이 비어있지 않으면 정답 리스트에 -1을 삽입한다.

위와 같은 순서로 코드를 짰을 때 시간초과 오류가 발생했다. 스택이 비어있는지 확인하지 않고 정답 리스트에 -1을 넣어놓은 상태로 하면 어떨까 생각했다.
하지만 그렇게 했어도 시간 초과 오류가 발생했다. 반복문으로 정답 리스트를 출력하는 과정에서 오류가 발생한 것 같다.
    print(*ans) : ans 리스트의 모든 요소를 공백으로 구분하여 출력한다.
출력하는 과정을 위와 같이 하였더니 오류가 발생하지 않았다.
"""

# Code

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
ans = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and array[stack[-1]] < array[i]:
        ans[stack.pop()] = array[i]
    stack.append(i)

print(*ans)

# 시간초과 오류 발생 코드

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
ans = [0] * n
stack = []

for i in range(n):
    while stack and array[stack[-1]] < array[i]:
        ans[stack.pop()] = array[i]
    stack.append(i)

while stack:
    ans[stack.pop()] = -1

result = ""
for i in range(n):
    result += str(ans[i]) + " "

print(result)

## 메모리: 155560 KB, 시간: 1088 ms