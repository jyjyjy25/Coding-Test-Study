# BOJ_1541_잃어버린 괄호
# 난이도: 실버 2
# 풀이 날짜: 23.10.15
# 풀이 시간: 17 분

# How to
"""
1. '-'를 기준으로 입력받는다.
2. '+'를 기준으로 나눈다.
3. '-'로 나눈 것 중, '+' 먼저 계산하여 num에 저장한다.
4. '-'로 나눈 것들을 계산하여 출력한다.
"""

# Comment
"""
- input().split('-'): '-'를 기준으로 split해서 array 리스트에 저장
- 하나하나 숫자와 기호를 저장해두었다가 계산해야 하나 생각했는데 교재 참고해서 더 효율적인 코드를 짤 수 있었다.
"""

# Code
array = input().split('-') 

num = []
for i in array:
    sum = 0
    tmp = i.split('+')

    for j in tmp:
        sum += int(j)
    num.append(sum)

n = num[0]

for i in range(1, len(num)):
    n -= num[i]
print(n)

## 메모리: 31120 KB, 시간: 44 ms
