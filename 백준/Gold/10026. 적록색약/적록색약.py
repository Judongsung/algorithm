from sys import stdin
from collections import deque

def check_color(one, other, is_color_weak):
    if one == other or (is_color_weak and one in ('R', 'G') and other in ('R', 'G')):
        return True
    return False

def find_area(start_r, start_c, grid, visited, is_color_weak):
    color = grid[start_r][start_c]
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    
    while queue:
        r, c = queue.popleft()
        for r_dir, c_dir in dirs:
            near_r = r+r_dir
            near_c = c+c_dir
            if 0 <= near_r < n and 0 <= near_c < n and not visited[near_r][near_c]:
                near_color = grid[near_r][near_c]
                if check_color(color, near_color, is_color_weak):
                    queue.append((near_r, near_c))
                    visited[near_r][near_c] = True

n = int(stdin.readline())
grid = [stdin.readline() for _ in range(n)]
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
cw_area = 0
n_area = 0

visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            find_area(i, j, grid, visited, False)
            n_area += 1
            
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            find_area(i, j, grid, visited, True)
            cw_area += 1

print(n_area, cw_area)