from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

def dfs(tree, parent_map, parent, cur):
    for conn in tree[cur]:
        if conn == parent:
            continue
        parent_map[conn] = cur
        dfs(tree, parent_map, cur, conn)
                
def solution(n, tree):
    parent_map = [None]*(n+1)
    dfs(tree, parent_map, None, 1)
    return parent_map[2:]
    
n = int(stdin.readline())
tree = [None]+[[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
result = solution(n, tree)
for el in result:
    print(el)