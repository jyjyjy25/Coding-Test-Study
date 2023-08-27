# BOJ_1874_스택 수열
# 난이도: 골드1
# 풀이 날짜: 23.01.01
# 풀이 시간: 1:10:12

# How to
# 빼야할 수 < top -> 불가능
# 빼야할 수가 stack에 존재하지 않으면 그만큼 수 push
# 뺴야할 수가 top보다 작으면 NO를 출력 후 break
# 그렇지 않으면 top을 pop

# Comment
# 10%에서 시간초과 뜸
# 교재 코드랑 거의 유사한거 같은데 어디서 시간을 잡아먹는건지..?
# count()가 좀 오래걸리나

# Code
import sys
n = int(sys.stdin.readline())
order = list(int(sys.stdin.readline()) for _ in range(n))

stack = []
num = 0
answer = ""
for i in range(n):
    if stack.count(order[i]) == 0:
        for j in range(order[i]-num):
            num += 1
            stack.append(num)
            answer += "+\n"
    if order[i] < stack[-1]:
        print("NO")
        break
    else:
        stack.pop()
        answer += "-\n"

if len(stack)==0:
    print(answer)



## 메모리:  KB, 시간:  ms