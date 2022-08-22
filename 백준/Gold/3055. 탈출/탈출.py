from sys import stdin
from collections import deque

SONIC = 'S'
CAVE = 'D'
EMPTY = '.'
WATER = '*'
ROCK = 'X'
TIME = 2
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def get_min_run():
    result = -1
    sr, sc = sonic_loc
    queue = deque([(sr, sc, 0)])
    goal = cave_loc
    visited = [[False for _ in row] for row in board]
    visited[sr][sc] = True
    
    while queue:
        r, c, t = queue.popleft()
        if (r, c) == goal:
            result = t
            break
        if board[r][c] == ROCK:
            continue
        
        for r_dir, c_dir in dirs:
            next_r = r+r_dir
            next_c = c+c_dir

            if 0 <= next_r < row and 0 <= next_c < col and is_passable_loc(next_r, next_c, t) and not visited[next_r][next_c]:
                queue.append((next_r, next_c, t+1))
                visited[next_r][next_c] = True
    else:
        result = 'KAKTUS'
        
    return result

def is_passable_loc(r, c, time):
    water_time = water_time_board[r][c]
    return water_time == -1 or time+1 < water_time

row, col = map(int, stdin.readline().split())
board = []
sonic_loc = None
cave_loc = None
water_queue = deque()
water_time_board = [[-1 for __ in range(col)] for _ in range(row)]
for i in range(row):
    line = list(stdin.readline().rstrip())
    for j, el in enumerate(line):
        if not sonic_loc and el == SONIC:
            sonic_loc = (i, j)
        if not cave_loc and el == CAVE:
            cave_loc = (i, j)
        if el == WATER:
            water_queue.append((i, j, 0))
            water_time_board[i][j] = 0
    board.append(line)

time = 0
while water_queue:
    r, c, t = water_queue.popleft()

    for r_dir, c_dir in dirs:
        next_r = r+r_dir
        next_c = c+c_dir

        if 0 <= next_r < row and 0 <= next_c < col and board[next_r][next_c] not in [ROCK, CAVE]\
                and water_time_board[next_r][next_c] == -1:
            water_time_board[next_r][next_c] = t+1
            water_queue.append((next_r, next_c, t+1))
                
min_run = get_min_run()
print(min_run)