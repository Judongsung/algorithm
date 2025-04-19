from collections import deque

def solution(gems):
    answer = []
    
    gem_set = set(gems)
    idx_dict = {gem:deque() for gem in gem_set}

    for i, gem in enumerate(gems):
        idx_dict[gem].append(i)
    
    left = 0
    right = 0
    
    for gem in gem_set:
        right = max(right, idx_dict[gem][0])
        
    min_left = 0
    min_right = right
    min_len = right-left+1
        
    while True:
        left_gem = gems[left]
        idx_dict[left_gem].popleft()
        
        if not idx_dict[left_gem]:
            break
        elif idx_dict[left_gem][0] > right:
            right = idx_dict[left_gem][0]
            
        left += 1
        cur_len = right-left+1
        if cur_len < min_len:
            min_len = cur_len
            min_left = left
            min_right = right
            
    return [min_left+1, min_right+1]