# BOJ_12891_DNS 비밀번호
# 난이도: 실버2
# 풀이 날짜: 23.08.22
# 풀이 시간: 40분

# How to
'''
- S: 문자열의 개수
- T: 비밀번호의 길이
- dna_str: 주어진 DNA 문자열
- rule: 문자열을 key값으로, 필요한 개수가 value가 되도록 저장한 딕셔너리

1. 시작 인덱스 i와 끝 인덱스 j가 T 길이의 윈도우 사이즈를 만족하도록 설정해준다. (i=0, j=P-1)
2. 초기 i,j에 대하여 A, C, G, T의 개수를 세어 딕셔너리인 checklist를 만들었다.
3. rule과 checklist를 비교하여 조건에 맞으면 ANS 값을 1씩 더해준다.
4. 윈도우를 한칸 옆으로 옮기기 위하여 문자열의 i 인덱스의 개수는 하나 빼주고, j 인덱스의 다음 문자의 개수는 하나 더해준다.
5. j 다음 문자가 없을 때까지 3,4번을 반복한다.
'''

# Comment
'''
맨 처음엔 string.count()함수를 사용하였다. 이때는 시간초과가 날 것 같았지만, 간단해서 그냥 해봤었다. (결국 시간초과)
그다음으로는 매번 i부터 j까지의 문자열에 대해 알파벳의 개수를 각각 구했었다. 그래서 시간초가가 났다.

그렇게 풀다가 생각해보니.. 왜 매번 그걸 계산하고있었지?! 를 발견해버렸다.
그래서 윈도우를 옮기면서 다음에 없어질 인덱스와 추가될 인덱스에 대해서만 checklist에 반영하게끔 수정하였다!

다 푼 이후에 교재를 봤는데, 저렇게 리스트들과 긴 코드들을 사용한 것보다 내 코드가 훨 좋은거 같다 ㅎㅎ
'''

# Code
import sys
input = sys.stdin.readline

S, P = map(int, input().split())
dna_str = input()
a, c, g, t = map(int, input().split())
rule = {'A': a, 'C':c, 'G':g, 'T':t}

i = 0
j = P - 1

ANS = 0

checklist = {'A': 0, 'C':0, 'G':0, 'T':0}  
for s in dna_str[i:j+1]:
    checklist[s] += 1

while (j < S):
    tmp = True
    for alpha in rule.keys():
        if rule[alpha] > checklist[alpha]:
            tmp = False
            break
    
    if tmp: ANS += 1

    if j+1 == S:
        break
    else:
        checklist[dna_str[i]] -= 1
        checklist[dna_str[j+1]] += 1
        i += 1; j += 1
    
print(ANS)


## 메모리: 32988 KB, 시간: 720 ms