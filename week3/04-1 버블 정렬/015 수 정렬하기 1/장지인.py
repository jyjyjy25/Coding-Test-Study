# BOJ_2750_수정렬하기
# 난이도: 브론즈2
# 풀이 날짜: 23.09.29
# 풀이 시간: 10분

# How to
'''
    1. 정렬할 수들의 개수를 N으로 받는다. 이후, N개의 수들을 차례대로 리스트에 넣는다.
    2. 버블정렬을 수행한다.
'''

# Comment
'''
    나름 버블정렬은 익숙해서 금방 풀 수 있었다.
    input()함수를 많이 써야하길래 sys.stdin.readline함수가 필요한가 싶었지만 없이도 잘 수행되었다.
'''

# Code

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

for i in range(N):
    for j in range(N-1-i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
        
for num in nums:
    print(num)
  

## 메모리: 31256 KB, 시간: 200 ms