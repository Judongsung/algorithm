from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**5)

def solution(n, inorder, postorder):
    index_map = [0]*(n+1)
    for i in range(n):
        index_map[inorder[i]] = i
    rec(index_map, inorder, postorder, 0, n-1, 0, n-1)
    
def rec(index_map, inorder, postorder, in_start, in_end, post_start, post_end):
    if in_start == in_end:
        print(inorder[in_start], end=' ')
        return
    elif in_start > in_end:
        return
    root = postorder[post_end]
    inorder_root_idx = index_map[root]
    
    in_left_start = in_start
    in_left_end = inorder_root_idx-1
    post_left_start = post_start
    post_left_end = post_start+(in_left_end-in_left_start)
    
    in_right_start = inorder_root_idx+1
    in_right_end = in_end
    post_right_start = post_left_end+1
    post_right_end = post_end-1
    
    print(root, end=' ')
    rec(index_map, inorder, postorder, in_left_start, in_left_end, post_left_start, post_left_end)
    rec(index_map, inorder, postorder, in_right_start, in_right_end, post_right_start, post_right_end)
    return

n = int(stdin.readline())
inorder = list(map(int, stdin.readline().split()))
postorder = list(map(int, stdin.readline().split()))
preorder = solution(n, inorder, postorder)