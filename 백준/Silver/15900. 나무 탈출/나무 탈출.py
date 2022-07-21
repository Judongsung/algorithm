from sys import stdin
from collections import deque

def solution(graph):
    total_path_length = 0
    visited = [False for _ in graph]
    queue = deque([(1, 0)])
    visited[1] = True
    
    while queue:
        node, path_length = queue.pop()
        connected_nodes = graph[node]
        
        if len(connected_nodes) == 1 and visited[connected_nodes[0]]:
            total_path_length += path_length
            continue
        
        for conn in connected_nodes:
            if visited[conn]:
                continue
            queue.append((conn, path_length+1))
            visited[conn] = True
            
    return 'Yes' if total_path_length%2==1 else 'No'

n = int(stdin.readline())
graph = [None]+[[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

result = solution(graph)
print(result)