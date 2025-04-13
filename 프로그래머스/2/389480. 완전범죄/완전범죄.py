index_dict = dict()

def solution(info, n, m, index=0, a_trace=0, b_trace=0):
    if a_trace >= n or b_trace >= m:
        return -1
    elif index == len(info):
        return a_trace
    elif ((a_trace, b_trace) in index_dict\
            and index_dict[(a_trace, b_trace)] >= index):
        return -1
    
    
    
    index_dict[(a_trace, b_trace)] = index
    choose_a = solution(info, n, m, index+1, a_trace+info[index][0], b_trace)
    choose_b = solution(info, n, m, index+1, a_trace, b_trace+info[index][1])
    
    if choose_a != -1 and choose_b != -1:
        return min(choose_a, choose_b)
    elif choose_a == -1:
        return choose_b
    else:
        return choose_a