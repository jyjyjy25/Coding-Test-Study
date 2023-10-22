# BOJ_1541_잃어버린 괄호
# 난이도: 실버2
# 풀이 날짜: 23.10.22
# 풀이 시간:

# How to


# Comment


# Code
import sys
fomularArr = sys.stdin.readline().strip().split('-')
for i in range(len(fomularArr)):
    tmp = fomularArr[i].split('+')
    for j in range(len(tmp)):
        tmp[j] = tmp[j].lstrip('0')
    fomularArr[i] = eval('+'.join(tmp))

print(fomularArr[0] - sum(fomularArr[1:len(fomularArr)]))
## 메모리:  KB, 시간:  ms