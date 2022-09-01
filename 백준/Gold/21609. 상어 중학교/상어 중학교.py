from sys import stdin
from collections import deque

EMPTY = -2
BLACK = -1
RAINBOW = 0
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def check_group(r, c):
    group = set()
    rainbow_blocks = set()
    color = board[r][c]
    queue = deque([(r, c)])
    
    while queue:
        cur_r, cur_c = queue.pop()
        if visited[cur_r][cur_c] or (cur_r, cur_c) in rainbow_blocks:
            continue
            
        group.add((cur_r, cur_c))
        if board[cur_r][cur_c] == RAINBOW:
            rainbow_blocks.add((cur_r, cur_c))
        else:
            visited[cur_r][cur_c] = True
        
        for r_dir, c_dir in dirs:
            near_r = cur_r+r_dir
            near_c = cur_c+c_dir
            if 0 <= near_r < n and 0 <= near_c < n and board[near_r][near_c] in (color, RAINBOW):
                queue.append((near_r, near_c))
    
    if len(group) < 2:
        group = set()
        rainbow_blocks = set()
    return group, len(rainbow_blocks)

def pop_blocks(group):
    for r, c in group:
        board[r][c] = EMPTY

def force_gravity():
    global board
    forced = [row.copy() for row in board]
    
    for c in range(n):
        for r in range(n-1, -1, -1):
            el = forced[r][c]
            if el >= 0:
                for i in range(r, n):
                    if i == n-1 or forced[i+1][c] != EMPTY:
                        break
                forced[r][c] = EMPTY
                forced[i][c] = el
    
    board = forced
    
def rotate():
    global board
    board = [[board[c][r] for c in range(n)] for r in range(n-1, -1, -1)]

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
total_score = 0

while True:
    visited = [[False for __ in range(n)] for _ in range(n)]
    biggest_group_set = set()
    biggest_rainbow_num = 0
    
    for r in range(n):
        for c in range(n):
            if not visited[r][c] and board[r][c] > 0:
                group_set, rainbow_num = check_group(r, c)
                if len(group_set) > len(biggest_group_set) or (len(group_set) == len(biggest_group_set) and rainbow_num >= biggest_rainbow_num):
                    biggest_group_set = group_set
                    biggest_rainbow_num = rainbow_num
    
    if not biggest_group_set:
        break
    
    total_score += len(biggest_group_set)**2
    pop_blocks(biggest_group_set)
    force_gravity()
    rotate()
    force_gravity()
    
print(total_score)