from sys import stdin
from heapq import heappush, heappop

INF = 10**8

def find_min_time(start, goal):
    queue = [(0, start)]
    visited = [INF for _ in range(n+1)]
    visited[start] = 0
    
    while queue:
        time, cur = heappop(queue)
        if cur == goal:
            result = time
            break
        
        for i in range(1, n+1):
            next_time = time+matrix[cur][i]
            if next_time < visited[i]:
                heappush(queue, (next_time, i))
                visited[i] = next_time
                
    return result

def find_all_min_time(start):
    queue = [(0, start)]
    visited = [INF for _ in range(n+1)]
    visited[start] = 0
    
    while queue:
        time, cur = heappop(queue)
        for i in range(1, n+1):
            next_time = time+matrix[cur][i]
            if next_time < visited[i]:
                heappush(queue, (next_time, i))
                visited[i] = next_time
                
    return visited

max_time = 0
n, m, x = map(int, stdin.readline().split())
matrix = [[INF for __ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    start, end, time = map(int, stdin.readline().split())
    matrix[start][end] = time
        
go_back_time = find_all_min_time(x)
for start in range(1, n+1):
    time = find_min_time(start, x)+go_back_time[start]
    if time > max_time:
        max_time = time
        
print(max_time)