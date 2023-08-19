# BOJ_1940_주몽의 명령
# 난이도: 실버 4
# 풀이 날짜: 23.08.20
# 풀이 시간:

# How to
'''
1. 입력받은 재료 리스트를 오름차순으로 정렬한다.
2. start_pointer와 end_pointer를 지정하고 조건에 따라 포인터의 값을 변경한다.
    start_pointer에 해당하는 리스트 값을 s, end_pointer에 해당하는 리스트의 값을 e라고 할 때,
    2-1. s + e < M 일 경우, start_pointer 1 증가
    2-2. s + e > M 일 경우, end_pointer 1 감소
    2-3. s + e == M 일 경우, start_pointer 1 증가 & end_pointer 1 감소
'''

# Code
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
items = list(map(int, sys.stdin.readline().split()))

cnt = 0
start_pointer = 0
end_pointer = N - 1

items.sort()
while (start_pointer < end_pointer):
    if (items[start_pointer] + items[end_pointer] < M):
        start_pointer = start_pointer + 1
    elif (items[start_pointer] + items[end_pointer] > M):
        end_pointer = end_pointer - 1
    else:
        cnt = cnt + 1
        end_pointer = end_pointer - 1
        start_pointer = start_pointer + 1

print(cnt)

## 메모리: 32276 KB, 시간: 52 ms