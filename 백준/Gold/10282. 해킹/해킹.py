from sys import stdin
from collections import deque

INF = 10**8

t = int(stdin.readline())
for _ in range(t):
    n, d, c = map(int, stdin.readline().split())
    c -= 1
    dependency = [[] for _ in range(n)]
    times = [INF for _ in range(n)]
    times[c] = 0
    for _ in range(d):
        a, b, s = map(int, stdin.readline().split())
        dependency[b-1].append((a-1, s))
    queue = deque([(c, 0)])
    max_time = 0
    com_count = 0
    
    while queue:
        num, until_time = queue.popleft()
        
        for depend, hack_time in dependency[num]:
            next_time = until_time+hack_time
            if next_time < times[depend]:
                times[depend] = next_time
                queue.append((depend, next_time))
            
    for time in times:
        if time != INF:
            com_count += 1
            if time > max_time:
                max_time = time
    print(com_count, max_time)