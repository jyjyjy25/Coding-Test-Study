# BOJ_1920_수 찾기
# 난이도: 실버 4
# 풀이 날짜: 23.10.15
# 풀이 시간: 21 분

# How to
"""
1. n, array, m, target_array를 입력받는다.
2. target을 확인한 경우를 알려줄 변수 find를 정의한다. (찾으면 1, 못 찾으면 0을 출력해야 하기 때문)
3. 이진 탐색을 수행한다.
    중간값(mid)을 정의한다.
    중간값이 target(i)보다 크면 start를 증가시키고, 작으면 end를 감소시킨다.
    mid와 i가 같으면 원하는 수를 찾았음을 의미한다.
4. 결과를 출력한다.
"""

# Comment
"""

"""

# Code
n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
target_array = list(map(int, input().split()))

for i in target_array:   
    find = False

    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] < i:
            start = mid + 1
        elif array[mid] > i:
            end = mid - 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)


## 메모리: 46720 KB, 시간: 632 ms
