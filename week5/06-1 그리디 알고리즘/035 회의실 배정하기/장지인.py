# BOJ_1931_회의실 배정
# 난이도: 실버1
# 풀이 날짜: 23.10.15
# 풀이 시간: 30분

# How to
'''
    회의 종료 시간을 기준으로 정렬하여 조건에 맞는 회의의 개수를 센다.
'''

# Comment
'''
    s >= end인데 s > end로 해서 한번 틀렸음.. 식겁했네
    다 풀고 보니 드는 생각이. 우선순위큐까지 쓰지 않아도 괜찮은 문제인 것 같다.
'''

# Code
import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
queue = PriorityQueue()
for _ in range(N):
    a, b = map(int, input().split())
    queue.put([b, a]) # 회의 끝나는 시간, 회의 시작하는 시간

end, start = queue.get()
ANS = 1
while not queue.empty():
    e, s = queue.get()
    if s >= end:
        end = e
        ANS += 1

print(ANS)
    

## 메모리: 51020 KB, 시간: 664 ms