# BOJ_1715_카드 정렬하기
# 난이도: 골드4
# 풀이 날짜: 23.10.14
# 풀이 시간: 20분

# How to


# Comment
'''
    합치고 있는 카드 뭉치를 포함해 모든 카드 뭉치들에 대해,
    가장 작은 두 뭉치를 합쳐나가는 것이 가장 적은 시간이 든다.
    따라서 우선순위큐로 매번 작은 카드뭉치를 get할 수 있게 하였다
    현재 섞고 있는 카드가 get한 카드보다 크다면, 합치는데 더 적은 시간이 걸리는 뭉치들이 있을 수 있으므로
    큐에 다시 넣은다음 그다음으로 작은 뭉치를 새로 뽑아서 합친다.
    매 순간의 결과는 ANS라는 변수에 합쳐서, 총 카드를 정렬한 횟수를 기록한다.
'''

# Code
import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
queue = PriorityQueue()
for _ in range(N):
    queue.put(int(input()))

ANS = 0
tmp = queue.get()
while not queue.empty():
    m = queue.get()
    if tmp > m:
        queue.put(tmp)
        tmp = m + queue.get()
    else:
        tmp += m
    ANS += tmp

print(ANS)

## 메모리: 37576 KB, 시간: 584 ms