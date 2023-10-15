# BOJ_1300_골드3
# 난이도: 골드1
# 풀이 날짜: 23.10.15
# 풀이 시간:

# How to


# Comment
# 처음엔 행렬을 다 만들까 하다가 시간 제약 때문에 다른 방법을 찾음
# 전~혀 생각나지 않고 책도 이해가 잘 안 돼서 블로그 참고함

# [중요한 아이디어1 - B[k] = x의 의미]
# B[k] = x란 B에서 k번째 값은 x라는 의미
# 이는 곧 x보다 같거나 작은 값의 개수가 k개(B는 오름차순이므로)
# x보다 작거나 같은 수의 개수가 k개인 x를 찾으면 됨

# [중요한 아이디어2]
# 각 행에서 x보다 작은 값의 개수는 k/행의 몫과 같다.

# 아이디어를 떠올리기가 너무 어려운 문제였던 것 같다.

# Code
import sys
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
s = 0
e = k
ans = 0

while s <= e:
    mid = (s+e)//2
    count = 0

    for i in range(1, n+1):
        count += min(mid//i, n)

    if count >= k:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)


## 메모리:  31252KB, 시간:  1072ms