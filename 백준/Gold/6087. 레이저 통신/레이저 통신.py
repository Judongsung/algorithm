from sys import stdin
from heapq import heappop
from heapq import heappush

EMPTY = '.'
WALL = '*'
TARGET = 'C'
INF = 10**5
DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

clen, rlen = map(int, stdin.readline().split())
board = []
targets = []
for r in range(rlen):
    line = stdin.readline().rstrip()
    if len(targets) < 2:
        for c in range(clen):
            if line[c] == TARGET:
                targets.append((r, c))
    board.append(line)

start_r, start_c = targets[0]
goal = targets[1]
queue = []
for next_dir, dir_info in enumerate(DIRS):
    next_r = start_r+dir_info[0]
    next_c = start_c+dir_info[1]
    if 0 <= next_r < rlen and 0 <= next_c < clen and board[next_r][next_c] != WALL:
        queue.append((0, next_r, next_c, next_dir))
visited = [[[INF for ___ in DIRS] for __ in range(clen)] for _ in range(rlen)]
visited[start_r][start_c] = [0 for _ in DIRS]

while queue:
    turn_count, r, c, cur_dir = heappop(queue)
    if (r, c) == goal:
        result = turn_count
        break
    elif turn_count >= visited[r][c][cur_dir]:
        continue
    visited[r][c][cur_dir] = turn_count

    for next_dir, dir_info in enumerate(DIRS):
        next_r = r+dir_info[0]
        next_c = c+dir_info[1]
        if 0 <= next_r < rlen and 0 <= next_c < clen and board[next_r][next_c] != WALL:
            next_turn_count = turn_count
            if next_dir != cur_dir:
                next_turn_count += 1
            heappush(queue, (next_turn_count, next_r, next_c, next_dir))
        
print(result)