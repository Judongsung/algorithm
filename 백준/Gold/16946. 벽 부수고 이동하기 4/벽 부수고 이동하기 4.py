from sys import stdin
from collections import deque

EMPTY = '0'
WALL = '1'
DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def find_empty_group(start_r, start_c):
    global next_group
    group = next_group
    next_group += 1
    count = 0
    queue = deque([(start_r, start_c)])
    visited = set()
    
    while queue:
        r, c = queue.pop()
        if (r, c) in visited:
            continue
        loc_group_dict[(r, c)] = group
        count += 1
        visited.add((r, c))
        
        for r_dir, c_dir in DIRS:
            next_r = r+r_dir
            next_c = c+c_dir
            if 0 <= next_r < n and 0 <= next_c < m and board[next_r][next_c] == EMPTY:
                queue.append((next_r, next_c))
                
    group_count_dict[group] = count

n, m = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(n)]
result = [[EMPTY for __ in range(m)] for _ in range(n)]
wall_set = set()
next_group = 0
loc_group_dict = {}
group_count_dict = {}
for r in range(n):
    for c in range(m):
        if board[r][c] == WALL:
            wall_set.add((r, c))
        elif (r, c) not in loc_group_dict:
            find_empty_group(r, c)

for r, c in wall_set:
    connected_group_set = set()
    count = 1
    for r_dir, c_dir in DIRS:
        next_r = r+r_dir
        next_c = c+c_dir
        if 0 <= next_r < n and 0 <= next_c < m and board[next_r][next_c] == EMPTY:
            group = loc_group_dict[(next_r, next_c)]
            if group in connected_group_set:
                continue
            count += group_count_dict[group]
            connected_group_set.add(group)
    result[r][c] = str(count%10)
    
for row in result:
    print(''.join(row))