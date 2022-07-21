from sys import stdin
from collections import deque

def get_node_depths(tree):
    node_depths = [-1 for _ in tree]
    queue = deque([(1, 0)])
    node_depths[1]= 0
    
    while queue:
        node, depth = queue.pop()
        
        for conn in tree[node]:
            if node_depths[conn] > -1:
                continue
            node_depths[conn] = depth+1
            queue.append((conn, depth+1))
    
    return node_depths

def get_parent(tree, node_depths, node):
    for conn in tree[node]:
        if node_depths[conn] < node_depths[node]:
            return conn

def find_common_ancestor(tree, node_depths, a, b):
    if node_depths[a] < node_depths[b]:
        a, b = b, a
    a_ancestor = a
    b_ancestor = b
    a_ancestor_depth = node_depths[a]
    b_ancestor_depth = node_depths[b]
    
    while a_ancestor_depth > b_ancestor_depth:
        a_ancestor = get_parent(tree, node_depths, a_ancestor)
        a_ancestor_depth = node_depths[a_ancestor]
    
    while a_ancestor != b_ancestor:
        a_ancestor = get_parent(tree, node_depths, a_ancestor)
        b_ancestor = get_parent(tree, node_depths, b_ancestor)
    
    return a_ancestor

n = int(stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
node_depths = get_node_depths(tree)
m = int(stdin.readline())
for _ in range(m):
    flag = True
    visited = [False for _ in range(n+1)]
    one, other = map(int, stdin.readline().split())
    result = find_common_ancestor(tree, node_depths, one, other)
    print(result)