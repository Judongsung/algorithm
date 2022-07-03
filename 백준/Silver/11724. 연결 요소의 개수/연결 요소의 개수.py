from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

def dfs(graph, node, not_visited):
    if node not in not_visited:
        return
    
    not_visited.remove(node)
    children = graph[node]
    
    for child in children:
        dfs(graph, child, not_visited)
        
    return

count = 0
graph = {}
n, m = map(int, stdin.readline().split())
for i in range(1, n+1):
    graph[i] = []
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

not_visited = set(range(1, n+1))

while not_visited:
    node = list(not_visited)[0]
    dfs(graph, node, not_visited)
    count += 1

print(count)