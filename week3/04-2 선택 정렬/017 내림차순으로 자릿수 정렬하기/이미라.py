# BOJ_1427_소트인사이드
# 난이도: 실버 5
# 풀이 날짜: 23.09.23
# 풀이 시간: 12 분

# How to
"""
1. 수를 list 타입으로 입력받는다.
2. 내림차순으로 정렬한다.
3. 출력한다.
"""

# Comment
"""
"""

# Code

arr = list(map(int, str(input())))

arr.sort(reverse = True)
 
for i in arr:
    print(i, end='')


## 메모리: 31256 KB, 시간: 44 ms