# BOJ_11660_구간 합 구하기 2
# 난이도: 실버1
# 풀이 날짜: 23.08.23
# 풀이 시간: 42분

# How to
"""
1. 입력받은 데이터를 리스트에 저장하기
2. 합 배열 저장하기
3. 입력 구간에 대한 결과 계산 및 출력
- 런타임 에러가 너무 많이 났음
- 배열을 0부터 하는 방법도 있었음(교재 참고)
    array = []
    for i in range(n):
        row = [0] + [int(x) for x in input().split()]
        array.append(row)
"""

# Code

# 에러가 나지 않는 코드

import sys 
input = sys.stdin.readline

n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

hap_list = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        hap_list[i][j] = hap_list[i][j - 1] + hap_list[i - 1][j] - hap_list[i - 1][j - 1] + array[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int,input().split())

    result = hap_list[x2][y2] - hap_list[x2][y1 - 1] - hap_list[x1 - 1][y2] + hap_list[x1 - 1][y1 - 1]
    print(result)


## 메모리: 106008 KB,  시간: 1080 ms