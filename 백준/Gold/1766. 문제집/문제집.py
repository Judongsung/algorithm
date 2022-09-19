from sys import stdin
from heapq import heappush, heappop

PRE_COUNT = 0
AFTER_SET = 1

n, m = map(int, stdin.readline().split())
graph = [[0, set()] for _ in range(n+1)]
graph[0][PRE_COUNT] = -1
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][AFTER_SET].add(b)
    graph[b][PRE_COUNT] += 1
result = []
    
hq = [i for i, el in enumerate(graph) if not el[PRE_COUNT]]

while hq:
    cur = heappop(hq)
    
    for after in graph[cur][AFTER_SET]:
        graph[after][PRE_COUNT] -= 1
        if not graph[after][PRE_COUNT]:
            heappush(hq, after)
    
    result.append(str(cur))
    
print(' '.join(result))