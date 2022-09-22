from sys import stdin
from collections import deque

EMPTY = '0'
WALL = '1'
DIRS = [(1, 0), (0, 1), (0, -1), (-1, 0)]

def find_min_distance():
    global visited
    goal = (n-1, m-1)
    queue = deque([(0, 0, k, 0)])
    visited = [[-1 for __ in range(m)] for _ in range(n)]
    visited[0][0] = k
    
    while queue:
        r, c, breakable, distance = queue.popleft()
        if (r, c) == goal:
            min_distance = distance+1
            break
        
        for r_dir, c_dir in DIRS:
            next_r = r+r_dir
            next_c = c+c_dir
            if 0 <= next_r < n and 0 <= next_c < m:
                if board[next_r][next_c] == EMPTY and breakable > visited[next_r][next_c]:
                    queue.append((next_r, next_c, breakable, distance+1))
                    visited[next_r][next_c] = breakable
                elif breakable and breakable-1 > visited[next_r][next_c]:
                    queue.append((next_r, next_c, breakable-1, distance+1))
                    visited[next_r][next_c] = breakable-1
    else:
        min_distance = -1
    
    return min_distance

n, m, k = map(int, stdin.readline().split())
board = [stdin.readline().rstrip() for _ in range(n)]
result = find_min_distance()
print(result)