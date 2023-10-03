# BOJ_10989_수 정렬하기 3
# 난이도: 실버5
# 풀이 날짜: 23.10.02
# 풀이 시간:

# How to
# 기수 정렬 쳐보니까 계수 정렬이라는걸 알게 되서 활용해봄
# 숫자가 뭐가 나올지 모르니까 어떻게 하면 좋을까 하다가 젤 큰 수로 하면 될 것 같아서 arr의 크기를 num의 최대값으로 설정
# 배열 크기만큼 돌면서 해당 숫자 인덱스에 +1
# 출력할 땐 해당 인덱스를 그 개수만큼 돌면서 출력

# Comment
# 메모리 초과가 났는데 1.배열을 받아 둠 2.max 연산 이 둘 중에 원인이 있을 것으로 예상됨

# Code(메모리초과)
import sys
n = int(sys.stdin.readline().strip())
num = list(int(sys.stdin.readline().strip()) for _ in range(n))
maxNum = max(num)
arr = [0] * (maxNum+1)

for i in range(n):
    arr[num[i]] += 1
    i += 1
print(arr)

for i in range(n+1):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
## 메모리:  KB, 시간:  ms