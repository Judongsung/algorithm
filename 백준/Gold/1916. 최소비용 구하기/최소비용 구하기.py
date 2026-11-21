from sys import stdin
from heapq import heappop, heappush

INF = 100_000 * 100_000

n = int(stdin.readline())
m = int(stdin.readline())

graph = [[INF for __ in range(n)] for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for i in range(m):
    start, end, cost = map(int, stdin.readline().split())
    start -= 1
    end -= 1
    
    if cost < graph[start][end]:
        graph[start][end] = cost

target_start, target_end = map(int, stdin.readline().split())
target_start -= 1
target_end -= 1

min_distances = [INF for _ in range(n)]
not_visited = set([i for i in range(n)])
hq = []

for i in range(n):
    heappush(hq, (graph[target_start][i], i))

while target_end in not_visited:
    d, cur = heappop(hq)
    
    if cur in not_visited:
        min_distances[cur] = d
        not_visited.remove(cur)
        
        for nxt in not_visited:
            heappush(hq, (d + graph[cur][nxt], nxt))

print(min_distances[target_end])