from collections import deque

EMPTY = 0
OIL = 1

def get_oil_set_and_col_set(land, land_checked, r, c, rlen, clen):
    oil_set = set()
    col_set = set()
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    queue = deque()
    queue.append((r, c))
    land_checked[r][c] = True
    
    while queue:
        cur_r, cur_c = queue.pop()
        oil_set.add((cur_r, cur_c))
        col_set.add((cur_c))
        
        for r_dir, c_dir in dirs:
            next_r = cur_r+r_dir
            next_c = cur_c+c_dir
            if 0 <= next_r < rlen and 0 <= next_c < clen and land[next_r][next_c] == OIL and not land_checked[next_r][next_c]:
                land_checked[next_r][next_c] = True
                queue.append((next_r, next_c))
                
    return oil_set, col_set
    

def solution(land):
    land_checked = [[False for el in row] for row in land]
    rlen = len(land)
    clen = len(land[0])
    col_amount = [0 for _ in range(clen)]
    
    for i, row in enumerate(land):
        for j, el in enumerate(row):
            if el == OIL and not land_checked[i][j]:
                oil_set, col_set = get_oil_set_and_col_set(land, land_checked, i, j, rlen, clen)
                
                for c in list(col_set):
                    col_amount[c] += len(oil_set)
                    
    return max(col_amount)