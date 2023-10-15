# BOJ_2343_기타 레슨
# 난이도: 실버 1
# 풀이 날짜: 23.10.15
# 풀이 시간: 16 분

# How to
"""
1. n, m, array를 입력받는다.
2. start는 array의 최댓값으로, end는 array의 총합으로 초기화 한다.
3. 이진 탐색을 시작한다.
    강의 순서대로 블루레이에 넣는다.
    블루레이의 개수가 m보다 크면 start를 증가시키고, m보다 작으면 end를 감소시킨다.
4. 결과를 출력한다.
"""

# Comment
"""
- 문제를 이해하긴 조금 어려웠지만 이진 탐색 풀이 적용해서 풀었다.
"""

# Code
n, m = map(int, input().split())
array = list(map(int, input().split()))

start, end = max(array), sum(array)

answer = 0

while start <= end:
    mid = (start + end) // 2

    count, sum = 0, 0

    for i in range(n):
        if sum + array[i] > mid:
            count += 1
            sum = 0
        sum += array[i]

    if sum:
        count += 1
        
    if count > m:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)

## 메모리: 42204 KB, 시간: 656 ms
