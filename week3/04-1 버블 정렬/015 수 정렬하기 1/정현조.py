# BOJ_2750_수 정렬하기
# 난이도: 브론즈1
# 풀이 날짜: 23.08.29
# 풀이 시간: 17:10

# How to
# for문의 범위를 루프의 범위로 설정
# while문을 돌면서 조건에 부합할 때 swap 진행

# Comment
# 첨에 자꾸 while문 1번만 돌길래 띠용했는데 
# j를 for문 밖에서 초기화 했기 때문에 발생한 일이었다.
# 작은 것도 잘 살펴봐야 한다..는 교훈을 얻음

# Code
import sys
n = int(sys.stdin.readline())
numList = [int(sys.stdin.readline()) for i in range(n)]

tmp = 0
for i in range(n, 0, -1): #범위를 range로 설정
    j = 0
    while j+1 < i:
        if numList[j] > numList[j+1]:
            tmp = numList[j]
            numList[j] = numList[j+1]
            numList[j+1] = tmp
        j += 1

result = "\n".join(map(str, numList))
print(result)

## 메모리:  31256KB, 시간:  236ms