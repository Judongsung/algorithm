from sys import stdin
from heapq import heappush, heappop

INF = 10**6
DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

count = 0
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    count += 1
    board = [list(map(int, stdin.readline().split())) for _ in range(n)]
    queue = [(0, 0, 0)]
    visited = [[10**6 for __ in range(n)] for _ in range(n)]
    goal = (n-1, n-1)
    
    while queue:
        loss, r, c = heappop(queue)
        loss += board[r][c]
        if (r, c) == goal:
            min_loss = loss
            break
        elif loss >= visited[r][c]:
            continue
        visited[r][c] = loss
        
        for r_dir, c_dir in DIRS:
            next_r = r+r_dir
            next_c = c+c_dir
            if 0 <= next_r < n and 0 <= next_c < n:
                heappush(queue, (loss, next_r, next_c))
          
    print('Problem %d: %d'%(count, min_loss))