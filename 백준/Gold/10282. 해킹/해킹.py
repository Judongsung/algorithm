from sys import stdin
from collections import deque

t = int(stdin.readline())
for _ in range(t):
    n, d, c = map(int, stdin.readline().split())
    dependency = [[] for _ in range(n)]
    times = [10**8 for _ in range(n)]
    times[c-1] = 0
    for _ in range(d):
        a, b, s = map(int, stdin.readline().split())
        dependency[b-1].append((a-1, s))
    queue = deque([(c-1, 0)])
    com_count = 0
    
    while queue:
        num, until_time = queue.popleft()
        
        for depend, hack_time in dependency[num]:
            next_time = until_time+hack_time
            if next_time < times[depend]:
                times[depend] = next_time
                queue.append((depend, next_time))
            
    connected = [time for time in times if time < 10**8]
    print(len(connected), max(connected))