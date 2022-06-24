from sys import stdin
from collections import deque

EMPTY = '0'
WALL = '1'
RIGHT = 0
DOWN = 1
RIGHT_DOWN = 2

n = int(stdin.readline())
board = [stdin.readline().split() for _ in range(n)]
goal = n-1
count = 0
queue = deque()
queue.append((0, 1, RIGHT))

while queue:
    r, c, d = queue.pop()
    if r == goal and c == goal:
        count += 1
        continue
        
    is_right_empty = c+1 < n and board[r][c+1] == EMPTY
    is_down_empty = r+1 < n and board[r+1][c] == EMPTY
    is_right_down_empty = r+1 < n and c+1 < n and board[r+1][c+1] == EMPTY
    
    if d != DOWN and is_right_empty:
        queue.append((r, c+1, RIGHT))
    if d != RIGHT and is_down_empty:
        queue.append((r+1, c, DOWN))
    if is_right_empty and is_down_empty and is_right_down_empty:
        queue.append((r+1, c+1, RIGHT_DOWN))

print(count)