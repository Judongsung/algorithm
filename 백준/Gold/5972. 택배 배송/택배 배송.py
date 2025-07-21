from sys import stdin
from heapq import heappush, heappop


def find_min_cost(nodes: list, start: int, target: int) -> int:
    min_cost = [float('inf')]*len(nodes)
    visited = [False]*len(nodes)
    min_cost[start] = 0
    remain_nodes = [(0, start)]

    while not all(visited):
        while visited[remain_nodes[0][1]]:
            heappop(remain_nodes)
        _, cur = heappop(remain_nodes)
        for connected, cost in nodes[cur]:
            move_cost = min_cost[cur]+cost
            if move_cost < min_cost[connected]:
                min_cost[connected] = move_cost
                heappush(remain_nodes, (move_cost, connected))
        visited[cur] = True
    
    return min_cost[target]


n, m = map(int, stdin.readline().rstrip().split())
nodes = [[] for _ in range(n)]
for _ in range(m):
    one, other, cost = map(int, stdin.readline().rstrip().split())
    one, other = one-1, other-1 # 1 based index to 0 based index
    nodes[one].append((other, cost))
    nodes[other].append((one, cost))
        
print(find_min_cost(nodes, 0, n-1))