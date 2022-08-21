from sys import stdin
from collections import deque

SHORTER = 0
LONGER = 1

n, m = map(int, stdin.readline().split())
graph = [[set(), []] for _ in range(n+1)]
graph[0][SHORTER].add(None)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][LONGER].append(b)
    graph[b][SHORTER].add(a)

queue = deque()
result = []
for num, node in enumerate(graph):
    if not node[SHORTER]:
        queue.append(num)

while queue:
    num = queue.popleft()
    node = graph[num]
    result.append(str(num))
    
    for longer_num in node[LONGER]:
        graph[longer_num][SHORTER].remove(num)
        if not graph[longer_num][SHORTER]:
            queue.append(longer_num)
            
print(' '.join(result))