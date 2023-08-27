# BOJ_1253_'좋은 수' 구하기
# 난이도: 골드4
# 풀이 날짜: 23.08.20
# 풀이 시간: 약 41분

# How to
'''
1. 입력받은 리스트를 오름차순으로 정렬한다.
2. start_pointer = 0, end_pointer = N-1로 설정한다.
3. 현재 순회하고 있는 인덱스를 i라고 할 때, nums[start_pointer] + nums[end_pointer] == good_num일 경우 (음의 정수도 고려해야 한다.)
    3-1. start_pointer == i일 경우 start_pointer를 1 증가시킨다. 왜냐하면, 순회하고 있는 리스트 값(nums[i])과 0(nums[end_pointer])을 더하면 good_num(nums[i])이 되기 때문이다.
    3-2. end_pointer == i일 경우 end_pointer를 1 감소시킨다. 왜냐하면, 0(nums[start_pointer])과 순회하고 있는 리스트 값(nums[i])를 더하면 good_num(nums[i])이 되기 때문이다.
    3-3. 그 외의 경우에는 좋은 수로 판별하고 나머지 경우의 수를 확인하지 않고 while 문을 빠져나온다.
'''

# Code
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

cnt = 0
for i in range(N):
    start_pointer = 0
    end_pointer = N - 1
    good_num = nums[i]
    while (start_pointer < end_pointer):
        if nums[start_pointer] + nums[end_pointer] < good_num:
            start_pointer += 1
        elif nums[start_pointer] + nums[end_pointer] > good_num:
            end_pointer -= 1
        else:
            if start_pointer == i:
                start_pointer += 1
            elif end_pointer == i:
                end_pointer -= 1
            else:
                cnt += 1
                break

print(cnt)

## 메모리: 31256 KB, 시간: 888 ms