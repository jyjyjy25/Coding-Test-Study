# BOJ_2750_수 정렬하기 1
# 난이도: 브론즈1
# 풀이 날짜: 23.09.01
# 풀이 시간: 약 9분

# How to
"""
1. 정렬할 숫자를 하나씩 입력받아 nums에 append한다.
2. 두 수를 비교하는 횟수인 N-1번만큼 for 문을 순회한다.
3. 두 수를 비교하여 더 큰 수가 왼쪽에 있을 경우 오른쪽으로 swap한다. 즉, 오름차순 정렬한다.
"""

# Comment
"""
백준에 제출하면서 11달 전에 제출했던 코드가 있길래 다시 한 번 봤다.
왜 저렇게 난해하게 짰나 싶다.
이렇게 실력이 늘고 있음을 느끼는 것 같다.
"""

# Code
import sys

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))

for i in range(N-1):
    for j in range(N-1-i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

for n in nums:
    print(n)


## 메모리: 31256 KB, 시간: 184 ms