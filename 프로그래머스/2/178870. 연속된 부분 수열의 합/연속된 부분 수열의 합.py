def solution(sequence, k):
    answer = []
    min_len = len(sequence)+1
    min_left = 0
    min_right = 0
    left = 0
    right = 0
    part_sum = sequence[0]
    
    while left < len(sequence) and right < len(sequence):
        if part_sum == k:
            cur_len = right-left+1
            if cur_len < min_len:
                min_len = cur_len
                min_left = left
                min_right = right
                
        if part_sum < k:
            right += 1
            if right == len(sequence):
                break
            part_sum += sequence[right]
        else:
            part_sum -= sequence[left]
            left += 1
        
    
    
    return [min_left, min_right]