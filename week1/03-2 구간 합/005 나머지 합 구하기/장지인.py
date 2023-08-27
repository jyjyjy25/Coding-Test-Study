# BOJ_10986_나머지 합
# 난이도: 골드3
# 풀이 날짜: 23.08.15
# 풀이 시간: 35분

# How to
'''
오래 걸렸지만, 이것도 책 덕분에 더 빨리 푼거라는 생각이 드는 문제.
'i까지의 구간합' % M과 'j까지의 구간합' % M이 같다면, 'i에서 j+1 까지의 구간 합' % M은 0이다.
-> 이 말을 이해하는데 겁나 오래걸렸다.

이 문제에서 기억해야할 것은 같은 값이 몇번 나왔는지를 체크하는데에 list의 index를 사용했던 점인 것 같다.
'''

# Code
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
ANS = 0

sums = [nums[0]]
for i in range(1, N):
    sums.append(sums[i-1] + nums[i])

same_idx = [0 for _ in range(M)]

for i in range(N):
    tmp = sums[i] % M
    if tmp == 0: ANS += 1
    same_idx[tmp] += 1

for cnt in same_idx:
    if cnt > 1:
        ANS += cnt * (cnt-1) // 2

print(ANS)


## 메모리: 153796 KB, 시간: 784 ms