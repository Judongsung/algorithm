from collections import deque

START = "S"
EXIT = "E"
LEVER = "L"
PATH = "O"
WALL = "X"

def find_min_route(maps, start, goal, rlen, clen):
    queue = deque()
    visited = set()
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    queue.append([start[0], start[1], 0])
    visited.add(start)
    
    while queue:
        r, c, time = queue.popleft()
        time += 1
        
        for r_dir, c_dir in dirs:
            next_r = r+r_dir
            next_c = c+c_dir
            if 0 <= next_r < rlen and 0 <= next_c < clen and maps[next_r][next_c] != WALL and (next_r, next_c) not in visited:
                if (next_r, next_c) == goal:
                    return time
                else:
                    queue.append([next_r, next_c, time])
                    visited.add((next_r, next_c))
    
    return -1
                    

def solution(maps):
    time = 0
    rlen = len(maps)
    clen = len(maps[0])
    start = None
    lever = None
    exit = None
    
    for r, row in enumerate(maps):
        for c, el in enumerate(row):
            if el == START:
                start = (r, c)
            elif el == LEVER:
                lever = (r, c)
            elif el == EXIT:
                exit = (r, c)
                
            if start and lever and exit:
                break
        else:
            continue
        break
        
    time = find_min_route(maps, start, lever, rlen, clen)
    if time < 0:
        return -1
    temp = find_min_route(maps, lever, exit, rlen, clen)
    if temp < 0:
        return -1
    time += temp
    return time