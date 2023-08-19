# BOJ_10999_구간 합 구하기 2
# 난이도: 실버1
# 풀이 날짜: 23.08.16
# 풀이 시간:

# How to

# - 펜윅 트리 사용시 런타임 에러 발생
# - 세그먼트 트리를 이용해 해결

# Code

import sys

def init_tree(arr, tree, start, end, node):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        init_tree(arr, tree, start, mid, node * 2)
        init_tree(arr, tree, mid + 1, end, node * 2 + 1)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def update_tree(tree, lazy, start, end, node, idx_start, idx_end, diff):
    update_lazy(tree, lazy, start, end, node)

    if idx_start > end or start > idx_end:
        return
    
    if start >= idx_start and idx_end >= end:
        tree[node] += (end - start + 1) * diff
        if start != end:
            lazy[node * 2] += diff
            lazy[node * 2 + 1] += diff
        return
    
    mid = (start + end) // 2
    update_tree(tree, lazy, start, mid, node * 2, idx_start, idx_end, diff)
    update_tree(tree, lazy, mid + 1, end, node * 2 + 1, idx_start, idx_end, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def update_lazy(tree, lazy, start, end, node):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
      
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
      
        lazy[node] = 0


def query_tree(tree, lazy, start, end, node, left, right):
    update_lazy(tree, lazy, start, end, node)

    if left > end or start > right:
        return 0
    
    if start >= left and right >= end:
        return tree[node]
    
    mid = (start + end) // 2
    return query_tree(tree, lazy, start, mid, node * 2, left, right) + query_tree(tree, lazy, mid + 1, end, node * 2 + 1, left, right)


## 메모리: 188528 KB,  시간: 1976 ms