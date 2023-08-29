# BOJ_1253_좋다
# 난이도: 골드5
# 풀이 날짜: 23.08.19
# 풀이 시간:

# How to
# 1. i번째 수와 j번째 수를 더한다
# 2. 받아온 배열의 최대값이 두 수를 더한 값보다 크고
#    arr 배열에 두 수를 더한 값이 없을 경우 append 한다.(합의 모든 경우의 수를 arr에 모음)
# 3. for문으로 arr을 돌면서 받아온 배열에 해당 값이 있다면 해당 값의 개수를 good에 더한다.

# Code
import sys #시간 초과
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().strip().split(' ')))

arr = []
good = 0
for i in range(n-1):
    for j in range(i+1, n, 1):
        tmp = numbers[i]+numbers[j]
        if(max(numbers) >= tmp and arr.count(tmp) == 0):
            arr.append(tmp)
print(arr)

for i in range(len(arr)):
    if(numbers.count(arr[i])!=0):
            good += numbers.count(arr[i])

print(good)

## 메모리:  KB, 시간:  ms