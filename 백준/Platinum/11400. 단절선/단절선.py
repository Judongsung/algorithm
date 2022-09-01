from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

def dfs(node, parent=-1):
    global next_order
    order_list[node] = next_order
    min_connect_order = next_order
    next_order += 1
    
    for connect in graph[node]:
        if connect == parent:
            continue
        elif order_list[connect] == -1:
            low = dfs(connect, node)
            if low > order_list[node]:
                result.append(get_pair(node, connect))
        else:
            low = order_list[connect]
        min_connect_order = min(min_connect_order, low)
    
    return min_connect_order
            
def get_pair(one, other):
    if one > other:
        one, other = other, one
    return (one, other)

v, e = map(int, stdin.readline().split())
graph = [[] for _ in range(v+1)]
order_list = [-1 for _ in range(v+1)]
next_order = 0
for _ in range(e):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
result = []

dfs(1)
print(len(result))
for a, b in sorted(result):
    print(a, b)