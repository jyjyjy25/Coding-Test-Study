# BOJ_1300_K번째 수
# 난이도: 골드1
# 풀이 날짜: 23.10.14
# 풀이 시간: 20분 + 30분

# How to


# Comment
'''
    현재까지 발견한 법칙(?)
    N이 홀수일 때 N/2의 제곱보다 작은수가 N!-1개 존재함
    N이 짝수일 때 (N/2)*((N/2)+1)가 2개 존재, 보다 작은수가 N!-2개 존재함
    ...
'''

# Code

N = int(input())
k = int(input())



## 메모리:  KB, 시간:  ms

# 생각하기 전에 일단 간단하게 풀어본 버전. 생각 외로 시간초과가 아닌 매모리초과가 낫다
'''
N = int(input())
k = int(input())
B = []
for i in range(1, N+1):
    for j in range(1, N+1):
        B.append(i*j)

B.sort()
print(B[k])
'''