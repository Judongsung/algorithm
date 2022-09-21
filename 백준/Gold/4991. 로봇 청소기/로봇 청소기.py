from sys import stdin
from collections import deque

INF = 10**9
CLEAN = '.'
DIRTY = '*'
STUFF = 'x'
ROBOT = 'o'
DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def find_min_move(cur, comb):
    if comb not in memo[cur]:
        min_distance = INF
        
        for i in range(node_num):
            if i != cur and comb[i] == '1':
                temp = comb[:i]+'0'+comb[i+1:]
                min_distance = min(min_distance, graph[i][cur]+find_min_move(i, temp))
    
        memo[cur][comb] = min_distance
    return memo[cur][comb]

while True:
    clen, rlen = map(int, stdin.readline().split())
    if clen == rlen == 0:
        break
        
    start = None
    dirty_list = []
    total_move = INF
    board = [None for _ in range(rlen)]
    for r in range(rlen):
        row = list(stdin.readline().rstrip())
        for c in range(clen):
            if row[c] == DIRTY:
                dirty_list.append((r, c))
            elif row[c] == ROBOT:
                start = (r, c)
        
        board[r] = row
        
    nodes = [start]+dirty_list
    graph = [[INF for __ in nodes] for _ in nodes]
    node_num = len(nodes)
    for i in range(len(nodes)):
        graph[i][i] = 0
    for i, one in enumerate(nodes[:-1]):
        others = nodes[i+1:]
        remains = len(others)
        queue = deque([(one, 0)])
        visited = [[False for __ in range(clen)] for _ in range(rlen)]
        while queue:
            loc, distance = queue.popleft()
            r, c = loc
            if visited[r][c]:
                continue
            visited[r][c] = True

            if loc in others:
                j = nodes.index(loc)
                graph[i][j] = distance
                graph[j][i] = distance
                remains -= 1
                if not remains:
                    break

            for r_dir, c_dir in DIRS:
                next_r = r+r_dir
                next_c = c+c_dir
                if 0 <= next_r < rlen and 0 <= next_c < clen and board[next_r][next_c] != STUFF:
                    queue.append(((next_r, next_c), distance+1))
        if remains:
            total_move = -1
            break
    
    if total_move != -1:
        memo = [{'0'*node_num:0} for _ in nodes]
        for i in range(1, node_num):
            temp = ['1']*node_num
            temp[0] = '0'
            temp[i] = '0'
            comb = ''.join(temp)
            total_move = min(total_move, graph[0][i]+find_min_move(i, comb))
    
    print(total_move)