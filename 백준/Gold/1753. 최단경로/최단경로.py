from sys import stdin
import heapq

NUM = 0
WEIGHT = 1
VISITED = 2
INF = 10**9

v, e = map(int, stdin.readline().split())
root = int(stdin.readline())
graph = [[] for _ in range(v+1)]
min_distance = [INF for _ in range(v+1)]
for _ in range(e):
    a, b, w = map(int, stdin.readline().split())
    graph[a].append([b, w])

queue = []
heapq.heappush(queue, (0, root))

while queue:
    distance, node = heapq.heappop(queue)
    
    if distance < min_distance[node]:
        min_distance[node] = distance
        
        for near_node, weight in graph[node]:
            heapq.heappush(queue, (distance+weight, near_node))
        
for distance in min_distance[1:]:
    if distance == INF:
        distance = 'INF'
    print(distance)