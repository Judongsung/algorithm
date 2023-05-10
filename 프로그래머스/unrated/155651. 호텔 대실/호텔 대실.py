from collections import defaultdict

def time_to_num(time):
    hours = int(time[:2])
    minutes = int(time[3:])
    return hours*60+minutes

def solution(book_time):
    answer = 0
    sequence_dict = defaultdict(int)
    for in_time, out_time in book_time:
        sequence_dict[time_to_num(in_time)] += 1
        sequence_dict[time_to_num(out_time)+10] -= 1
        
    cur = 0
    
    for time in sorted(sequence_dict):
        cur += sequence_dict[time]
        answer = max(answer, cur)
    
    return answer