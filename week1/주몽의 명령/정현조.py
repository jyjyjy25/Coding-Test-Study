# BOJ_1940_주몽
# 난이도: 실버4
# 풀이 날짜: 23.08.19
# 풀이 시간:

# How to
# 1. 받아온 수 집합을 배열로 만든다
# 2. 배열의 첫 숫자([0])부터 m에서 빼 target 생성
# 3. count를 이용해 target에 해당하는 숫자가 배열에 없으면 [0]을 pop
# 4. 있으면 두 수 모두 배열에서 pop하고 동시에 count +1

# Code #틀렸는데 왜 틀렸는지 모르겠음
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
idx = sys.stdin.readline().strip().split(' ')
idx = list(map(int, idx))

count = 0
while idx:
    target = m - idx[0]
    if(idx.count(target)==0):
        idx.pop(0)
    else:
        targetIdx = idx.index(target)
        idx.pop(targetIdx)
        idx.pop(0)
        count += 1
print(count)

## 메모리:  KB, 시간:  ms