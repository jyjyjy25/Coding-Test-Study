# BOJ_1541_최솟값을 만드는 괄호 배치 찾기
# 난이도: 실버2
# 풀이 날짜: 23.10.15
# 풀이 시간: 약 25분

# How to
"""
최솟값을 만들기 위해서는 작은 수에서 큰 수를 빼야 한다.
즉 - 뒤에 (를, + 앞에 )를 넣으면 된다.

또한 0으로 시작하는 수를 앞의 0을 모두 제거하는 과정을 수행했다.
1. -를 기준으로 문자열을 분리하여 리스트 A에 저장한다.
2. 리스트 A의 각각의 요소를 +를 기준으로 문자열을 분리한다.
3. B 요소를 int로 변환하고 다시 str로 변환한다. 이 과정을 통해 앞의 0이 삭제된다.
4. 다시 문자열로 된 수식을 생성한다.
    4-1. B요소들을 '+'.join()으로 합쳐준다.
    4-2. 합친 수식 뒤에 '-'를 붙인다.
    4-3. 모두 합친 뒤 생성된 문자열의 마지막 요소 '-'를 제거한다.
"""

# Comment
"""
처음에 0으로 시작할 수 없다고 보고 구현했다가 .. 뒤늦게 수정하는데 애먹었다.
"""

# Code
import sys

expression = sys.stdin.readline().strip()

A = expression.split('-')

new_expression = ""
for a in A:
    B = list(map(str, map(int, a.split('+'))))
    new_expression += '+'.join(B)
    new_expression += '-'
new_expression = new_expression[:-1]

new_str = "("
for i, s in enumerate(new_expression):
    if s == '-':
        new_str += ")-("
    else:
        new_str += s

new_str += ')'

print(eval(new_str))


## 메모리: 31120 KB, 시간: 44 ms