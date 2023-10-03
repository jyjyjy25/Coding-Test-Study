# BOJ_12891_DNA 비밀번호
# 난이도: 실버5
# 풀이 날짜: 23.08.26
# 풀이 시간: 1:39:18

# How to
# 1st 시도
# arr[fPointer:bPointer]와 .count()를 이용하여 각 알파벳 개수를 셈 -> 시간초과
# gpt한테 물어보니까 문자열 슬라이싱에서 시간이 오래 걸린다네요?
# 그래서 교재 참고해서 품
# 튜플로 저장 및 비교하고 해서 해당하는 경우를 카운트 함

# Code
import sys
p, s = list(map(int, sys.stdin.readline().strip().split(' ')))
dnaArr = list(sys.stdin.readline().strip())
a, c, g, t = map(int, sys.stdin.readline().strip().split(' '))

count_list = {'A':0, 'C':0, 'G':0, 'T':0}
for i in range(s):
    count_list[dnaArr[i]] += 1

fPointer = 0
bPointer = s-1

count = 0
while bPointer != p:
    if(
        count_list['A'] >= a and 
        count_list['C'] >= c and 
        count_list['G'] >= g and 
        count_list['T'] >= t 
    ):
        count += 1
    
    count_list[dnaArr[fPointer]] -= 1
    fPointer += 1
    bPointer += 1
    if bPointer < p:
        count_list[dnaArr[bPointer]] +=1
print(count)


## 메모리:  39940KB, 시간:  464ms