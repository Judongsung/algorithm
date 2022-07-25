from sys import stdin
from collections import deque

def get_distance(tree, visited, start, goal):
    queue = deque([(start, 0)])
    visited[start] = True
    
    flag = True
    while flag and queue:
        cur_node, cur_distance = queue.popleft()
        
        for conn in tree[cur_node]:
            if visited[conn]:
                continue
            next_distance = cur_distance+tree[cur_node][conn]
            if conn == goal:
                result = next_distance
                flag = False
                break
            else:
                queue.append((conn, next_distance))
                visited[conn] = True
    
    return result

n, m = map(int, stdin.readline().split())
tree = [None]+[{} for _ in range(n)]
for _ in range(n-1):
    one, other, distance = map(int, stdin.readline().split())
    tree[one][other] = distance
    tree[other][one] = distance
for _ in range(m):
    one, other = map(int, stdin.readline().split())
    visited = [False for _ in tree]
    result = get_distance(tree, visited, one, other)
    print(result)