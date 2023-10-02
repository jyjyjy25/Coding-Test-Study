# BOJ_1427_소트인사이드
# 난이도: 실버5
# 풀이 날짜: 23.09.29
# 풀이 시간: 20분

# How to
'''
    1. 숫자를 리스트에 저장한다.
    2. 선택 정렬 알고리즘대로 정렬한다
        (1) 비교 대상을 맨 앞 인덱스부터 잡는다.
        (2) 비교 대상 이후의 인덱스들을 순회하며 가장 큰 값을 찾는다.
        (3) 비교 대상보다 큰 인덱스를 발견하면 스왑한다.
        (4) 비교할 인덱스를 뒤로 옮겨가며 (1)~(3)의 과정을 반복한다.
    3. 정렬된 리스트의 값을 출력한다.
'''

# Comment
'''
    선택정렬은 조금 헤맸지만 문제 없이 작성하였다.
    다만 마지막에 한단어로 출력하는데에 있어서 다음과 같은 문제가 발생했다.
    `print(n, end='')`와 같이 작성하였을때, 알수없는 퍼센트 기호가 같이 출력되었다.
    방법을 찾다가 모르겠어서 join 함수를 사용하였다.
    다만 join함수는 리스트의 값이 str일때만 사용가능하여 map 함수도 같이 사용했다.
'''

# Code
N = input()

nums = []
for num in N:
    nums.append(int(num))

N = len(N)
for i in range(N):
    max_id = i
    for j in range(i+1,N):
        if nums[max_id] < nums[j]:
            max_id = j
    
    if i != max_id:
        nums[i], nums[max_id] = nums[max_id], nums[i]

print(''.join(map(str,nums)))
        

## 메모리: 31256 KB, 시간: 40 ms