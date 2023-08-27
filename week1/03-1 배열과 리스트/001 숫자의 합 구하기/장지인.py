# BOJ_11720_숫자의 합
# 난이도: 브론즈4
# 풀이 날짜: 23.08.14
# 풀이 시간: 4분대

# How to
'''
전체 숫자의 개수를 N으로 받는다. (단 파이썬 특성상 사용하지 않아도 괜찮았음)
한줄에 숫자의 나열을 numbers로 받는다.
string 타입은 이터러블이므로 for ... in ... 반복문을 사용해 문자열의 원소 하나씩 순회하게 하였다.
순회하면서 정답을 저장하는 ANS 변수에 int형으로 변환하여 더해주었다.

다 풀고 책을 보니 list(input())으로 입력받을 경우, list(str)과 같이 적용됨을 보았다. 기억할것
'''
# Code
N = int(input())
numbers = input()

ANS = 0
for num in numbers:
    ANS += int(num)

print(ANS)

## 메모리: 31256 KB, 시간: 44 ms