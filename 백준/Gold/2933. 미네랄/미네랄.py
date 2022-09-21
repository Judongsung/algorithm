from sys import stdin
from collections import deque
from collections import defaultdict

EMPTY = '.'
MINERAL = 'x'
dirs = [(1, 0), (0, -1), (0, 1), (-1, 0)]

def throw(r, direction):
    if direction == 0:
        c_range = range(clen)
    else:
        c_range = range(clen-1, -1, -1)
    
    for c in c_range:
        if board[r][c] == MINERAL:
            pop(r, c)
            break
    
    return

def pop(r, c):
    board[r][c] = EMPTY
    total_cluster = set()
    cluster_list = []
    
    for r_dir, c_dir in dirs:
        near_r = r+r_dir
        near_c = c+c_dir
        if 0 <= near_r < rlen and 0 <= near_c < clen and board[near_r][near_c] == MINERAL and (near_r, near_c) not in total_cluster:
            cluster = find_cluster_set(near_r, near_c)
            if apply_gravity(cluster):
                break
            total_cluster |= cluster
    
    return

def find_cluster_set(start_r, start_c):
    cluster_set = set()
    queue = deque([(start_r, start_c)])
    
    while queue:
        loc = queue.pop()
        if loc in cluster_set:
            continue
        cluster_set.add(loc)
        
        r, c = loc
        for r_dir, c_dir in dirs:
            near_r = r+r_dir
            near_c = c+c_dir
            if 0 <= near_r < rlen and 0 <= near_c < clen and board[near_r][near_c] == MINERAL:
                queue.append((near_r, near_c))
    
    return cluster_set

def apply_gravity(cluster):
    is_applied = False
    bottom_dict = defaultdict(int)
    min_distance = 100
    for r, c in cluster:
        if r > bottom_dict[c]:
            bottom_dict[c] = r
    
    for c in bottom_dict:
        bottom_r = bottom_dict[c]
        distance = 0
        for r in range(bottom_r+1, rlen):
            if board[r][c] == MINERAL:
                break
            distance += 1
        if distance < min_distance:
            min_distance = distance
            
        if min_distance == 0:
            break
    
    if min_distance > 0:
        is_applied = True
        for r, c in sorted(cluster, reverse=True):
            board[r][c] = EMPTY
            board[r+min_distance][c] = MINERAL
    
    return is_applied

rlen, clen = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(rlen)]
n = int(stdin.readline())
throws = list(map(lambda x:rlen-int(x), stdin.readline().split()))
for i in range(n):
    throw(throws[i], i%2)
    
for row in board:
    print(''.join(row))