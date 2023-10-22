# BOJ_2343_문제명_기타 레슨
# 난이도: 실버1
# 풀이 날짜: 23.10.13
# 풀이 시간: 1시 3분

# How to
# 1. 값을 받는다
# 2. 강의 시간 배열 안을 돌면서 최대 시간을 s, 총합을 e로 지정한다
# 3. 시간의 합을 통해 필요한 블루레이 개수를 세고 블루레이 개수를 이용해 범위를 좁혀간다
# 4. 

# Comment
# 주어진 강의 시간 내에서 해결하려고만 해서 아이디어가 전혀 떠오르지 않았다..
# 책을 보고서도 블루레이 최소 크기는 9이고 최대 크기는 45라는걸 이해하는데도 쫌 걸림
# 손으로 풀어보기 보고 풀었는데 안 돼서 뭐가 문젠가 보니까 맨 마지막 else를 elif blurayCount < m 으로 해두는 바람에 둘이 같은 경우를 처리하지 않아서 무한대기에 빠졌던 거였음
# 개인적으로 인덱스를 값처럼 쓰는 것과 for in range()가 아닌 for in문은 항상 어렵고 헷갈림림
# 근데 왜 항상 답은 s인걸까?

# Code
# n: 강의 개수 m: 블루레이 개수
import sys
n, m = map(int, sys.stdin.readline().strip().split(' '))
minute = list(map(int, sys.stdin.readline().strip().split(' ')))
s, e = 0, 0

for i in minute:
    if s < i:
        s = i
    e += i

while s <= e:
    mid = (s+e)//2
    minuteSum = 0
    blurayCount = 0
    for i in range(n):
        if minuteSum + minute[i] > mid:
            minuteSum = 0
            blurayCount += 1
        minuteSum += minute[i]

    if minuteSum != 0:
        blurayCount += 1
    
    if blurayCount > m:
        s = mid + 1
    else:
        e = mid - 1

print(s)


## 메모리:  42204KB, 시간:  704ms