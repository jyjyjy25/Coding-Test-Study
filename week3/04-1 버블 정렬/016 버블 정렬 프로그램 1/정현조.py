# BOJ_1377_버블소트
# 난이도: 골드2
# 풀이 날짜: 23.08.29
# 풀이 시간: 1:05:37

# How to
# 1st try는 문제 있는 코드를 파이썬으로만 짰다. N이 너무 커서 당연히 시간초과
# 2nd는 중첩 for문을 전부 돌지 않는 방법을 찾아보려고 했는데
# 중첩 for문을 한번에 탈출할 방법이 없어서 실패
# 결국 책에서 제시한 아이디어를 참고해서 코드를 짬


# Comment
# 정렬 알고리즘을 응용하는게 아니라 뭔가 핀트가 다르다고 느껴짐..

# Code
import sys
n = int(sys.stdin.readline())
numList = sorted([(int(sys.stdin.readline()), i) for i in range(n)])

max = numList[0][1] - 0
for i in range(n-1):
    tmp = numList[i+1][1] - (i+1)
    if max < tmp:
        max = tmp
print(max+1)

'''
[1st try]
import sys
n = int(sys.stdin.readline())
numList = [int(sys.stdin.readline()) for i in range(n)]

changed = False
for i in range(n):
    changed = False
    for j in range(n-1):
        if numList[j] > numList[j+1]:
            changed = True
            numList[j], numList[j+1] = numList[j+1], numList[j]
    if changed == False:
        print(i+1)
        break
'''
'''
[2nd try]
import sys
n = int(sys.stdin.readline())
numList = [int(sys.stdin.readline()) for i in range(n)]

for i in range(n):
    for j in range(n-1):
        if j == n-2 and numList[j] <= numList[j+1]:
            #여기서 한번에 모든 for문을 탈출할 방법이 없음
        if numList[j] > numList[j+1]:
            numList[j], numList[j+1] = numList[j+1], numList[j]
'''
        

## 메모리:  105652KB, 시간:  992ms