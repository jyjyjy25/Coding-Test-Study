# BOJ_1253_좋다
# 난이도: 골드4
# 풀이 날짜: 23.08.20
# 풀이 시간: 20분

# How to
'''
바로 이전 문제를 거의 그대로 가져왔다.
단, 자기자신을 제외한 두 수의 합이어야 하기 때문에, 현재 대상이 되는 숫자의 인덱스 일 경우를 예외처리했다.
애초에 count 하는 부분에서 예외를 처리하면 됬었는데, 그 부분이 아닌 밑에 i, j를 변경하는 부분에서 예외처리를 했더니 오류가 났다.
현재는 왜 오류가 났었나 알아냈지만, 코드리뷰 하는 스터디원이 아래가 왜 틀렸는지 맞추라는 의미로 첨부하였다 ㅎ
'''

# Code
import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))
nums.sort()

count = 0
for idx, num in enumerate(nums):
    i = 0; j = len(nums)-1
    while (i < j):
        sum = nums[i] + nums[j]
        if sum == num:
            if i == idx:
                i += 1
            elif j == idx:
                j -= 1
            else:
                count += 1
                break
        elif sum < num:
            i += 1
        else: 
            j -= 1

print(count)

'''
# 첨에 푼 거
for idx, num in enumerate(nums):
    i = 0; j = len(nums)-1
    while (i < j):
        sum = nums[i] + nums[j]
        if sum == num:
            count += 1
            break
        elif sum < num:
            i += 1
            if i == idx: i += 1
        else: 
            j -= 1
            if j == idx: j -= 1
'''
## 메모리: 31256 KB, 시간: 1144 ms