# BOJ_1167_트리의 지름
# 난이도: 골드2
# 풀이 날짜: 23.10.14
# 풀이 시간:

# How to
'''
    받은 수를 숫자와 연산자로 구분한다
    + 앞뒤로는 항상 더한다.
    마지막에 뺄 항목들만 남기고 빼준다.
'''

# Comment
'''
    솔직히 더 깔끔한 방법이 있을 것 같긴 한데,, 코드 상으로는 조금 더럽습니다.
'''

# Code
exp = input().strip()
element = []

tmp = ''
for i, e in enumerate(exp):
    if e == '+' or e == '-':
        element.append(int(tmp))
        tmp = ''
        element.append(e)
    else:
        tmp += e
element.append(int(tmp))

t = 0
n = []
for e in element:
    if e == '-':
        n.append(t)
        t = 0
    elif e == '+':
        continue
    else:
        t += e
n.append(t)

ANS = n.pop(0)
for a in n:
    ANS -= a

print(ANS)
    
 
## 메모리: 31120 KB, 시간: 44 ms