from sys import stdin
from collections import deque

def get_tree_count(n, graph):
    count = 0
    visited = [False for _ in graph]
    visited[0] = True
    
    for node in range(1, n+1):
        if visited[node]:
            continue
        if is_tree(graph, visited, node):
            count += 1
    
    return count

def is_tree(graph, visited, node):
    result = True
    queue = deque([node])
    visited[node] = True
    
    while queue:
        cur_node = queue.pop()
        
        visited_conn_count = 0
        for conn in graph[cur_node]:
            if visited[conn]:
                visited_conn_count += 1
                continue
            queue.append(conn)
            visited[conn] = True
        
        if visited_conn_count > 1:
            result = False
    
    return result

case = 0
while True:
    case += 1
    result = 'Case %d: '%case
    n, m = map(int, stdin.readline().split())
    if n == m == 0:
        break
    graph = [None]+[[] for _ in range(n)]
    for _ in range(m):
        one, other = map(int, stdin.readline().split())
        graph[one].append(other)
        graph[other].append(one)
    
    tree_count = get_tree_count(n, graph)
    if tree_count == 0:
        result += 'No trees.'
    elif tree_count == 1:
        result += 'There is one tree.'
    else:
        result += 'A forest of %d trees.'%tree_count
    print(result)