# BOJ_1377_버블 소트
# 난이도: 골드 2
# 풀이 날짜: 23.09.23
# 풀이 시간: 45 분

# How to
"""
1. 처음 숫자를 입력받을 때 숫자와 입력받은 순서대로 리스트에 저장한다.
2. sorted() 함수를 사용하여 입력받은 숫자를 정렬한다.
3. 처음 입력받은 숫자의 순서와 sorted() 후의 순서의 차를 구해 각 수의 정렬에 필요한 횟수를 센다.
4. 횟수 중 가장 큰 수를 출력한다.
"""

# Comment
"""
- 버블정렬 과정을 하나하나 세는게 아니라 정렬 전, 후 만으로 필요한 정렬 횟수를 계산한다는 개념이 생소했다.
"""

# Code

import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    arr.append((int(input()), i))

sorted_arr = sorted(arr) 
answer = [] 

for i in range(N):
    answer.append(sorted_arr[i][1] - arr[i][1])

print(max(answer) + 1)


## 메모리: 124816 KB, 시간: 1164 ms