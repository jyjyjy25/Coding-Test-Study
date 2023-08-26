# BOJ_2018_연속된 자연수의 합 구하기
# 난이도: 실버 5
# 풀이 날짜: 23.08.20
# 풀이 시간: 약 25분

# How to
'''
1. 0부터 N까지의 요소를 갖는 리스트를 생성한다.
2. 자기 자신(N)은 무조건 경우에 수에 포함되므로 cnt를 1로 초기화한다.
3. end_pointer를 round(N/2), start_pointer를 end_pointer-1로 설정한다. N/2보다 큰 수들을 더할 경우 절대로 N이 될 수 없기 때문이다.
4. pointer를 sum 값에 따라 변경하면서 합을 계산한다.
    4-1. sum > N일 경우 end_pointer를 1 감소시킨다.
    4-2. sum < N일 경우 start_pointer를 1 감소시킨다.
    4-3. sum == N일 경우 start_pointer와 end_pointer를 1 감소시킨다.
'''

# Code
import sys

N = int(sys.stdin.readline())
num_list = list(range(0, N+1))

cnt = 1
end_pointer = round(N/2)
start_pointer = end_pointer - 1

sum = num_list[start_pointer] + num_list[end_pointer]
while (end_pointer != 0):    
    if sum == N:
        cnt += 1
        sum -= num_list[end_pointer]
        end_pointer -= 1
        start_pointer -= 1
        sum += num_list[start_pointer]
    elif sum > N:
        sum -= num_list[end_pointer]
        end_pointer -= 1
    elif sum < N:
        start_pointer -= 1
        sum += num_list[start_pointer]

print(cnt)

## 메모리:  KB, 시간:  ms
## 메모리 초과
