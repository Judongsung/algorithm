from sys import stdin
from collections import deque

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
EMPTY = 0
WALL = 1
VIRUS = 2

def check_safe_area_size(one, two, three):
    spread_num = -len(virus_loc_set)
    visited = [[False for __ in range(m)] for _ in range(n)]
    visited[one[0]][one[1]] = True
    visited[two[0]][two[1]] = True
    visited[three[0]][three[1]] = True
    
    queue = deque(virus_loc_set)
    
    while queue:
        r, c = queue.pop()
        if visited[r][c]:
            continue
        visited[r][c] = True
        spread_num += 1
        
        for r_dir, c_dir in dirs:
            near_r = r+r_dir
            near_c = c+c_dir
            if 0 <= near_r < n and 0 <= near_c < m and board[near_r][near_c] == EMPTY:
                queue.append((near_r, near_c))
    
    return empty_loc_num-spread_num-3

n, m = map(int, stdin.readline().split())
board = [None for _ in range(n)]
max_safe_area_size = 0
virus_loc_set = set()
empty_loc_set = set()
empty_loc_num = 0

for r in range(n):
    line = list(map(int, stdin.readline().split()))
    
    for c in range(m):
        if line[c] == VIRUS:
            virus_loc_set.add((r, c))
        elif line[c] == EMPTY:
            empty_loc_set.add((r, c))
            
    board[r] = line

empty_loc_list = list(empty_loc_set)
empty_loc_num = len(empty_loc_set)

for i, one in enumerate(empty_loc_list):
    for j, two in enumerate(empty_loc_list[i+1:]):
        for k, three in enumerate(empty_loc_list[i+j+2:]):
            safe_area_size = check_safe_area_size(one, two, three)
            max_safe_area_size = max(max_safe_area_size, safe_area_size)

print(max_safe_area_size)