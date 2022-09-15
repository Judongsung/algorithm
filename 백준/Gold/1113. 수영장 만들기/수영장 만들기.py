from sys import stdin
from collections import defaultdict
from collections import deque

dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def bfs(start):
    result = 0
    start_r, start_c = start
    visited = set()
    cur_h = board[start_r][start_c]
    min_near_h = 10
    fillable = True
    queue = deque([start])
    
    while queue:
        loc = queue.popleft()
        r, c = loc
        if loc in visited:
            continue
        visited.add(loc)
        
        if r in r_border or c in c_border:
            fillable = False

        for r_dir, c_dir in dirs:
            near_r = r+r_dir
            near_c = c+c_dir
            if 0 <= near_r < rlen and 0 <= near_c < clen:
                near_h = board[near_r][near_c]
                if near_h == cur_h:
                    queue.append((near_r, near_c))
                elif near_h < cur_h:
                    fillable = False
                elif near_h > cur_h and near_h < min_near_h:
                    min_near_h = near_h

    height_dict[cur_h] -= visited
    if fillable:
        for r, c in visited:
            board[r][c] = min_near_h
        height_dict[min_near_h] |= visited
        result = (min_near_h-cur_h)*len(visited)
    return result

water_amount = 0
rlen, clen = map(int, stdin.readline().split())
board = [None for _ in range(rlen)]
r_border = (0, rlen-1)
c_border = (0, clen-1)
height_dict = defaultdict(set)
for r in range(rlen):
    row = [int(el) for el in stdin.readline().rstrip()]
    for c in range(clen):
        height_dict[row[c]].add((r, c))
    board[r] = row
    
for h in sorted(height_dict):
    while height_dict[h]:
        water_amount += bfs(height_dict[h].pop())
        
print(water_amount)