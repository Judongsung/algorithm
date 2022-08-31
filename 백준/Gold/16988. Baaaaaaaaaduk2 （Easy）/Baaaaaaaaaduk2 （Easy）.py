from sys import stdin
from collections import deque

dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
EMPTY = '0'
BLACK = '1'
WHITE = '2'

def find_group(start_r, start_c):
    color = board[start_r][start_c]
    queue = deque([(start_r, start_c)])
    group = []
    near_empty_set = set()
    
    while queue:
        r, c = queue.pop()
        if checked[r][c]:
            continue
        
        checked[r][c] = True
        group.append((r, c))
        
        for r_dir, c_dir in dirs:
            near_r = r+r_dir
            near_c = c+c_dir
            if 0 <= near_r < n and 0 <= near_c < m:
                if board[near_r][near_c] == color:
                    queue.append((near_r, near_c))
                elif board[near_r][near_c] == EMPTY:
                    near_empty_set.add((near_r, near_c))
        
    return group, near_empty_set

n, m = map(int, stdin.readline().split())
board = [stdin.readline().rstrip().split() for _ in range(n)]
checked = [[False for __ in range(m)] for _ in range(n)]
white_groups = []
empty_points_near_white = set()
max_count = 0

for r in range(n):
    for c in range(m):
        if not checked[r][c] and board[r][c] == WHITE:
            group, empty_points = find_group(r, c)
            white_groups.append([group, empty_points])
            empty_points_near_white.update(empty_points)

list_empty_points_near_white = list(empty_points_near_white)
if len(list_empty_points_near_white) == 1:
    empty_point = empty_points_near_white
    for group, empty_points in white_groups:
        if len(empty_points-empty_point) == 0:
            max_count += len(group)
else:
    for i, one in enumerate(list_empty_points_near_white):
        for two in list_empty_points_near_white[i+1:]:
            empty_pair_set = set([one, two])
            count = 0
            for group, empty_points in white_groups:
                if len(empty_points-empty_pair_set) == 0:
                    count += len(group)
            max_count = max(max_count, count)
        
print(max_count)