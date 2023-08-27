# BOJ_2018_수들의 합5
# 난이도: 실버5
# 풀이 날짜: 23.08.19
# 풀이 시간:

# How to


# Code

import math

n = int(input())
end = 0
sum = 0
count = 0

    
for start in range(0, n):
    while sum < n and end < n :
        sum += end + 1
        end += 1
    if sum == n:
        count += 1
    sum -= start + 1

print(count)

## 메모리: 33376 KB, 시간: 4548 ms