from collections import deque

WATER = 'X'
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = set()
rlen = 0
clen = 0

def find_food(board, c, r):
    food = 0
    queue = deque([(c, r)])
    
    while queue:
        cur_c, cur_r = queue.pop()
        if (cur_c, cur_r) in visited:
            continue
        visited.add((cur_c, cur_r))
        food += int(board[cur_c][cur_r])
        
        for c_dir, r_dir in dirs:
            next_c = cur_c+c_dir
            next_r = cur_r+r_dir
            if 0 <= next_c < clen and 0 <= next_r < rlen and board[next_c][next_r] != WATER:
                queue.append((next_c, next_r))
        
    return food

def solution(maps):
    global clen, rlen
    answer = []
    clen = len(maps)
    rlen = len(maps[0])
    
    for c, row in enumerate(maps):
        for r, el in enumerate(row):
            if el != WATER and (c, r) not in visited:
                food = find_food(maps, c, r)
                answer.append(food)
    
    if not visited:
        answer = [-1]
    else:
        answer.sort()
    return answer