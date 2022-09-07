from sys import stdin
from collections import deque

EMPTY = '0'
WALL = '1'
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def find(cur_r, cur_c, cur_oil, check_func, parameters=None):
    result = False
    result_list = []
    queue = deque([(cur_r, cur_c, 0)])
    visited = [[False for __ in range(n)] for _ in range(n)]
    
    while queue:
        r, c, necessary_oil = queue.popleft()
        if visited[r][c] or necessary_oil > cur_oil:
            continue
        visited[r][c] = True
        
        check_result = check_func(r, c, necessary_oil, cur_oil, parameters)
        if check_result['success']:
            result_list.append(check_result)
        if not check_result['flag']:
            break
            
        for r_dir, c_dir in dirs:
            next_r = r+r_dir
            next_c = c+c_dir
            if 0 <= next_r < n and 0 <= next_c < n and board[next_r][next_c] != WALL:
                queue.append((next_r, next_c, necessary_oil+1))
    
    if result_list:
        result_list.sort(key=lambda x:x['loc'])
        result = result_list[0]
    
    return result

def check_client(r, c, used_oil, cur_oil, parameters):
    result_dict = {'success': False, 'flag': True}
    if used_oil > parameters['oil_use_limit']:
        result_dict['flag'] = False
    elif (r, c) in client_map:
        result_dict['success'] = True
        result_dict['client_id'] = client_map[(r, c)]
        result_dict['loc'] = (r, c)
        result_dict['remain_oil'] = cur_oil-used_oil
        parameters['oil_use_limit'] = used_oil
    return result_dict

def check_destination(r, c, used_oil, cur_oil, parameters):
    result_dict = {'success': False, 'flag': True}
    client_id = parameters['client_id']
    if destination_map[client_id] == (r, c):
        result_dict['success'] = True
        result_dict['flag'] = False
        result_dict['loc'] = (r, c)
        result_dict['used_oil'] = used_oil
        result_dict['remain_oil'] = cur_oil-used_oil
    return result_dict

n, m, remain_oil = map(int, stdin.readline().split())
board = [stdin.readline().split() for _ in range(n)]
taxi_r, taxi_c = map(int, stdin.readline().split())
taxi_r -= 1
taxi_c -= 1
client_map = {}
destination_map = [None for _ in range(m)]
for i in range(m):
    client_r, client_c, destination_r, destination_c = map(int, stdin.readline().split())
    client_map[(client_r-1, client_c-1)] = i
    destination_map[i] = (destination_r-1, destination_c-1)

for i in range(m):
    parameters = {'oil_use_limit': remain_oil}
    find_client_result = find(taxi_r, taxi_c, remain_oil, check_client, parameters)
    if not find_client_result:
        result = -1
        break
    
    parameters = {'client_id': find_client_result['client_id']}
    taxi_r, taxi_c = find_client_result['loc']
    remain_oil = find_client_result['remain_oil']
    client_map.pop((taxi_r, taxi_c))
    
    find_destination_result = find(taxi_r, taxi_c, remain_oil, check_destination, parameters)
    if not find_destination_result:
        result = -1
        break
    
    taxi_r, taxi_c = find_destination_result['loc']
    used_oil = find_destination_result['used_oil']
    remain_oil = find_destination_result['remain_oil']+used_oil*2
else:
    result = remain_oil

print(result)