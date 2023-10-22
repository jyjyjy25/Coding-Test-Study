# BOJ_1920_수 찾기
# 난이도: 실버4
# 풀이 날짜: 23.10.14
# 풀이 시간: 20분

# How to
'''
    배열 A를 정렬한다.
    이진 탐색을 수행하며 주어진 수가 배열에 존재하는지 확인한다.
        - (처음에는 전체범위) 주어진 범위의 중간 인덱스를 선정한다.
        - 중간에 위치하는 값과 찾고자 하는 수를 비교한다.
        - 찾고자 하는 수가 중간의 수보다 작은 경우에는 맨 앞부분부터 중간앞까지에 대해 다시 탐색을 시작한다.
          찾고자 하는 수가 중간의 수보다 큰 경우에는 중간뒤부터 맨 뒷부분까지에 대해 다시 탐색을 시작한다.
'''

# Comment
'''
    BFS, DFS보다는 훨씬 아이디어가 간단한게 이진탐색이기에 쉽게 풀 수 있었던 것 같다.
    사실 처음에 A 배열 정렬하는걸 까먹었어서 틀렸다.
'''

# Code
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
A.sort()

def binary_search(x, start, end):
    global A
    mid = int((end+start)/2)
    if start > end:
        return 0
    
    if A[mid] == x:
        return 1
    elif A[mid] > x:
        return binary_search(x, start, mid-1)
    else:
        return binary_search(x, mid+1, end)
    
for num in nums:
    print(binary_search(num, 0, N-1))
    

## 메모리: 47408 KB, 시간: 640 ms
'''
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
A.sort()

def binary_search(x, start, end):
    global A
    mid = int((end+start)/2)
    # print(f'A[{mid}] => {A[mid]} / {A}')
    if start > end:
        return 0
    
    if A[mid] == x:
        return 1
    elif A[mid] > x:
        # print(f'call {start} to {mid-1}')
        return binary_search(x, start, mid-1)
    else:
        # print(f'call {mid+1} to {end}')
        return binary_search(x, mid+1, end)
    
for num in nums:
    # print(num,'!')
    print(binary_search(num, 0, N-1))
    '''