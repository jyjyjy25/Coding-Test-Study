# BOJ_1300_배열에서 K번째 수 찾기
# 난이도: 골드 2
# 풀이 날짜: 23.10.15
# 풀이 시간: 약 50분

# How to


# Comment
"""
처음엔 A 배열을 생성하고, 배열에서 중앙 인덱스에 대한 값인 중앙값을 구하려고 A 배열을 extend해서 1차원으로 만든 B배열을 사용했다.
그런데 그냥 (start+end)//2를 계산하면 바로 중앙값이 나오다니.. 천잰가
"""

# Code
import sys

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())

start = 1
end = K
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for n in range(1, N+1):
        cnt += min(mid // n, N)

    if cnt < K:
        start = mid + 1
    elif cnt >= K:
        end = mid - 1

print(start)


## 메모리: 31120 KB, 시간: 1040 ms