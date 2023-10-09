# BOJ_2023_신기한 소수
# 난이도: 골드5
# 풀이 날짜: 23.10.09
# 풀이 시간: 30분

# How to
# 1. n을 받는다
# 2. 소수를 구하는 함수를 짠다
# 3. 자리수가 n과 동일하면 출력하고 아니면 재귀함수를 돌림

# Comment
# 자리수가 n과 동일할 때를 어떻게 할지 모르겠어서 교재 참고함
# 근데 지금보니까 짝수를 제거하는 조건은 필요없을듯

# Code
import sys
n = int(sys.stdin.readline().strip())

def prime(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True

def DFS(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(1, 10):
            if (num*10 + i)%2 != 0 and prime(num*10 + i):
                DFS(num*10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)


## 메모리:  31256KB, 시간:  7316ms