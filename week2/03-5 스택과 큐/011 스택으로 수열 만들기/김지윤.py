# BOJ_1874_스택으로 수열 만들기
# 난이도: 실버3
# 풀이 날짜: 23.08.27
# 풀이 시간: 약 38분

# How to
"""
1. i를 1씩 증가시키면서 stack에 push(+)한다. (1<=num일 경우에만)
2. 1>num일 경우 stack에서 pop(-)한다.
    이때 수열을 담는 리스트(sequence)에 pop한 값을 append한다. 나중에 수열(num_list)과 비교하여 수열을 만들수 있는지 여부를 판단하기 위함이다.
3. 수열(num_list)과 수열을 담는 리스트(sequence)를 비교하여 같으면 연산 순서를 출력하고, 다를 경우 NO를 출력한다.
"""

# Comments
"""
수열을 만들 수 없는 경우에 대해 명확하게 정의내리지 못해서 결국 수열과 비교해서
같으면 만들 수 있고, 다르면 만들 수 없다로 구현했다.
근데 교재 코드에서도 수열을 만들지 못한다는 것을 알게 되더라도 for 문은 끝까지 순회하는 걸 보아 시간복잡도는 큰 차이가 없을 것 같다.
"""

# Code
import sys

N = int(sys.stdin.readline())
num_list = []  # 정답 수열 리스트
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

stack = []
i = 1
sequence = []  # 수열을 담는 리스트
answer = []  # 연산 순서를 담는 리스트
for num in num_list:
    while (1):
        if i <= num:
            stack.append(i)
            i += 1
            answer.append('+')
        else:
            sequence.append(stack.pop())
            answer.append('-')
            break

if sequence == num_list:
    for a in answer:
        print(a)
else:
    print('NO')

## 메모리: 40552 KB, 시간: 196 ms