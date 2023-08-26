# BOJ_17298_오큰수
# 난이도: 골드4
# 풀이 날짜: 23.08.27
# 풀이 시간: 1시간
# How to
'''
1. 수열을 차례대로 받는다.
2. 스택이 비어있으면 수열을 스택에 push한다.
3. 스택이 비어있지 않으면 스택 최상위의 인덱스의 값과 그다음으로 넣을 값을 비교한다.
   스택 최상위 인덱스의 값보다 새로운 값이 큰 경우) 기존 스택에 있는 값을 pop()하고 새로운 값을 해당 인덱스에 채운다.
   스택 최상위 인덱스의 값보다 새로운 값이 작은 경우) 새로운 값의 인덱스를 스택에 push()한다.
4. 수열의 길이만큼 반복한 이후에 남은 스택의 인덱스에 모두 -1을 저장한다.
'''

# Comment
'''
처음에 스택으로 풀 방법이 전혀 생각이 나지 않았다.
그래서 스스로 생각한 방법론으로 풀었다.
예제 입력/출력값에 대해서는 잘 나오는데, 제출하면 1%에서 틀렸다고 나온다.
왜!!!!
'''

# Code

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ANS = [-1 for _ in range(N)]
print(ANS)

stack = []
for i in range(N):
    while(len(stack) != 0 and A[stack[-1]] < A[i]):
        ANS[stack.pop()] = A[i]
    stack.append(i)

print(*ANS)

## 메모리: 155568 KB, 시간: 1208 ms

'''
# 틀렸으나, 어떤 반례가 있는지 궁금한 코드... 1%에서 틀린다.
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ANS = []

def find_NGE(id):
    tmp = id+1
    for a in A[id+1:]:
        if A[id] < a:
            return tmp, a
        else:
            tmp += 1
    return None, -1

NGE_idx = None
NGE_value = None
for idx in range(N):
    if NGE_idx == None:
        NGE_idx, NGE_value = find_NGE(idx)
    ANS.append(NGE_value)
    
    if idx+1 == NGE_idx:
        NGE_idx = None
    
print(*ANS)
'''