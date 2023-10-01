# BOJ_11399_ATM 인출 시간 계산하기
# 난이도: 실버3
# 풀이 날짜: 23.10.01
# 풀이 시간: 약 50분

# How to
"""
1. num_list[0]의 값을 sorted_list의 초기값으로 넣어둔다.
2. 인덱스 1부터 N까지 반복문을 통해 num_list를 순회한다.
    2-1. 인덱스(i)에 해당하는 값을 sorted_list에 append한다.
    2-2. sorted_list에 추가한 값(curr_num)을 삽입할 위치를 탐색하기 위해 추가한 값을 제외한 마지막 인덱스(i-1)부터 거꾸로 순회한다.
        2-2-1. 만약 sorted_list[j] > curr_num 이라면 sorted_list[j]와 sorted_list[j+1]을 swap한다.
        2-2-2. 만약 sorted_list[j] > curr_num 이 아니라면 적절한 위치에 curr_num을 삽입했으므로 해당 for 문을 break를 통해 빠져나온다.
3. 모든 사람이 돈을 인출하는 데 필요한 시간을 계산한다.
    3-1. temp_sum에는 각 사람이 돈을 인출하는 데 걸리는 시간(Pi)을 계산하여 저장한다.
    3-2. result에는 모든 사람이 돈을 인출하는 데 걸리는 시간을 계산하여 저장한다.

"""

# Comment
"""
처음에는 shift 과정때문에 삽입정렬이랑 선택정렬이 뭐가 다른지 약간 헷갈렸는데,
삽입정렬은 찾는 요소가 탐색 과정에서 가까이 있을 경우 더 효율적인 알고리즘인 것 같다. 이래서 책에서 이진탐색을 사용해면 더 효율적이라고 했구나.
또한 최종 정답을 계산할 때 합배열을 사용하는 게 더 가독성이 좋아보인다.
"""


# Code
import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

sorted_list = [num_list[0]]
for i in range(1, N):
    curr_num = num_list[i]
    sorted_list.append(curr_num)
    for j in range(i-1, -1, -1):
        if sorted_list[j] > curr_num:
            sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
        else:
            break

temp_sum = 0
result = 0
for i, n in enumerate(sorted_list):
    temp_sum += n
    result += temp_sum

"""
## 합 배열을 이용하여 모든 사람이 돈을 인출하는 데 걸리는 시간 계산
# S = [0] * N
# S[0] = sorted_list[0]
# result = S[0]
# for i in range(1, N):
#     S[i] = S[i-1] + sorted_list[i]
#     result += S[i]
"""

print(result)


## 메모리: 31256 KB, 시간: 104 ms