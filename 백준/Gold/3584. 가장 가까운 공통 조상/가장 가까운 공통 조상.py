from sys import stdin
from collections import deque

PARENT = 0
CHILDREN = 1

def init_level(graph, root):
    levels = [0 for _ in range(n+1)]
    queue = deque([(root, 0)])
    
    while queue:
        node, level = queue.popleft()
        levels[node] = level
        
        for child in graph[node][CHILDREN]:
            queue.append((child, level+1))
    
    return levels

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    graph = [[None, []] for _ in range(n+1)]
    not_child = set(range(1, n+1))
    
    for _ in range(n-1):
        parent, child = map(int, stdin.readline().split())
        graph[parent][CHILDREN].append(child)
        graph[child][PARENT] = parent
        not_child.discard(child)
        
    root = not_child.pop()
    levels = init_level(graph, root)
    one, other = map(int, stdin.readline().split())
    
    while one != other:
        if levels[one] < levels[other]:
            other = graph[other][PARENT]
        else:
            one = graph[one][PARENT]
    
    print(one)