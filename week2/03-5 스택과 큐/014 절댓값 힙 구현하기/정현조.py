# BOJ_11286_절댓값 힙
# 난이도: 실버1
# 풀이 날짜: 23.08.27
# 풀이 시간:

# How to
# 뭘로 풀어야할지 감도 안잡혀서 책에서 우선순위 큐라는 정보만 얻어서 풀었는데
# 메소드 찾아서 풀어보니까 풀이가 책이랑 거의 똑같네요..;

# Comment
# get()[idx]가 되는게 신기
# 근데 heap은 왜 queue에서 가져오고 queue는 왜 collections에서 가져오지
# put(우선순위, 넣을 값) 기억!!

# Code
import sys
from queue import PriorityQueue
n = int(sys.stdin.readline())

heap = PriorityQueue()
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap.empty():
            print(0)
        else:
            print(heap.get()[1])
    else:
        heap.put((abs(num), num))

## 메모리:  44036KB, 시간: 320ms