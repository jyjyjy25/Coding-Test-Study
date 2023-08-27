# BOJ_12891_DNS 비밀번호
# 난이도: 실버 5
# 풀이 날짜: 23.08.26
# 풀이 시간: 80분

# How to
"""
- add(): 새로 들어온 문자를 센다
- remove(): 문자를 제거하고 checkSecret --
1. 데이터를 입력 받아서 값이 0인 데이터의 개수만큼 checkSecret를 증가시킨다.
2. 유효한 비밀 번호인지 판단한다.
    - checkSecret == 4
"""

# Comment
"""
- 방향을 아예 못 잡아서 교재 참고하면서 해결
"""

# Code

checklist = [0] * 4
myarray = [0] * 4
checkSecret = 0 # 몇 개의 문자와 관련된 개수를 충족하는지 확인

def add(c):
    global checklist, myarray, checkSecret

    if c == 'A':
        myarray[0] += 1
        if myarray[0] == checklist[0]:
            checkSecret += 1
    
    elif c == 'C':
        myarray[1] += 1
        if myarray[1] == checklist[1]:
            checkSecret += 1
    
    elif c == 'G':
        myarray[2] += 1
        if myarray[2] == checklist[2]:
            checkSecret += 1

    elif c == 'T':
        myarray[3] += 1
        if myarray[3] == checklist[3]:
            checkSecret += 1

def remove(c):
    global checklist, myarray, checkSecret

    if c == 'A':
        if myarray[0] == checklist[0]:
            checkSecret -= 1
        myarray[0] -= 1
    
    elif c == 'C':
        if myarray[1] == checklist[1]:
            checkSecret -= 1
        myarray[1] -= 1
    
    elif c == 'G':
        if myarray[2] == checklist[2]:
            checkSecret -= 1
        myarray[2] -= 1

    elif c == 'T':
        if myarray[3] == checklist[3]:
            checkSecret -= 1
        myarray[3] -= 1


S, P = map(int, input().split())
result = 0

array = list(input())
checklist = list(map(int, input().split()))

for i in range(4):
    if checklist[i] == 0:
        checkSecret += 1

for i in range(P):
    add(array[i])

if checkSecret == 4:
    result += 1

for i in range(P, S):
    j = i - P

    add(array[i])
    remove(array[j])

    if checkSecret == 4:
        result += 1

print(result)

## 메모리: 39940 KB, 시간: 476 ms