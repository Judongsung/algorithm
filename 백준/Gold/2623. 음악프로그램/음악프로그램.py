from sys import stdin
from collections import deque

PREV_COUNT = 0
NEXT_NUMS = 1

n, m = map(int, stdin.readline().split())
result = []
graph = [[0, []] for _ in range(n+1)]
graph[0][PREV_COUNT] = 1
queue = deque()
for _ in range(m):
    data = list(map(int, stdin.readline().split()))
    num = data[0]
    order = data[1:]
    for i in range(num-1):
        a = order[i]
        b = order[i+1]
        graph[a][NEXT_NUMS].append(b)
        graph[b][PREV_COUNT] += 1
    
queue += [i for i, node in enumerate(graph) if not node[PREV_COUNT]]
    
flag = True
while flag and queue:
    num = queue.popleft()
    node = graph[num]
    result.append(num)
    
    for next_num in node[NEXT_NUMS]:
        next_node = graph[next_num]
        if next_node in result:
            flag = False
            break
        next_node[PREV_COUNT] -= 1
        if next_node[PREV_COUNT] == 0:
            queue.append(next_num)
            
if len(result) < n:
    result = [0]

for num in result:
    print(num)