from sys import stdin
from collections import deque

EMPTY = '0'
WALL = '1'
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

n, m = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(n)]
visited = [[[False]*2 for __ in range(m)] for _ in range(n)]
goal = (n-1, m-1)
queue = deque([(0, 0, 1, False)])
result = -1

while queue:
    r, c, count, crashed = queue.popleft()
    if visited[r][c][crashed]:
        continue
    elif (r, c) == goal:
        result = count
        break
        
    visited[r][c][crashed] = True
    
    for r_dir, c_dir in dirs:
        next_r = r+r_dir
        next_c = c+c_dir
        if 0 <= next_r < n and 0 <= next_c < m:
            if board[next_r][next_c] == EMPTY:
                queue.append((next_r, next_c, count+1, crashed))
            elif board[next_r][next_c] == WALL and not crashed:
                queue.append((next_r, next_c, count+1, True))

print(result)