# BOJ_11047_동전 0
# 난이도: 실버4
# 풀이 날짜: 23.10.14
# 풀이 시간: 10분

# How to
'''
    가장 큰 동전부터 차례대로 확인한다.
    해당 동전을 최대한 몇개 필요한지 '몫'을 통해서 구한다.
    해당 개수만큼 제외하고 남는 금액, 즉 '나머지'를 K로 업데이트한다.
    위 과정을 K가 0이 될 때까지 반복한다.
'''

# Comment
'''
    하하 요즘 알고리즘 강의에서 듣고 있는 파트가 그리디입니다.
'''

# Code
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
ANS = 0

for coin in reversed(coins):
    if K < coin:
        continue
    ANS += int(K/coin)
    K %= coin
    if K == 0:
        break

print(ANS)
    

## 메모리: 31120 KB, 시간: 40 ms