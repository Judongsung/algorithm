from sys import stdin
from collections import deque

EMPTY = '0'
WALL = '1'
VIRUS = '2'
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def get_combination(start, end, count, prev=None):
    if count == 0:
        return [prev]
    if prev == None:
        prev = []
        
    result = []
    for num in range(start, end):
        temp = prev.copy()
        temp.append(num)
        result += get_combination(num+1, end, count-1, temp)
    return result

def spread_virus(active_virus):
    result = -1
    remain_empty_loc_num = empty_loc_num
    visited = [[False for __ in range(n)] for _ in range(n)]
    next_queue = deque(active_virus)
    time = -1
    flag = True
    
    while flag and next_queue:
        queue = next_queue
        next_queue = deque()
        time += 1
        while queue:
            r, c = queue.pop()
            if visited[r][c]:
                continue
            visited[r][c] = True
            if board[r][c] == EMPTY:
                remain_empty_loc_num -= 1
                if remain_empty_loc_num == 0:
                    result = time
                    flag = False
                    break
            
            for r_dir, c_dir in dirs:
                next_r = r+r_dir
                next_c = c+c_dir
                if 0 <= next_r < n and 0 <= next_c < n and board[next_r][next_c] != WALL and not visited[next_r][next_c]:
                    next_queue.append((next_r, next_c))
    
    return result

n, m = map(int, stdin.readline().split())
board = [None for _ in range(n)]
min_time = n*n
virus_loc_list = []
empty_loc_num = 0
for r in range(n):
    line = stdin.readline().rstrip().split()
    for c in range(n):
        if line[c] == VIRUS:
            virus_loc_list.append((r, c))
        elif line[c] == EMPTY:
            empty_loc_num += 1
    board[r] = line

if empty_loc_num == 0:
    min_time = 0
else:
    combinations = get_combination(0, len(virus_loc_list), m)
    for combination in combinations:
        active_virus = [virus_loc_list[i] for i in combination]
        time = spread_virus(active_virus)
        if time > 0 and time != min_time:
            min_time = min(time, min_time)

    if min_time == n*n:
        min_time = -1
        
print(min_time)