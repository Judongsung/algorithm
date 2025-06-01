from sys import stdin
from typing import List


LEFT = 0
RIGHT = 1

def restore_tree(preorder:List[int], inorder:List[int]) -> List[List[int]]:
    tree = [[None, None] for _ in range(len(preorder)+1)]
    inorder_idx_map = [None for _ in range(len(inorder)+1)] # 노드가 1번부터 있어서 index 0은 더미데이터
    for i, node in enumerate(inorder):
        inorder_idx_map[node] = i
    pre_idx = 0

    def build(in_left:int, in_right:int) -> int:
        nonlocal pre_idx
        if in_left > in_right:
            return None

        cur = preorder[pre_idx]
        pre_idx += 1

        root_in_idx = inorder_idx_map[cur]

        left = build(in_left, root_in_idx-1)
        right = build(root_in_idx+1, in_right)

        tree[cur][LEFT] = left
        tree[cur][RIGHT] = right

        return cur
        
    build(0, len(inorder)-1)
    return tree

def postorder(tree:List[List[int]], cur:int) -> List[int]:
    result = []

    if tree[cur][LEFT]:
        result += postorder(tree, tree[cur][LEFT])
    if tree[cur][RIGHT]:
        result += postorder(tree, tree[cur][RIGHT])
        
    result.append(cur)
    return result

t = int(stdin.readline().rstrip())
for _ in range(t):
    n = int(stdin.readline().rstrip())
    preorder = list(map(int, stdin.readline().rstrip().split()))
    inorder = list(map(int, stdin.readline().rstrip().split()))
    tree = restore_tree(preorder, inorder)
    result = postorder(tree, preorder[0])
    print(' '.join(list(map(str, result))))