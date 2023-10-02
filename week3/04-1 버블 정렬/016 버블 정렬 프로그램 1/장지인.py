# BOJ_1377_버블 소트
# 난이도: 골드2
# 풀이 날짜: 23.09.29
# 풀이 시간: 40분

# How to
'''
    1. 전체 수의 개수를 N으로 입력받는다. 이후 숫자와 인덱스를 같이 리스트에 넣어준다.
    2. sort()함수로 정렬해준다. 숫자가 인덱스보다 앞에 있으므로, 숫자를 기준으로 정렬된다.
    3. 현재 인덱스와 기존 인덱스의 차가 가장 큰 값을 구하고 1을 더해 반환한다.
'''

# Comment
'''
    처음에는 무슨 소리를 하는건지 모르겠어서 그냥 이전 문제 코드에 changed 변수를 추가해서 문제를 풀었다.
    근데 다시보니까 실제 버블정렬을 하지 않고도 확인할 수 있도록 하는 문제였다.
    최근 알고리즘 수업을 듣고있기에 버블정렬의 시간복잡도를 계산해보았다.
        N개의 데이터가 있다고 할 때, 총 N번 실행하고 N-n번 반복한다. 약 N^2의 시간복잡도를 가짐.
    책을 참고하였을 때 python의 sort()함수는 시간복잡도가 NlogN이라고 한다. 따라서 sort()를 쓴 다음의 방법론으로 하는게 좋다.
    
    책의 문제분석하기 부분을 참고하여 문제를 풀었다.

    다만, "swap이 일어나지 않는 반복문이 한번 더 실행 되는 것을 감안해 최댓값에 1을 더한다" 이 부분이 이해가지 않습니다.

    ++ 졸라이상한점.. 이전 문제에선 괜찮았으면서 이 문제에서는 sys 모듈 안쓰면 시간초과남.. 왜?
'''

# Code
import sys
input = sys.stdin.readline
N = int(input())
nums = []
for i in range(N):
    nums.append([int(input()), i])

sorted_nums = sorted(nums)

result = 0
for i in range(N):
    n = sorted_nums[i][1] - i
    if result < n:
        result = n

print(result+1)

## 메모리: 113844 KB, 시간: 1716 ms

'''
# 맨 처음에 간단하게 푼 버전(시간초과남)
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

changed = False
for i in range(N):
    changed = False
    for j in range(N-1-i):
        if nums[j] > nums[j+1]:
            changed = True
            nums[j], nums[j+1] = nums[j+1], nums[j]
    if changed == False:
        print(i + 1)
        break
'''        
# for num in nums:
#     print(num)

## 메모리:  KB, 시간:  ms