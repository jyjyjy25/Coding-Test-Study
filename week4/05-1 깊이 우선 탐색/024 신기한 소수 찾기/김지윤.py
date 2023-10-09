# BOJ_2023_신기한 소수 찾기
# 난이도: 골드5
# 풀이 날짜: 23.10.09
# 풀이 시간: 약 28분

# How to
"""
1. 자릿수가 한 개이면서 소수인 수는 2, 3, 5, 7이다.
2. 2부터 DFS 탐색을 시작한다.
    2-1. 자릿수가 N일 경우 값을 출력한다. 이때 문제의 요구대로 오름차순 정렬되어 출력된다.
    2-2. 2 * 10에 i를 더한 값이 소수인지 확인한다. 이때 i가 2의 배수일 경우 무조건 소수가 아니므로 이 경우는 제외한다.
    2-3. 소수일 경우 (2)를 반복한다.
"""

# Comment
"""
처음엔 N자리 중 소수를 찾고 소수일 경우 N-1, N-2, N-3 ... 자리의 값이 소수인지 판별하려고 했다.
하지만 반대로 자릿수가 한 개인 소수부터 시작하는게 더 효율적인 걸 보고 유레카였다.
"""


# Code
import sys
import math
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())


def is_prime(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


def DFS(x):
    if len(str(x)) == N:
        print(x)
    else:
        for i in range(1, 10, 2):
            if is_prime(x * 10 + i):
                DFS(x * 10 + i)


prime_num = [2, 3, 5, 7]
for p in prime_num:
    DFS(p)


## 메모리: 33376 KB, 시간: 44 ms