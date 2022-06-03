def get_distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def dfs(graph, visited, cur, goal):
    visited[cur] = True
    if cur == goal:
        return True
    
    for conn in graph[cur]:
        if visited[conn]:
            continue
        if dfs(graph, visited, conn, goal):
            return True
    
    return False

def solution(n, home, markets, goal):
    maximum_move = 1000
    result = 'sad'
    graph = [[] for _ in range(n+2)]
    visited = [False for _ in graph]
    locations = [home]+markets+[goal]
    for i, a in enumerate(locations):
        for j, b in enumerate(locations[i+1:]):
            if get_distance(a, b) <= 1000:
                b_idx = i+j+1
                graph[i].append(b_idx)
                graph[b_idx].append(i)
    
    if dfs(graph, visited, 0, n+1):
        result = 'happy'
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    home = tuple(map(int, input().split()))
    markets = [tuple(map(int, input().split())) for __ in range(n)]
    goal = tuple(map(int, input().split()))
    result = solution(n, home, markets, goal)
    print(result)