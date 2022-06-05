from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

def dfs(tree, parent_map, parent, cur):
    for conn in tree[cur]:
        if conn == parent:
            continue
        parent_map[conn] = cur
        dfs(tree, parent_map, cur, conn)
                
def solution(n, relations):
    parent_map = [None]*(n+1)
    tree = [None]+[[] for _ in range(n)]
    for a, b in relations:
        tree[a].append(b)
        tree[b].append(a)
    
    dfs(tree, parent_map, None, 1)
    return parent_map[2:]
    
n = int(stdin.readline())
relations = [list(map(int, stdin.readline().split())) for _ in range(n-1)]
result = solution(n, relations)
for el in result:
    print(el)