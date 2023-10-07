# BOJ_2023_신기한 소수
# 난이도: 골드5
# 풀이 날짜: 23.10.8
# 풀이 시간: 30분

# How to
'''
    다음 과정을 반복한다.
        소수를 받아 소수*10~ 소수*10+9 범위 내에서 소수인 수를 찾는다.
        소수라면 DFS함수에 다시 재귀적으로 넣어준다.
        자리수를 만족한다면 출력한다.
    한자리 수 중 소수는 2, 3, 5, 7 이므로, 이 4개의 수들로 시작한다.
'''

# Comment
'''
    소수를 구하는 과정이 꽤나 시간을 소요하기 때문에, 문제가 생기지 않을까 싶었다.
    그러나 이 문제처럼 모든 수에 대해 따지는 게 아니라 몇몇 수만 따지는 경우까지는 괜찮다고 하여 그냥 is_prime 함수를 만들었다.

    오류를 3번정도 보았다.
        1. 시간초과(2~num까지로 나눴었음) -> 2 부터 num/2 + 1로 고쳐서 해결
        2. typeError(num/2가 소수라서..) -> int type으로 바꿔서 해결
        3. recursionlimit 추가.. 잊지말자.
'''

# Code
import sys
sys.setrecursionlimit(10**6)

def DFS(num, N):
    if num >= 10**(N-1):
        print(num)

    else:
        for i in range(num*10,num*10+10):
            if is_prime(i):
                DFS(i, N)

def is_prime(num):
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True

N = int(input())

DFS(2, N)
DFS(3, N)
DFS(5, N)
DFS(7, N)

## 메모리: 31256 KB, 시간: 7248 ms