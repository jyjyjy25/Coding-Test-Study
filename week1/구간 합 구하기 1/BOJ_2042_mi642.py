# BOJ_2042_구간 합 구하기 1
# 난이도: 실버 3
# 풀이 날짜: 23.08.15
# 풀이 시간:

# How to

# - 선형 합으로 문제를 풀었더니 시간초과 발생
# - 펜윅 트리를 이용해서 해결

# Code

n, m, k = map(int, input().split())  ### 개수, 수 변경 횟수, 구간의 합

num = [int(input()) for _ in range(n)]

for _ in range(m + k):
    a, b, c = map(int,input().split())

    if a == 1:
        num[b - 1] = c
    elif a == 2:
        print(sum(num[b - 1:c]))

import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

arr=[0] * (n + 1)
tree=[0] * (n + 1)

def update(i, num):
    arr[i] += num
    while i <= n:
        tree[i] += num
        i += i & -i

def sum(i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= i & -i
    return res


for i in range(1, n + 1):
    update(i, int(input()))
for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        update(b, c - arr[b])
    else:
        print(sum(c) - sum(b - 1))

## 메모리: 124564 KB,  시간: 2096 ms