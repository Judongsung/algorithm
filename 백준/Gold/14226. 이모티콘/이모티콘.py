from sys import stdin
from collections import deque


def find_min_time(goal: int) -> int:
    max_n = 2000
    q = deque()
    q.append((1, 0, 0)) # cur, clipboard, time
    visited = [[False]*max_n for _ in range(max_n)] # visited[cur][clipboard]
    visited[1][0] = True

    while q:
        cur, clipboard, time = q.popleft()

        if cur != clipboard and not visited[cur][cur]:
            q.append((cur, cur, time+1))
            visited[cur][cur] = True

        if cur+clipboard < max_n and not visited[cur+clipboard][clipboard]:
            if cur+clipboard == goal:
                return time+1
                
            q.append((cur+clipboard, clipboard, time+1))
            visited[cur+clipboard][clipboard] = True

        if cur-1 > 0 and not visited[cur-1][clipboard]:
            if cur-1 == goal:
                return time+1
                
            q.append((cur-1, clipboard, time+1))
            visited[cur-1][clipboard] = True
    
s = int(stdin.readline())
print(find_min_time(s))