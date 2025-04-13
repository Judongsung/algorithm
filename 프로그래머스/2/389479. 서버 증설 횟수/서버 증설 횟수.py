from collections import deque
from math import ceil

REMOVE_TIME = 0
REMOVE_NUM = 1

def solution(players, m, k):
    answer = 0
    current_server = 0
    server_remove_deque = deque()
    
    for time, p_num in enumerate(players):
        if server_remove_deque and server_remove_deque[0][REMOVE_TIME] == time:
            current_server -= server_remove_deque.popleft()[REMOVE_NUM]
        
        required_server = p_num//m
        if current_server < required_server:
            server_add_num = required_server-current_server
            server_add_info = [time+k, server_add_num]
            server_remove_deque.append(server_add_info)
            current_server += server_add_num
            answer += server_add_num
    
    return answer