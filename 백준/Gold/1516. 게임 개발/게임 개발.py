from sys import stdin
from collections import deque

PREV_COUNT = 0
PREV_LIST = 1
AFTER_LIST = 2

n = int(stdin.readline())
graph = [[0, None, []] for _ in range(n+1)]
build_times = [0 for _ in range(n+1)]
memo = [0 for _ in range(n+1)]
queue = deque([])
for i in range(1, n+1):
    info = list(map(int, stdin.readline().split()))
    memo[i] = info[0]
    prev_tech = info[1:-1]
    
    if not prev_tech:
        queue.append(i)
    else:
        graph[i][PREV_COUNT] = len(prev_tech)
        graph[i][PREV_LIST] = prev_tech
        for prev in prev_tech:
            graph[prev][AFTER_LIST].append(i)
            
while queue:
    cur = queue.popleft()
    if graph[cur][PREV_LIST]:
        memo[cur] += max([memo[prev] for prev in graph[cur][PREV_LIST]])
    
    for after in graph[cur][AFTER_LIST]:
        graph[after][PREV_COUNT] -= 1
        if not graph[after][PREV_COUNT]:
            queue.append(after)
            
for time in memo[1:]:
    print(time)