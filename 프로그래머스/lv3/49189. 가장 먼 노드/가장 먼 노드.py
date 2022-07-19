from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in graph]
    for node1, node2 in edge:
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    queue = deque([(1, 0)])
    visited[1] = True
    max_distance = 0
    max_distance_count = 0
    
    while queue:
        node, distance = queue.popleft()
        if distance > max_distance:
            max_distance = distance
            max_distance_count = 1
        elif distance == max_distance:
            max_distance_count += 1
        
        for near_node in graph[node]:
            if visited[near_node]:
                continue
            queue.append((near_node, distance+1))
            visited[near_node] = True
    
    return max_distance_count