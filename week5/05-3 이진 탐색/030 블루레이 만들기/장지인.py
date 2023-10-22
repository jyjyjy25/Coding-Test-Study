# BOJ_2343_기타 레슨
# 난이도: 실버1
# 풀이 날짜: 23.10.14
# 풀이 시간: 40분

# How to
'''
'''

# Comment
'''
    책의 문제 분석하기, 손으로 풀어보기를 참고하였습니다.
    가장 좀 신박했던 것은, 강의들에 대해서 이진탐색을 수행하는 것이 아니라, 블루레이 시간에 대해 수행한다는 것이였다.
    직접 써보면서 하니 이해가 되었다. 
    다만,, 책이 쉬운것도 어렵게 말하기 때문에.. 힘들었다.
'''

# Code
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

start = max(lectures)
end = sum(lectures)

def find(start, end):
    global lectures, M
    
    if start > end:
        return start
    
    mid = int((start + end)/2)

    s = 0
    n = 0
    for lect in lectures:
        if lect + s <= mid:
            s += lect
        else:
           n += 1
           s = lect

    if n >= M:
        return find(mid+1, end)
    else:
        return find(start, mid-1)
    
print(find(start, end))

## 메모리: 42204 KB, 시간: 220 ms