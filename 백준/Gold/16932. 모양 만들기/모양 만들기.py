from sys import stdin
from collections import deque

EMPTY = '0'
FILLED = '1'
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def get_shape_num(r, c):
    if (r, c) not in shape_num_dict:
        add_shape_set(r, c)
    return shape_num_dict[(r, c)]

def add_shape_set(r, c):
    shape_set = find_shape_set(r, c)
    shape_sets.append(shape_set)
    return

def find_shape_set(r, c):
    num = len(shape_sets)
    shape_set = set()
    queue = deque([(r, c)])
    
    while queue:
        cur_r, cur_c = queue.pop()
        if visited[cur_r][cur_c]:
            continue
        visited[cur_r][cur_c] = True
        shape_set.add((cur_r, cur_c))
        shape_num_dict[(cur_r, cur_c)] = num
        
        for r_dir, c_dir in dirs:
            near_r = cur_r+r_dir
            near_c = cur_c+c_dir
            if 0 <= near_r < n and 0 <= near_c < m and not visited[near_r][near_c] and board[near_r][near_c] == FILLED:
                queue.append((near_r, near_c))
    
    return shape_set

def get_near_loc_set(r, c):
    near_loc_set = set()
    for r_dir, c_dir in dirs:
        near_r = r+r_dir
        near_c = c+c_dir
        if 0 <= near_r < n and 0 <= near_c < m:
            near_loc_set.add((near_r, near_c))
    return near_loc_set

n, m = map(int, stdin.readline().split())
board = [stdin.readline().split() for _ in range(n)]
visited = [[False for __ in range(m)] for _ in range(n)]
shape_sets = []
shape_num_dict = {}
max_size = 0

for r in range(n):
    for c in range(m):
        if board[r][c] == EMPTY:
            size = 1
            loc_set = get_near_loc_set(r, c)
            near_num_set = set()
            
            for near_r, near_c in loc_set:
                if board[near_r][near_c] == FILLED:
                    shape_num = get_shape_num(near_r, near_c)
                    if shape_num not in near_num_set:
                        near_num_set.add(shape_num)
                        size += len(shape_sets[shape_num])
            
            max_size = max(max_size, size)
            visited[r][c] = True

print(max_size)