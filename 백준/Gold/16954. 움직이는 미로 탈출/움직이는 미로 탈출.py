from sys import stdin
from collections import deque

SIZE = 8
EMPTY = '.'
WALL = '#'
DIRS = [(r, c) for c in range(-1, 2) for r in range(-1, 2)]

board = [stdin.readline().rstrip() for _ in range(SIZE)]
empty_line = [EMPTY for _ in range(SIZE)]
next_queue = set([(SIZE-1, 0)])
goal = (0, SIZE-1)
result = 0
flag = True

while flag and next_queue:
    queue = deque(next_queue)
    next_queue = set()
    
    while queue:
        r, c = queue.popleft()
        if board[r][c] == WALL:
            continue
        elif (r, c) == goal:
            result = 1
            flag = False
            break
        
        for r_dir, c_dir in DIRS:
            next_r = r+r_dir
            next_c = c+c_dir
            if 0 <= next_r < SIZE and 0 <= next_c < SIZE and board[next_r][next_c] == EMPTY:
                next_queue.add((next_r, next_c))
    
    board = [empty_line]+board[:-1]
    
print(result)