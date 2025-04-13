def solution(diffs, times, limit):
    answer = 0
    min_clear_time = sum(times)
    replay_time = [time+times[i-1] for i, time in enumerate(times)]
    start = 1
    last = max(diffs)
    
    cur_level = (start+last)//2
    while start <= last:
        cur_level = (start+last)//2
        clear_time = min_clear_time
        for i, diff in enumerate(diffs):
            if cur_level <= diff:
                clear_time += (diff-cur_level)*replay_time[i]
            if clear_time > limit:
                break
    
        if clear_time > limit:
            start = cur_level+1
        elif clear_time <= limit:
            last = cur_level-1
    
    answer = start
    
    return answer