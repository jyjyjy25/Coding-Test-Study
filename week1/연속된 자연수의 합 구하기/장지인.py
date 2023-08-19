# BOJ_2018_수들의 합 5
# 난이도: 실버5
# 풀이 날짜: 23.08.20
# 풀이 시간: 20분

# How to
'''
책에서 풀이해주는 것과 같이 포인터 두개를 이용해서 풀었다.
숫자 N을 표현하는데에 있어서 가장 큰 수는 N/2 + 1일 것이라고 생각했다.
예를들어 99를 표현하는 연속된 숫자 중 가장 큰 수가 포함될 경우가 49+50 인것처럼...
그래서 while문에 조건을 'high < (N/2 + 1)'와 같이 뒀었는데 98퍼센트 정도에서 틀렸다는 결과가 나타났다.
어떤 반례가 있는지 궁금하다..
'''

# Code
import sys
input = sys.stdin.readline

N = int(input())

high = low = sum = count = 1

while(high < N):
    if sum == N:
        count += 1
        high += 1
        sum += high
    elif sum < N:
        high += 1
        sum += high
    else:
        sum -= low
        low += 1

print(count)
    

## 메모리: 31256 KB, 시간: 5240 ms