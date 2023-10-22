# BOJ_1931_회의실 배정하기
# 난이도: 실버1
# 풀이 날짜: 23.10.15
# 풀이 시간: 약 25분

# How to
"""
문제의 자잘한 조건을 잘 챙겨야 할 것 같다.
1. 이전 회의가 종료되자 마자 새로운 회의를 시작할 수 있다. -> 종료 시간 이후에 시작하는 회의를 탐색할 때 등호(=) 필요
2. 회의의 시작 시간과 끝나는 시간이 같을 수 있다. -> 종료 시간을 기준으로 정렬
3. 회의 시작 시간은 0부터 가능하다. -> end를 -1로 초기화
"""

# Comment
"""
"""

# Code
import sys

N = int(sys.stdin.readline().strip())

A = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    A.append((end, start)) # 종료 시간을 기준으로 정렬하기 위해 end를 0번째에 삽입

A.sort()

end = -1 # 0부터 회의가 시작할 수 있는 시간이므로 -1로 초기화
cnt = 0
for t in A:
    if t[1] >= end:  # 이전 회의가 종료되자 마자 새로운 회의를 시작할 수 있으므로 = 필요
        end = t[0]
        cnt += 1

print(cnt)

## 메모리: 44580 KB, 시간: 228 ms