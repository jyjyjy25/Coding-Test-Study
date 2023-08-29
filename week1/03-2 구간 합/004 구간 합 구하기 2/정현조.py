# BOJ_11660_구간 합 구하기 5
# 난이도: 실버1
# 풀이 날짜: 23.08.19
# 풀이 시간:

# How to
# 1. 길이가 n인 1차원 배열 생성
# 2. for문을 돌며 각 인덱스에 배열을 넣어 2차원 배열 생성
# 3. (x1, y1), (x2, y2)가 주어질 경우
# (x1~x2, y1~y2)인 요소들을 다 더하면 된다는 점을 이용해 이중 for문을 돌림

# Code
import sys #시간초과..
line1 = sys.stdin.readline().strip().split(' ')
n = int(line1[0])
m = int(line1[1])

arr = [0]*n
for i in range(n):
    ele = sys.stdin.readline().strip().split(' ')
    ele = list(map(int, ele))
    arr[i] = ele

for i in range(m):
    position = sys.stdin.readline().strip().split(' ')
    position = list(map(int, position))
    
    sum = 0
    for j in range(position[0]-1, position[2]): #x
        for k in range(position[1]-1, position[3]): #y
            sum += arr[j][k]
    print(sum)


## 메모리:  KB, 시간:  ms