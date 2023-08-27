# BOJ_1940_주몽
# 난이도: 골드5
# 풀이 날짜: 23.08.20
# 풀이 시간:

# How to

# 책의 수도코드를 보면서 작성했음... 결국 코드가 동일해짐

# Code

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
list = list(map(int, input().split()))
list.sort()

count = 0
i = 0
j = n - 1

while i < j:
    if list[i] + list[j] < m:
        i += 1
    elif list[i] + list[j] > m:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)

## 메모리: 32276 KB, 시간: 56 ms