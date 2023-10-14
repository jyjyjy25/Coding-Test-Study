# BOJ_2343_블루레이 만들기
# 난이도: 실버1
# 풀이 날짜: 23.10.15
# 풀이 시간: 약 60분

# How to
"""
이진 탐색은 무엇을 탐색할지 생각하는 것이 중요한 것 같다. 그래서 해당 문제를 기반으로 정리해보자면,
무엇을 탐색해야 하는가? "블루레이의 크기"를 탐색해야 한다.

이를 기반으로 start, end를 어떻게 초기화해야 하는지 생각한다.
해당 문제에서는 블루레이 크기의 최솟값과 최댓값을 start와 end로 초기화하면 된다.
start는 레슨의 최댓값이며, 이는 블루레이의 최대 개수를 의미한다.
end는 모든 레슨의 합이며, 이는 블루레이의 최소 개수를 의미한다.

또한 블루레이의 개수가 M보다 크다면 블루레이의 크기를 늘려야 하며, 블루레이의 개수가 M보다 작거나 같다면 블루레이의 크기를 줄여야 한다.
이 연관관계를 잘 고려해야 구현해야 한다. (나는 이런 관계를 머릿속으로만 생각하면 항상 왜이렇게 헷갈리는지 모르겠다..)
"""

# Comment
"""
와.. 문제 이해하는데 진짜 오래걸렸다..
일단 왜 최소값을 최대 레슨시간인 9로 하고, 최댓값을 레슨 시간을 모두 합한 45로 지정했는지 잘 이해가 안됐다.

최소값(start)을 9로 지정한 이유는, 만약 블루레이 크기가 1일 경우 1분짜리 레슨만 블루레이에 담을 수 있고 그 이상 크기의 레슨은 블루레이에 담을 수 없다.
모든 레슨을 블루레이에 담아야 하므로 레슨 중 가장 크기가 큰 9가 최소값이 되어야 한다. 즉 블루레이 크기가 9일 경우 블루레이의 개수는 9개가 된다.
최댓값(end)을 45로 정한 이유는, 블루레이 크기가 45일 경우 모든 레슨을 1개의 블루레이에 담을 수 있기 때문이다.
"""

# Code
import sys

N, M = map(int, sys.stdin.readline().split())
lesson = list(map(int, sys.stdin.readline().split()))


def cal_bluelay_cnt(lesson, mid):
    bluelay_cnt = 1
    lesson_sum = 0
    for le in lesson:
        lesson_sum += le
        if lesson_sum > mid:
            bluelay_cnt += 1
            lesson_sum = le
    
    return bluelay_cnt


start = max(lesson)
end = sum(lesson)
while start <= end:
    mid = (start + end) // 2
    bluelay_cnt = cal_bluelay_cnt(lesson, mid)

    if bluelay_cnt > M:
        start = mid + 1
    elif bluelay_cnt <= M:
        end = mid - 1

print(start)


## 메모리: 42204 KB, 시간: 172 ms