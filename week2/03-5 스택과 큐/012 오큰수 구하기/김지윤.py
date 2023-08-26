# BOJ_17298_오큰수 구하기
# 난이도: 골드4
# 풀이 날짜: 23.08.27
# 풀이 시간: 약 49분

# How to
"""
1. stack에 인덱스를 append한다.
2. stack이 비어있지 않고, sequence_list[stack[-1]]이 다음 수열의 값(sequence_list[i+1])보다 
    작다면, stack의 마지막 요소에 해당하는 인덱스에 다음 수열의 값을 할당한다.
    크거나 같다면, stack의 마지막 요소에 해당하는 인덱스에 -1을 할당한다.
"""

# Comments
"""
왜 틀렸는지 진짜 모르겠다 !!
"""

# Code
import sys

N = int(sys.stdin.readline())
sequence_list = list(map(int, sys.stdin.readline().split()))

stack = []
NGE = [0] * N
for i, s in enumerate(sequence_list):
    stack.append(i)
    if i == N-1:  # 수열의 마지막 값에 대한 NGE는 항상 -1
        NGE[stack.pop()] = -1
        break

    while stack and s < sequence_list[i+1]:
        if sequence_list[stack[-1]] < sequence_list[i+1]:
            NGE[stack.pop()] = sequence_list[i+1]
        else:
            NGE[stack.pop()] = -1
            break

print(*NGE)

## 메모리:  KB, 시간:  ms
## -> 틀렸습니다.