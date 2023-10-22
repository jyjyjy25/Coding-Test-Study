# BOJ_1931_회의실 배정
# 난이도: 실버 1
# 풀이 날짜: 23.10.15
# 풀이 시간: 24 분

# How to
"""
1. n을 입력받는다.
2. 회의시간을 초기화 한다(종료시간, 시작시간).
3. array를 오름차순으로 정렬한다.
4. 가장 빨리 끝나는 회의를 시작으로 겹치지 않는 회의가 나온 경우 count를 증가시킨다.
5. 결과를 출력한다.
"""

# Comment
"""
- 처음 문제를 봤을 때, 어떻게 풀어야 하나 막막했는데, 아래 개념을 알고나니 쉽게 풀 수 있었다.
    종료시간을 기준으로 오름차순으로 정렬하기 위해 2차원 배열의 설정을 다음과 같이 하였다.
        array[i][0] = b
        array[i][1] = a
- ` 회의가 빨리 끝나는 순서대로 정렬해야 한다. `
"""

# Code
n = int(input())
array = [[0] * 2 for _ in range(n)]

for i in range(n):
    a, b = map(int, input().split())

    array[i][0] = b
    array[i][1] = a

array.sort()

count = 0
end_time = array[0][1]

for i in range(n):
    if array[i][1] >= end_time:
        count += 1
        end_time = array[i][0]

print(count)

## 메모리: 39576 KB, 시간: 160 ms
