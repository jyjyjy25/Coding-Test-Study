# BOJ_1427_내림차순으로 자릿수 정렬하기
# 난이도: 실버5
# 풀이 날짜: 23.10.01
# 풀이 시간: 약 15분

# How to
"""
1. 문자열을 입력받고 for 문을 통해 각각의 문자에 접근하여 int로 형변환을 한 뒤 리스트에 저장한다.
2. 현재 남은 정렬 리스트에서 max()를 이용하여 최댓값을 max_value에 저장하고, 최댓값에 대한 인덱스를 max_idx에 저장한다.
3. 현재값과 최댓값을 swap한다. 이때 문자열로 출력하기 위해 최댓값을 str로 형변환하여 저장한다.
4. join()을 이용하여 리스트를 하나의 문자열로 합쳐 출력한다.
"""

# Comment
"""
이 문제는 선택 정렬 알고리즘 구현보다 입출력을 어떻게 할 것인가에 더 고민이 많았다.
우선 입력의 경우 정렬을 하려면 int로 형변환해야 한다고 생각했다.
    '2143'과 같이 입력이 들어오게 되면 문자열로 입력을 받고 각각의 문자에 접근해서 하나씩 형변환하는 방법밖에 없다고 생각했지만,
    책을 참고하니 문자로 입력을 받아도 정렬이 수행됨을 알 수 있었다. 자릿수 하나하나를 정렬하는 거라 가능한 것 같다.
또한 출력의 경우 '4321'과 같이 출력해야 하는데, end=''를 이용하거나 *num_list를 이용하여 출력했을 때 이상하게도 '%' 문자가 마지막에 같이 출력되었다.
이를 없애려 최후의 방법으로 join을 사용하기 위해 결국 swap할 때 최댓값을 str로 형변환해주게 되었다.
"""


# Code
import sys
nums = sys.stdin.readline().strip()

num_list = []
for n in nums:
    num_list.append(int(n))

for i, n in enumerate(num_list):
    max_value = max(num_list[i:])
    max_idx = num_list.index(max_value)
    num_list[max_idx], num_list[i] = n, str(max_value)

print(''.join(num_list))


## 메모리: 31256 KB, 시간: 40 ms