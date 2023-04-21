from collections import deque

dia_pick = {'diamond':1, 'iron':1, 'stone':1}
iron_pick = {'diamond':5, 'iron':1, 'stone':1}
stone_pick = {'diamond':25, 'iron':5, 'stone':1}
mine_dict = [dia_pick, iron_pick, stone_pick]

def split_list(before, unit):
    div, mod = divmod(len(before), unit)
    return [before[i*unit:(i+1)*unit] for i in range(div)]+[before[div*unit:div*unit+mod]]

def solution(picks, minerals):
    min_fatigue = 10**6
    mineral_split = split_list(minerals, 5)
    mineral_len = len(mineral_split)
    picks_tuple = tuple(picks)
    queue = deque([[(0, 0, 0), 0, 0]])
    
    while queue:
        used_picks, mineral_idx, fatigue = queue.popleft()
        if fatigue > min_fatigue:
            continue
        if used_picks == picks_tuple or mineral_idx == mineral_len:
            min_fatigue = min(fatigue, min_fatigue)
            continue
        
        for cur_pick in range(3):
            if used_picks[cur_pick] < picks[cur_pick]:
                cur_fatigue = 0
                for cur_mineral in mineral_split[mineral_idx]:
                    cur_fatigue += mine_dict[cur_pick][cur_mineral]
                
                
                used_picks_after = list(used_picks)
                used_picks_after[cur_pick] += 1
                queue.append([tuple(used_picks_after), mineral_idx+1, fatigue+cur_fatigue])
                
    return min_fatigue