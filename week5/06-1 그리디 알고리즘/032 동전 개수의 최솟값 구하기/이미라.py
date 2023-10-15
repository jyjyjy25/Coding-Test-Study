# BOJ_11047_동전 0
# 난이도: 실버 3
# 풀이 날짜: 23.10.15
# 풀이 시간: 16 분

# How to
"""
1. n, k, array를 입력받는다.
2. 그리디 탐색을 실행한다.
    배열 array를 거꾸로 반복한다.
    현재 동전의 가치가 k보다 작거나 같으면,
        count에 k를 동전으로 나눈 몫을 더한다.  
        k는 동전으로 나눈 나머지로 다시 반복한다.
3. 결과를 출력한다.
"""

# Comment
"""
- 교재를 참고했다.
    교재 코드대로 하면 런타임에러가 발생해서 append로 수정했음
- 주의해야 하는 것: 그리디 탐색은 속도가 빠르지만 항상 정확한 답을 제공하진 않기 때문에 적용 가능 여부를 항상 확인해야 한다.
"""

# Code
n, k = map(int, input().split())
array = []

for i in range(n):
    array.append(int(input()))

count = 0

for i in reversed(range(n)):
    if array[i] <= k:
        count += int(k / array[i])
        k = k % array[i]

print(count)

## 메모리: 31120 KB, 시간: 44 ms
