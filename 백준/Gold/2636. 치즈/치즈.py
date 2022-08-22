from sys import stdin
from collections import deque

EMPTY = '0'
CHEESE = '1'
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def round_queue(queue, parameters=None):
    cheese_func = parameters['cheese_func']
    empty_func = parameters['empty_func']
    while queue:
        r, c = queue.pop()
        
        for r_dir, c_dir in dirs:
            near_r = r+r_dir
            near_c = c+c_dir
            
            if 0 <= near_r < rlen and 0 <= near_c < clen and not visited[near_r][near_c]:
                if board[near_r][near_c] == CHEESE:
                    cheese_func(near_r, near_c, parameters)
                elif board[near_r][near_c] == EMPTY:
                    empty_func(near_r, near_c, parameters)
                visited[near_r][near_c] = True
                
    return

def add_queue(r, c, parameters):
    queue = parameters['queue']
    queue.append((r, c))
    
def add_result(r, c, parameters):
    result = parameters['result']
    result += [(r, c)]
    
def add_queue_wrap_area(r, c, parameters):
    queue = parameters['queue']
    queue += get_wrap_area(r, c)

def get_wrap_area(r, c):
    result = []
    queue = deque([(r, c)])
    visited[r][c] = True
    
    parameters = {'queue':queue, 'result':result, 'cheese_func':add_result, 'empty_func':add_queue}
    round_queue(queue, parameters)
    
    return result

rlen, clen = map(int, stdin.readline().split())
board = [stdin.readline().split() for _ in range(rlen)]
visited = [[False for __ in range(clen)] for _ in range(rlen)]
time = 0
queue = deque()
next_queue = deque()
for r in range(rlen):
    for c in [0, clen-1]:
        if board[r][c] == EMPTY and not visited[r][c]:
            next_queue += get_wrap_area(r, c)
for r in [0, rlen-1]:
    for c in range(1, clen-1):
        if board[r][c] == EMPTY and not visited[r][c]:
            next_queue += get_wrap_area(r, c)

while next_queue:
    queue = next_queue
    next_queue = deque()
    remain_cheese_count = len(queue)
    time += 1
    parameters = {'queue':next_queue, 'cheese_func':add_queue, 'empty_func':add_queue_wrap_area}
    round_queue(queue, parameters)
    
print(time)
print(remain_cheese_count)