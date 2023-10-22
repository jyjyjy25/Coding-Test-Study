# BOJ_1931_회의실 배정
# 난이도: 실버1
# 풀이 날짜: 23.10.22
# 풀이 시간:

# How to
# 1. 두선순위 큐를 이용해 끝나는 시간과 회의 시간을 기준으로 회의를 정렬한다.
#    ㄴ 만약 회의 시간이 0이면 시간을 최대로 해서 넣는다
# 2. 비교 기준을 하나 꺼낸다
# 3. 새로 꺼낸 회의의 시작 시간이 비교군의 끝나는 시간보다 작으면 넘어가고 그렇지 않으면 count를 1 올리고 비교군을 꺼낸 값으로 바꾼다
# 4. 3을 큐가 빌 때까지 반복한다

# Comment
# 85%에서 에러나길래 반례를 보니까
# 회의시간이 0이면 끝나는 시간이 같은 다른 회의에 대해 우선순위가 가장 높아져
# 원래는 들어올 수 있는 회의들을 무시해버리는 문제가 있었다.
# 그걸 어떻게 처리할까..하다가 마땅한 방법이 생각이 안 나서 그냥 시간을 최대로 해 순위를 최하위로 낮춰버렸다

# Code
from queue import PriorityQueue
import sys
n = int(sys.stdin.readline())
meetings = PriorityQueue(maxsize=n)

for _ in range(n):
    s, e = map(int, sys.stdin.readline().strip().split(' '))
    time = e-s
    if time == 0:
        meetings.put((e, 2^31, s))
    else:
        meetings.put((e, time, s))

count = 1
comparison = meetings.get()
while not meetings.empty():
    tmp = meetings.get()
    if tmp[2] < comparison[0]:
        continue
    else:
        count += 1
        comparison = tmp

print(count) #85%
    

## 메모리:  52988KB, 시간:  600ms