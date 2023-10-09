# BOJ_2023_신기한 소수
# 난이도: 골드 5
# 풀이 날짜: 23.10.07
# 풀이 시간: 32분

# How to
"""
1. 수를 입력받는다.
2. 1의 자리 2, 3, 5, 7로 시작하여 DFS를 실행한다.
    입력받은 수의 자릿수가 n과 동일하면 그 수를 출력한다.
    동일하지 않은 경우 * 10을 하고 새로운 1의 자리 수를 더해주어야 한다.
        새로운 1의 자리 수 i가 짝수인지 확인한다.
        새로운 1의 자리 수 i가 소수인지 확인한다.
        위의 두 경우를 만족하는 경우 DFS()를 실행한다.
"""

# Comment
"""
- 천의 자리에서 내려오면서 확인을 해야하나, 1의 자리에서 올라가야 하는가를 고민했었는데 1에서 올라가면 2, 3, 5, 7로 경우를 줄일 수 있었다.
"""

# Code
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())

def is_prime(num) -> bool:
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True

def DFS(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if is_prime(num * 10 + i):
                DFS(num * 10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)

## 메모리: 31256 KB, 시간: 6912 ms