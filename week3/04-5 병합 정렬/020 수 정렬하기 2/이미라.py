# BOJ_11004_수 정렬하기 2
# 난이도: 실버 5
# 풀이 날짜: 23.09.24
# 풀이 시간: 14분

# How to
"""
1. N, arr를 입력받는다.
2. arr를 오름차순으로 정렬한다.
3. arr의 요소들을 한 줄씩 출력한다.
"""

# Comment
"""
- input() 이 sys.stdin.readline() 보다 느린 이유 :
    input() 내장 함수는 prompt message를 출력하고, 개행 문자를 삭제한 값을 리턴하기 때문에 느리다.
"""

# Code
import sys

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in arr:
    print(i)

## 메모리: 77108 KB, 시간: 1464 ms