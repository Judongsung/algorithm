from sys import stdin
from heapq import heappush, heappop


TIME = 0
PREV_REMAINS = 1
NEXT_NODES = 2

def find_min_time(schedules: list[list[int]]) -> int:
    graph = [[0, 0, []] for _ in schedules] # [time, prev_remains, next_nodes]
    q = []

    for i, s in enumerate(schedules):
        graph[i][TIME] = s[0]
        graph[i][PREV_REMAINS] = s[1]
        
        for j in range(s[1]):
            graph[s[2+j]][NEXT_NODES].append(i)

        if graph[i][PREV_REMAINS] == 0:
            heappush(q, [graph[i][TIME], i])

    while q:
        time, node = heappop(q)
        
        for next_node in graph[node][NEXT_NODES]:
            graph[next_node][PREV_REMAINS] -= 1
            
            if graph[next_node][PREV_REMAINS] == 0:
                heappush(q, [time+graph[next_node][TIME], next_node])

    return time

n = int(stdin.readline())
schedules = []
for _ in range(n):
    info = list(map(int, stdin.readline().rstrip().split()))
    for i in range(info[1]):
        info[2+i] -= 1 # 1-base index to 0-base index

    schedules.append(info)

print(find_min_time(schedules))