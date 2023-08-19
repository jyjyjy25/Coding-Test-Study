import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
idx = sys.stdin.readline().strip().split(' ')
idx = list(map(int, idx))

count = 0
while idx:
    target = m - idx[0]
    if(idx.count(target)==0):
        idx.pop(0)
    else:
        targetIdx = idx.index(target)
        idx.pop(targetIdx)
        idx.pop(0)
        count += 1
print(count)