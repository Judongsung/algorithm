from sys import stdin
from collections import deque

LAND = '1'
SEA = '0'
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def round_queue(queue, parameters):
    land_func = parameters['land_func']
    sea_func = parameters['sea_func']
    visited = parameters['visited']
    for el in queue:
        r, c = el[:2]
        visited[r][c] = True
    
    flag = True
    while flag and queue:
        cur_data = queue.popleft()
        r, c = cur_data[:2]
        parameters['cur_data'] = cur_data
        
        for r_dir, c_dir in dirs:
            near_r = r+r_dir
            near_c = c+c_dir
            
            if 0 <= near_r < n and 0 <= near_c < n and not visited[near_r][near_c]:
                parameters['near_r'] = near_r
                parameters['near_c'] = near_c
                if board[near_r][near_c] == LAND:
                    flag = land_func(queue, parameters)
                elif board[near_r][near_c] == SEA:
                    flag = sea_func(queue, parameters)
                visited[near_r][near_c] = True
                
            if not flag:
                break
                
    return

def find_land_edge(r, c):
    land_set = set()
    edge_set = set()
    visited = [[False for __ in range(n)] for _ in range(n)]
    visited[r][c] = True
    queue = deque([(r, c)])
    land_set.add((r, c))
    parameters = {'land_func':add_queue_land_set, 'sea_func':add_edge_set, 'land_set':land_set, 'edge_set':edge_set, 'visited':visited}
    round_queue(queue, parameters)
    return land_set, list(edge_set)
                
def add_queue_land_set(queue, parameters):
    near_r = parameters['near_r']
    near_c = parameters['near_c']
    parameters['land_set'].add((near_r, near_c))
    queue.append((near_r, near_c))
    return True
    
def add_edge_set(queue, parameters):
    cur_r, cur_c = parameters['cur_data']
    parameters['edge_set'].add((cur_r, cur_c))
    return True

def find_nearest_land_distance(land_set, edge_set):
    queue = deque()
    visited = [[False for __ in range(n)] for _ in range(n)]
    for r, c in list(land_set):
        visited[r][c] = True
    for r, c in list(edge_set):
        queue.append((r, c, 0))
    parameters = {'land_func':find_nearest_land, 'sea_func':add_nearest_land_distance_queue, 'result':0, 'visited':visited}
    round_queue(queue, parameters)
    return parameters['result']

def add_nearest_land_distance_queue(queue, parameters):
    distance = parameters['cur_data'][2]
    near_r = parameters['near_r']
    near_c = parameters['near_c']
    queue.append((near_r, near_c, distance+1))
    return True

def find_nearest_land(queue, parameters):
    distance = parameters['cur_data'][2]
    parameters['result'] = distance
    return False

n = int(stdin.readline())
board = [stdin.readline().rstrip().split() for _ in range(n)]
total_land_set = set()
shortest_bridge = n*n
for r in range(n):
    for c in range(n):
        if board[r][c] == LAND and (r, c) not in total_land_set:
            land_set, edge_set = find_land_edge(r, c)
            bridge = find_nearest_land_distance(land_set, edge_set)
            total_land_set.update(land_set)
            shortest_bridge = min(bridge, shortest_bridge)

print(shortest_bridge)