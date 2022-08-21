from sys import stdin
from collections import deque

SHORTER = 0
LONGER = 1

n, m = map(int, stdin.readline().split())
graph = [[0, []] for _ in range(n+1)]
graph[0][SHORTER] = 1
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][LONGER].append(b)
    graph[b][SHORTER] += 1

queue = deque()
result = []
for num, node in enumerate(graph):
    if node[SHORTER] == 0:
        queue.append(num)

while queue:
    num = queue.popleft()
    node = graph[num]
    result.append(str(num))
    
    for longer_num in node[LONGER]:
        graph[longer_num][SHORTER] -= 1
        if graph[longer_num][SHORTER] == 0:
            queue.append(longer_num)
            
print(' '.join(result))