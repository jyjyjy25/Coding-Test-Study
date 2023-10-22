# BOJ_1744_수를 묶어서 최댓값 만들기
# 난이도: 골드4
# 풀이 날짜: 23.10.15
# 풀이 시간: 약 35분

# How to
"""
양수든 음수든 큰 수끼리 묶여야 큰 값을 만들어낼 수 있다.
양수와 음수를 각각의 리스트로 저장해둔다. 하지만 이때 0과 1은 묶어서 계산할 때 방해가 되므로 따로 저장해둔다.
∵) 4 3 2 1로 수열이 내림차순 정렬되어 있을 때 4*3 + 2*1 보다 4*3 + 2 + 1로 계산해야 더 큰 값이 나온다.

양수 리스트는 내림차순으로 정렬한 뒤 2개씩 묶어 곱한 뒤 더한다.
이때 양수 리스트 내의 요소의 개수가 홀수일 경우 나중에 따로 더한다.

음수 리스트는 오름차순으로 정렬한 뒤 2개씩 묶어 곱한 뒤 더한다.
이때 음수 리스트 내의 요소의 개수가 홀수이면서 0이 존재할 경우 0을 곱해서 더하고, 0이 존재하지 않을 경우엔 그대로 더한다.
"""

# Comment
"""
"""

# Code
import sys

N = int(sys.stdin.readline().strip())

pos_nums = []
nag_nums = []
one = 0
zero = 0

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x > 1:
        pos_nums.append(x)
    elif x < 0:
        nag_nums.append(x)
    elif x == 1:
        one += 1
    elif x == 0:
        zero += 1

sum = 0

pos_nums.sort(reverse=True)
for i in range(0, len(pos_nums) - 1, 2):
    sum += pos_nums[i] * pos_nums[i+1]

# 양수의 개수가 홀수일 경우
if len(pos_nums) % 2 == 1:
    sum += pos_nums[-1]

nag_nums.sort()
for i in range(0, len(nag_nums) - 1, 2):
    sum += nag_nums[i] * nag_nums[i+1]

# 음수의 개수가 홀수일 경우
if len(nag_nums) % 2 == 1:
    if zero != 0:
        sum += 0
    elif zero == 0:
        sum += nag_nums[-1]

# 남은 1 더하기
sum += one

print(sum)


## 메모리: 31120 KB, 시간: 44 ms