from sys import stdin

NOT_VISITED = -1

def check_graph(graph, binary_map, root):
    result = True
    queue = [(root, False)]
    flag = True
    
    while flag and queue:
        num, state = queue.pop()
        binary_map[num] = state
        state = not state
        for connected in graph[num]:
            if binary_map[connected] != NOT_VISITED:
                if binary_map[connected] != state:
                    result = False
                    flag = False
                    break
                continue
            queue.append((connected, state))
    
    return result

k = int(stdin.readline())
for _ in range(k):
    v, e = map(int, stdin.readline().split())
    graph = [None]+[[] for __ in range(v)]
    for __ in range(e):
        u, v = map(int, stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    binary_map = [NOT_VISITED for __ in graph]
    result = 'YES'
    
    for i in range(1, v+1):
        if binary_map[i] == NOT_VISITED and not check_graph(graph, binary_map, i):
            result = 'NO'
            break
    print(result)