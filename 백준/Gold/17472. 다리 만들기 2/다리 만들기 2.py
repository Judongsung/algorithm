from sys import stdin
from collections import deque

SEA = 0
LAND = 1
    
def disjoint_set(length):
    return [i for i in range(length)]
    
def union(arr, one, other):
    one_parent = find(arr, one)
    other_parent = find(arr, other)
    if one_parent > other_parent:
        one_parent, other_parent = other_parent, one_parent
    arr[other_parent] = arr[one_parent]

def find(arr, num):
    if arr[num] != num:
        parent = find(arr, arr[num])
        arr[num] = parent
    return arr[num]
    
def is_unique_set(arr):
    for i in range(len(arr)):
        if find(arr, i) != 0:
            return False
    return True
    
def get_next_target_idx(arr, cur_idx, target):
    arrlen = len(arr)
    idx = cur_idx
    while idx < arrlen and arr[idx] != target:
        idx += 1
    return idx
            
def find_min_row_bridges(board, is_converted=False):
    if is_converted:
        rows, cols = m, n
    else:
        rows, cols = n, m
    for r in range(rows):
        c = 0
        while c < cols:
            c = get_next_target_idx(board[r], c, LAND)
            if c == cols:
                break
            inum = get_island_num(r, c, is_converted)
            
            c = get_next_target_idx(board[r], c, SEA)
            if c == cols:
                break
            distance = 0
            next_c = get_next_target_idx(board[r], c, LAND)
            distance = next_c-c
            c = next_c
            if c == cols:
                break

            if distance < 2:
                continue

            next_inum = get_island_num(r, c, is_converted)
            if next_inum != inum:
                inum_pair = get_pair_tuple(inum, next_inum)
                if inum_pair not in bridge_distance_map or bridge_distance_map[inum_pair] > distance:
                    bridge_distance_map[inum_pair] = distance

def get_pair_tuple(one, other):
    return tuple(sorted([one, other]))

def get_island_num(r, c, is_converted=False):
    if is_converted:
        r, c = c, r
    for num, island in enumerate(island_list):
        if (r, c) in island:
            return num
        
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    island = set()
    visited = [[False for e in row] for row in board]
    queue = deque([(r, c)])
    visited[r][c] = True
    
    while queue:
        cur_r, cur_c = queue.pop()
        island.add((cur_r, cur_c))
        
        for r_dir, c_dir in dirs:
            next_r = cur_r+r_dir
            next_c = cur_c+c_dir
            if 0 <= next_r < n and 0 <= next_c < m and board[next_r][next_c] == LAND and not visited[next_r][next_c]:
                queue.append((next_r, next_c))
                visited[next_r][next_c] = True
                
    island_list.append(island)
    return len(island_list)-1

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
island_list = []
bridge_distance_map = {}
is_converted = False

find_min_row_bridges(board)

converted_board = [[board[j][i] for j in range(n)] for i in range(m)]
is_converted = True
find_min_row_bridges(converted_board, True)

selected = set()
distances = sorted(bridge_distance_map.items(), key=lambda x:x[1])
ds = disjoint_set(len(island_list))
result = 0
for inum_pair, distance in distances:
    inum_one, inum_other = inum_pair
    if find(ds, inum_one) == find(ds, inum_other):
        continue
    result += distance
    selected.add(inum_one)
    selected.add(inum_other)
    union(ds, inum_one, inum_other)
    
if len(selected) < len(island_list) or not is_unique_set(ds):
    result = -1
print(result)