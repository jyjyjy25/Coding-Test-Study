# BOJ_12891_DNA 비밀번호
# 난이도: 실버5
# 풀이 날짜: 23.08.26
# 풀이 시간: 약 19분

# How to
"""
1. 딕셔너리를 이용하여 현재 부분 문자열에 대한 각각의 문자 개수를 나타낸다.
2. 초기 1회에 한하여 부분 문자열에 대한 각각의 문자(A, C, G, T) 개수를 딕셔너리에 업데이트한다.
3. "기존 검사 결과에 새로 들어온 문자열, 제거되는 문자열만 반영하여 확인" <- 핵심 아이디어를 중심으로 슬라이딩 윈도우 기법을 통해
    for 문을 돌면서 현재 부분 문자열에 대한 각각의 문자(A, C, G, T) 개수를 딕셔너리에 업데이트한다.
4. 각각의 문자에 대한 최소한의 개수를 만족하는지의 여부를 확인한다. 만족할 경우 cnt를 1 증가시킨다. 
    (by check_condition() 함수)
"""

# Comments
"""
교재 방식을 참고해서 내 방식대로 풀어봤다.
global을 애용하는 것도 코드 가독성 측면에서 괜찮은 방법인 것 같다.
"""

# Code
import sys


def check_condition(curr_str_dict):
    global cnt
    if curr_str_dict['A'] >= min_A and curr_str_dict['C'] >= min_C and curr_str_dict['G'] >= min_G and curr_str_dict['T'] >= min_T:
        cnt += 1


DNA_str_len, partial_str_len = map(int, sys.stdin.readline().split())
DNA_str = sys.stdin.readline()
min_A, min_C, min_G, min_T = map(int, sys.stdin.readline().split())

cnt = 0
curr_str_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}  # ACGT 문자열에 대한 개수를 0으로 초기화

# 초기 부분 문자열 할당 #
for i in range(partial_str_len):
    curr_str_dict[DNA_str[i]] += 1
check_condition(curr_str_dict)  # 초기의 부분 문자열에 대해 조건을 만족하는지 확인

for i in range(DNA_str_len - partial_str_len):  # 초기 할당한 횟수를 제외하고 (DNA_str_len - partial_str_len)번만큼 새로운 부분 문자열이 생성된다.
    start_p = i
    end_p = start_p + partial_str_len

    curr_str_dict[DNA_str[start_p]] -= 1  # curr_str_dict에서 start_p가 가리키는 값의 개수를 1 감소시킨다.
    curr_str_dict[DNA_str[end_p]] += 1  # curr_str_dict에서 end_p가 가리키는 값의 개수를 1 증가시킨다.
    check_condition(curr_str_dict)

print(cnt)


## 메모리: 32356 KB, 시간: 444 ms


"""
# 1번째 도전 #

# How to
1. 부분 문자열의 길이를 슬라이딩 윈도우의 범위로 지정한다.
2. 문자열을 순회하면서 부분 문자열을 초기화하고, 해당 부분 문자열이 A, C, G, T의 최소 개수를 만족하는지 확인한다.

# Comments
교재의 로직과는 다른 방식으로 접근하긴 했지만.. 결과는 시간 초과이다.
대체 어디서 시간 초과가 난 걸까..?
친절하게 코드 설명을 주석으로 달았으니 누가 분석해주면 정말 좋겠군..ㅜ
교재 방식(기존 검사 결과에 새로 들어온 문자열, 제거되는 문자열만 반영하여 확인)으로도 풀어봐야겠다.
아! 그리고 슬라이딩 윈도우는 2개의 포인터를 사용해야 하는데 이 점을 약간 간과하고 인덱스 슬라이싱으로만 접근하긴 했다..

# Code
import sys

DNA_str_len, partial_str_len = map(int, sys.stdin.readline().split())
DNA_str = sys.stdin.readline()
min_A, min_C, min_G, min_T = map(int, sys.stdin.readline().split())

cnt = 0
for i in range(DNA_str_len - partial_str_len + 1):  # 생성되는 부분 문자열의 수는 (DNA_str_len - partial_str_len + 1)개이다.
    ACGT_len = {'A': 0, 'C': 0, 'G': 0, 'T': 0}  # 부분 문자열에 존재하는 ACGT 각각의 문자열의 개수를 0으로 초기화한다.
    partial_str = DNA_str[i:i + partial_str_len]
    for s in partial_str:
        ACGT_len[s] += 1  # 특정 문자의 개수를 1 증가시킨다.
        if (ACGT_len['A'] >= min_A and ACGT_len['C'] >= min_C and ACGT_len['G'] >= min_G and ACGT_len['T'] >= min_T):  # 조건에 맞을 경우 cnt를 1 증가시키고 for문을 빠져나온다.
            cnt += 1
            break

print(cnt)

## 메모리:  KB, 시간:  ms
## -> 시간초과
"""