from sys import stdin

SOM = 'S'
YIM = 'Y'
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def find_sp(r, c):
    result = 0
    s_count = 0
    y_count = 0
    loc_list = []
    
    result = dfs(r, c, loc_list)
    return result

def dfs(r, c, loc_list, s_count=0, y_count=0, prev_group_id=0):
    group_id = get_group_id(r, c, prev_group_id)
    if not (0 <= r < 5 and 0 <= c < 5) or visited[r][c] or group_id in group_id_set:
        return 0
    
    group_id_set.add(group_id)
    if board[r][c] == SOM:
        s_count += 1
    else:
        y_count += 1
    
    if s_count+y_count == 7 and s_count > y_count:
        return 1
    elif y_count >= 4:
        return 0
    
    visited[r][c] = True
    loc_list.append((r, c))
    count = 0
    
    for cur_r, cur_c in loc_list:
        for r_dir, c_dir in dirs:
            near_r = cur_r+r_dir
            near_c = cur_c+c_dir
            count += dfs(near_r, near_c, loc_list, s_count, y_count, group_id)
    
    visited[r][c] = False
    loc_list.pop()
    return count

def get_group_id(r, c, prev_group_id=0):
    return prev_group_id+2**(r*5+c)

board = [list(stdin.readline().rstrip()) for _ in range(5)]
visited = [[False for __ in range(5)] for _ in range(5)]
group_id_set = set()
count = 0

for r in range(5):
    for c in range(5):
        count += find_sp(r, c)

print(count)