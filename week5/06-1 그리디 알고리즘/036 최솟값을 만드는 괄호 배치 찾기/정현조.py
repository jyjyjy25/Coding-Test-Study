# BOJ_1541_잃어버린 괄호
# 난이도: 실버2
# 풀이 날짜: 23.10.22
# 풀이 시간: 40분

# How to
# 1. '-'를 기준으로 수식을 쪼갠다
# 2. '+'를 기준으로 수식을 다시 쪼개고 앞에 0이 붙어있다면 제거해주고 문자열로 된 수식/숫자를 int 형식의 연산 결과, 숫자로 만든다
# 3. 맨 처음 인덱스 값에서 나머지 인덱스 값의 합을 뺀다

# Comment
# 문제에 0이 붙을수도 있다는 조건이 왜 있나 하고 걍 넘겼다가 여기서 시간이 더 걸렸다
# eval()은 좋은 함수 같다 ㅎㅎㅎ

# Code
import sys
fomularArr = sys.stdin.readline().strip().split('-')
for i in range(len(fomularArr)):
    tmp = fomularArr[i].split('+')
    for j in range(len(tmp)):
        tmp[j] = tmp[j].lstrip('0')
    fomularArr[i] = eval('+'.join(tmp))

print(fomularArr[0] - sum(fomularArr[1:len(fomularArr)]))
## 메모리:  31120KB, 시간:  44ms