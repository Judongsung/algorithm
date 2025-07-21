from sys import stdin
from heapq import heappush, heappop


def find_min_cost(graph: list, start: int, target: int) -> int:
    min_cost = [float('inf')]*len(graph)
    visited = [False]*len(graph)
    min_cost[start] = 0
    remain_nodes = [(0, start)]

    while remain_nodes:
        dist, cur = heappop(remain_nodes)
        if cur == target:
            return dist
        if dist < min_cost[cur]:
            continue
        for connected, cost in graph[cur]:
            move_cost = dist+cost
            if move_cost < min_cost[connected]:
                min_cost[connected] = move_cost
                heappush(remain_nodes, (move_cost, connected))
    
    return min_cost[target]


n, m = map(int, stdin.readline().rstrip().split())
nodes = [[] for _ in range(n)]
for _ in range(m):
    one, other, cost = map(int, stdin.readline().rstrip().split())
    one, other = one-1, other-1 # 1 based index to 0 based index
    nodes[one].append((other, cost))
    nodes[other].append((one, cost))
        
print(find_min_cost(nodes, 0, n-1))