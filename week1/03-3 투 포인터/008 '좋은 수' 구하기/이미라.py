# BOJ_1253_좋다
# 난이도: 골드5
# 풀이 날짜: 23.08.19
# 풀이 시간:

# How to

# - 투 포인터 개념을 적용하지 못해서 코드 참고
# - (문제를 풀 때 책이 없었음...)

# Code

n = int(input())
nums = sorted(map(int, input().split()))

answer = 0


def two_pointer(li, target):
    global answer

    start, end = 0, len(li) - 1

    while start < end:
        s = li[start] + li[end]
        if target == s:
            answer += 1
            return
        elif target > s:
            start += 1
        elif target < s:
            end -= 1


for i in range(n):
    two_pointer(nums[:i] + nums[i+1:], nums[i])

print(answer)

## 메모리: 31256 KB, 시간: 416 ms