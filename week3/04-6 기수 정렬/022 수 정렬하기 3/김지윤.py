# BOJ_10989_수 정렬하기 3
# 난이도: 실버5
# 풀이 날짜: 23.10.01
# 풀이 시간: 약 7분

# How to
"""
1. 계수정렬 알고리즘을 이용하여 입력받은 수를 정렬한다.
    1-1. 입력받는 수 범위만큼 0으로 초기화한 배열을 생성한다.
    1-2. 입력받은 수를 인덱스로 갖는 배열의 요소의 값을 1씩 증가시킨다.
    1-3. 배열의 값이 0이 아닌 요소들을 값만큼 인덱스를 출력한다.
"""

# Comment
"""
시도 2,3에서 자꾸 메모리 초과가 발생하길래 교재 코드를 통해 어느 부분이 메모리 초과를 발생시켰는지 비교해보면서 원인을 찾아냈는데, 원인은 list comprehension이었다..
찾아보니 list comprehension은 메모리의 낭비가 가장 큰 문제점으로 꼽히고 있었다.
새 리스트를 통재로 생성하기 때문에 리스트 사이즈가 커질수록 메모리 사용량이 증가한다.
따라서 generator 사용을 권장한다. generator는 사이즈가 커져도 차지하는 메모리 사이즈는 동일하다고 한다.
나중에 제대로 공부해서 정리해놔야겠다..
"""

# Code
import sys

N = int(sys.stdin.readline())
count = [0] * 10001

for _ in range(N):
    count[int(sys.stdin.readline())] += 1

for i, c in enumerate(count):
    for _ in range(c):
        print(i)


"""
[시도 3]
계수 정렬을 이용한 코드 - 메모리 초과
-> 왜 또 메모리 초과????

import sys

N = int(sys.stdin.readline())

count = [0] * 10001
for _ in range(N):
    count[int(sys.stdin.readline())] += 1

for i, c in enumerate(count):
    [print(i) for _ in range(c)]
"""


"""
[시도 2]
계수 정렬을 이용한 코드 - 메모리 초과
-> 입력받으면서 count 배열에 한 번에 저장해야하나?

import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

count = [0] * 10001
for n in nums:
    count[n] += 1

for i, c in enumerate(count):
    [print(i) for _ in range(c)]
"""


"""
[시도 1]
기수정렬을 이용한 코드 - 메모리 초과
참고: [https://10000cow.tistory.com/entry/%EC%A0%95%EB%A0%AC-7-%EA%B8%B0%EC%88%98-%EC%A0%95%EB%A0%ACradix-sort]
-> 열심히 배워왔건만..

import sys
from collections import deque

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
buckets = [deque() for _ in range(10)]

max_value = max(nums)
queue = deque(nums)
digit = 1

while max_value >= digit:
    while queue:
        num = queue.popleft()
        buckets[(num // digit) % 10].append(num)
    
    for bucket in buckets:
        while bucket:
            queue.append(bucket.popleft())
    digit *= 10

for n in list(queue):
    print(n)
"""


## 메모리: 31256 KB, 시간: 8904 ms