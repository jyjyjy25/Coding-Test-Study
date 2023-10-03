# BOJ_11004_K번째 수
# 난이도: 실버 5
# 풀이 날짜: 23.09.24
# 풀이 시간: 14분

# How to
"""
1. N, M, arr를 입력받는다.
2. arr를 오름차순으로 정렬한다.
3. M - 1에 해당하는 숫자를 출력한다.
"""

# Comment
"""
- int(input())으로 입력받으면 런타임 에러가 발생한다...
"""

# Code
import sys

N, M = map(int, sys.stdin.readline().split() )
arr = list( map(int, sys.stdin.readline().split()))

arr.sort()

print(arr[M - 1])

## 메모리: 623208 KB, 시간: 3960 ms