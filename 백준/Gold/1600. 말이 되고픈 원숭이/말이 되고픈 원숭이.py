from sys import stdin
from collections import deque

EMPTY = '0'
HURDLE = '1'
ORDINARY_DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
HORSE_DIRS = [(-2, -1), (-1, -2), (2, -1), (1, -2), (-2, 1), (-1, 2), (2, 1), (1, 2)]

def find_next_locs(r, c, remain_horse, dirs):
    result = []
    for r_dir, c_dir in dirs:
        next_r = r+r_dir
        next_c = c+c_dir
        if 0 <= next_r < rlen and 0 <= next_c < clen and board[next_r][next_c] == EMPTY and remain_horse > visited[next_r][next_c]:
            result.append((next_r, next_c, remain_horse))
    return result

k = int(stdin.readline())
clen, rlen = map(int, stdin.readline().split())
visited = [[-1 for __ in range(clen)] for _ in range(rlen)]
board = [stdin.readline().split() for _ in range(rlen)]
goal_r = rlen-1
goal_c = clen-1
next_queue = deque([(0, 0, k)])
count = 0
flag = True
result = -1

while flag and next_queue:
    queue = next_queue
    next_queue = deque()
    
    while queue:
        r, c, remain_horse = queue.popleft()
        if r == goal_r and c == goal_c:
            flag = False
            break
        elif visited[r][c] >= remain_horse:
            continue
        visited[r][c] = remain_horse
        
        if remain_horse:
            next_queue += find_next_locs(r, c, remain_horse-1, HORSE_DIRS)
        next_queue += find_next_locs(r, c, remain_horse, ORDINARY_DIRS)
        
    else:
        count += 1
else:
    if not flag:
        result = count
        
print(result)