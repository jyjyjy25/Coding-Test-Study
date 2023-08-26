# BOJ_1940_주몽
# 난이도: 실버4
# 풀이 날짜: 23.08.20
# 풀이 시간: 18분

# How to
'''
이전 문제와 비슷하게 다 받아서 포인터를 이동해가며 풀이하였다.
i < j로 하면 자연히 겹칠 일이 없을건데,, 생각을 못하고 i != j로 했었다.
또, "nums = list(map(int, input().split())).sort()"로 할 경우에 nums에 졍렬된 리스트가 아닌 None이 저장되었다.
이유를 생각해 보기로는, sort() 함수는 호출한 객체의 내용물을 정렬시켜준다. (무언가를 반환 X)
할당 연산자 = 는 제일 마지막에 적용이 되는데, 적용 직전의 상태가 .sort() 인데 이게 반환이 아니라서(?) nums에 할당되지 않는건가 싶다.
'''

# Code
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

nums = list(map(int, input().split()))
nums.sort()

i = 0
j = N - 1
count = 0
while (i < j):
    sum = nums[i] + nums[j]
    if sum == M:
        count += 1
        i += 1; j -= 1
    elif sum < M:
        i += 1
    else: 
        j -= 1

print(count)


## 메모리: 32276 KB, 시간: 52 ms