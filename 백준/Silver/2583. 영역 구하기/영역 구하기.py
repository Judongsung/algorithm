from sys import stdin
from collections import deque

dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def get_area_size(r, c):
    queue = deque([(r, c)])
    board[r][c] = True
    size = 0
    
    while queue:
        cur_r, cur_c = queue.pop()
        size += 1
        
        for r_dir, c_dir in dirs:
            next_r = cur_r+r_dir
            next_c = cur_c+c_dir
            
            if 0 <= next_r < m and 0 <= next_c < n and not board[next_r][next_c]:
                queue.append((next_r, next_c))
                board[next_r][next_c] = True
    
    return size

m, n, k = map(int, stdin.readline().split())
board = [[False for __ in range(n)] for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = True

area_sizes = []
for i in range(m):
    for j in range(n):
        if not board[i][j]:
            size = get_area_size(i, j)
            area_sizes.append(str(size))

area_sizes.sort(key=lambda x:int(x))
print(len(area_sizes))
print(' '.join(area_sizes))