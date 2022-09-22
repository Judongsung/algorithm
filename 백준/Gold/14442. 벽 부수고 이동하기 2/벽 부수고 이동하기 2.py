from sys import stdin
from collections import deque

INF = 10**8
EMPTY = '0'
WALL = '1'
DIRS = [(1, 0), (0, 1), (0, -1), (-1, 0)]

def find_min_distance():
    min_distance = INF
    goal = (n-1, m-1)
    queue = deque([(0, 0, k, 0)])
    visited = [[[False for ___ in range(k+1)] for __ in range(m)] for _ in range(n)]
    visited[0][0][k] = True
    
    while queue:
        r, c, breakable, distance = queue.popleft()
        if (r, c) == goal:
            min_distance = distance+1
            break
        
        for r_dir, c_dir in DIRS:
            next_r = r+r_dir
            next_c = c+c_dir
            if 0 <= next_r < n and 0 <= next_c < m:
                if board[next_r][next_c] == EMPTY and not visited[next_r][next_c][breakable]:
                    queue.append((next_r, next_c, breakable, distance+1))
                    visited[next_r][next_c][breakable] = True
                elif breakable and not visited[next_r][next_c][breakable-1]:
                    queue.append((next_r, next_c, breakable-1, distance+1))
                    visited[next_r][next_c][breakable-1] = True
    else:
        min_distance = -1
    
    return min_distance

n, m, k = map(int, stdin.readline().split())
board = [stdin.readline().rstrip() for _ in range(n)]
result = find_min_distance()
print(result)