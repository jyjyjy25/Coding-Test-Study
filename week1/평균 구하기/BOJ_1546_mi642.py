# BOJ_1546_평균
# 난이도: 브론즈1
# 풀이 날짜: 23.08.15
# 풀이 시간:

# How to


# Code

n = int(input())
score = list(map(int, input().split()))

higher_score = max(score)

average = 0
for i in score:
    average += (i / higher_score * 100)

print(average / len(score))

## 메모리:  KB, 시간:  ms