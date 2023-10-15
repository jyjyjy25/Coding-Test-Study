# BOJ_1300_K번째 수
# 난이도: 골드 2
# 풀이 날짜: 23.10.15
# 풀이 시간: 34 분

# How to
"""
1. n, k를 입력받는다.
2. start = 1, end = k로 초기화 해준다.
    이전에는 index로 탐색을 진행했기 때문에 start = 0이었으나, 이번에는 ` 수 `를 찾기 때문에 1로 초기화한다.
3. 이진 탐색을 시작한다. - 1차원 배열을 오름차순으로 나타냈을 때 k 번째 수를 찾아내야 한다.
    count를 초기화한다.
        mid보다 작거나 같은 숫자를 전부 찾으면 mid가 몇 번째 숫자인지 알 수 있다. 이때 n * 1이면 최댓값이 나오므로 n으로 제한을 준다.
    count가 k보다 작다면 start를 증가시키고, 크다면 end를 감소시킨다.
4. 결과를 출력한다.
"""

# Comment
"""
- 문제를 이해하기 어려웠다...
- 교재를 참고 했는데 ` 작은 수 카운트 ` 개념이 잘 이해되지 않았다...
    : 어떤 수보다 작은 자연수의 곱이 몇 개인지 알아내고자 할 때, a 보다 작은 수가 몇 개인지 찾아내면 a가 몇 번째 숫자인지 알아낼 수 있다.
"""

# Code
n = int(input())
k = int(input())

start, end = 1, k
answer = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in range(1, n + 1):
        count += min(int(mid // i), n)
    
    if count < k:
        start = mid + 1        
    else:
        answer = mid
        end = mid - 1

print(answer)

## 메모리: 31120 KB, 시간: 1316 ms
