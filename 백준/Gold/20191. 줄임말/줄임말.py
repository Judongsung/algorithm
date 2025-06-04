from typing import Dict, List
from sys import stdin


NOT_EXISTS = -1

def create_ch_idx_dict(text:str) -> Dict[str, List[int]]:
    result = {chr(ord('a')+i):[] for i in range(26)}
    for i, ch in enumerate(text):
        result[ch].append(i)
    return result

def find_next_idx(idxlist:List[int], prev_idx:int) -> int:
    left = 0
    right = len(idxlist)-1
    answer = NOT_EXISTS

    while left <= right:
        mid = (left+right)//2
        cur = idxlist[mid]
        if cur > prev_idx:
            answer = cur
            right = mid-1
        else:
            left = mid+1
    
    return answer

def find_min_repeat(sentence:str, repeat_text:str) -> int:
    repeat = 1
    ch_idx_dict = create_ch_idx_dict(repeat_text)
    prev_idx = -1
    
    for ch in sentence:
        if not ch_idx_dict[ch]:
            return NOT_EXISTS
            
        next_idx = find_next_idx(ch_idx_dict[ch], prev_idx)
        if next_idx == NOT_EXISTS:
            repeat += 1
            prev_idx = ch_idx_dict[ch][0]
        else:
            prev_idx = next_idx

    return repeat

sentence = stdin.readline().rstrip()
repeat_text = stdin.readline().rstrip()
result = find_min_repeat(sentence, repeat_text)
print(result)