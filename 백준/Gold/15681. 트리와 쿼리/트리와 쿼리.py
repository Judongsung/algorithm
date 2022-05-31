from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)
    
def get_tree_map(n, lines):
    tree_map = {}
    for i in range(1, n+1):
        tree_map[i] = []
    for n1, n2 in lines:
        tree_map[n1].append(n2)
        tree_map[n2].append(n1)
    
    return tree_map

def set_subtree_count_map(node_map, cur, parent, count_map):
    count = 1
    for el in node_map[cur]:
        if el == parent:
            continue
        count += set_subtree_count_map(node_map, el, cur, count_map)
    count_map[cur] = count
    return count

def solution(n, r, q, lines, ulist):
    tree_map = get_tree_map(n, lines)
    subtree_count_map = {}
    set_subtree_count_map(tree_map, r, None, subtree_count_map)
    result = [0]*q
    for i, u in enumerate(ulist):
        count = subtree_count_map[u]
        result[i] = count
    return result

n, r, q = map(int, stdin.readline().split())
lines = [list(map(int, stdin.readline().split())) for _ in range(n-1)]
ulist = [0] * q
for i in range(q):
    ulist[i] = int(stdin.readline())
result = solution(n, r, q, lines, ulist)
for el in result:
    print(el)