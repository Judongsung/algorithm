def bfs_push(queue, node):
    queue.append(node)
    
def dfs_push(queue, node):
    queue.insert(0, node)
    
def search(graph, root, search_type):
    if search_type == 'dfs':
        push_func = dfs_push
        for node in graph:
            node.sort(reverse=True)
    else:
        push_func = bfs_push
        for node in graph:
            node.sort()
    search_order = []
    visited = [False for _ in graph]
    queue = [root]
    while queue:
        node = queue.pop(0)
        if visited[node]:
            continue
        visited[node] = True
        search_order.append(node)
        
        for conn in graph[node]:
            if visited[conn]:
                continue
            push_func(queue, conn)
    
    return search_order

def solution(n, m, v, lines):
    graph = [[] for _ in range(n+1)]
    for n1, n2 in lines:
        if n2 in graph[n1]:
            continue
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    dfs_result = search(graph, v, 'dfs')
    bfs_result = search(graph, v, 'bfs')
    
    return [dfs_result, bfs_result]

n, m, v = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(m)]
result = solution(n, m, v, lines)
for r in result:
    r = map(str, r)
    print(" ".join(r))