# BOJ_1874_스택 수열
# 난이도: 실버2
# 풀이 날짜: 23.08.26
# 풀이 시간: 30분

# How to
'''
- N: 수열의 길이
- nums: 수열을 저장한 리스트
- stack: 1 부터의 수를 저장할 스택

1. 첫번째 수가 나올 때까지 stack에 1부터 push 한다.
2. 첫번째 수를 찾은 경우, 해당 수를 다시 pop하고, 다음 찾을 수를 num으로 받는다.
3-1. 만약 찾고자 하는 수가 아직 stack에 저장되지 않았다면, 원하는 수가 저장될 때까지 stack에 push한다.
     원하는 수가 stack에 저장되면 다시 pop해주고 다음 수로 넘어간다.
3-2. 만약 찾고자 하는 수가 stack의 top부분이라면 pop해주고 다음 수로 넘어간다.
3-3. 만약 stack의 top이 찾고자 하는 수보다 크다면, 수열이 완성될 수 없으므로 반복을 중지하고 'NO'를 출력한다.
4. 3-3의 조건에 걸리지 않는 이상 3번을 반복한다.
'''

# Comment
'''
스택문제.. 저번에도 몇번 풀었어서 그런지 쉽게 풀었다.
처음에 break문을 주지 않고 모든 작업이 끝난 후, stack이 비어있지 않으면 'NO'를 출력하게끔 했었다.
그러나 그 경우 시간초과가 발생하여서 중간에 그만두게끔 최적화하였다.
'''


# Code
N = int(input())
nums = []
ANS = []
for _ in range(N):
    nums.append(int(input()))

stack = []
ANS = []
i = 1
for num in nums:
    while(i <= num):
        stack.append(i)
        ANS.append('+')
        i += 1
    
    if len(stack) > 0 and stack[-1] == num:
        stack.pop()
        ANS.append('-')
        continue
    elif stack[-1] > num:
        print('NO')
        break

if len(stack) == 0:
    for a in ANS:
        print(a)
    


## 메모리: 36696 KB, 시간: 3872 ms