from sys import stdin
from collections import deque

WALL = '*'
EMPTY = '.'
DOOR = '#'
MIRROR = '!'
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def find_min_mirror(start):
    visited = set()
    min_count = 0
    queue = deque([(start, None, 0)])
    flag = True
    
    while flag and queue:
        loc, prev_dir, count = queue.popleft()
        if loc in visited:
            continue
        visited.add(loc)
        r, c = loc

        for i, direction in enumerate(dirs):
            r_dir, c_dir = direction
            next_r = r+r_dir
            next_c = c+c_dir
            
            while 0 <= next_r < n and 0 <= next_c < n:
                if board[next_r][next_c] == MIRROR:
                    queue.append(((next_r, next_c), i%2, count+1))
                elif board[next_r][next_c] == WALL:
                    break
                elif (next_r, next_c) == goal:
                    min_count = count
                    flag = False
                    break
                
                next_r += r_dir
                next_c += c_dir
                
    return min_count

n = int(stdin.readline())
board = [None for _ in range(n)]
doors = []
for r in range(n):
    line = list(stdin.readline().rstrip())
    if len(doors) < 2:
        for c in range(n):
            if line[c] == DOOR:
                doors.append((r, c))
    board[r] = line

start = doors[0]
goal = doors[1]
result = find_min_mirror(start)
print(result)