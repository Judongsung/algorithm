def get_score():
    pass
    return memo


def solution(A, B):
    answer = 0
    sorted_a = sorted(A)
    sorted_b = sorted(B)
    pa = 0
    pb = 0
    
    while pa < len(sorted_b) and pb < len(sorted_b):
        if sorted_a[pa] >= sorted_b[pb]:
            pb += 1
        
        if pb < len(sorted_b) and sorted_a[pa] < sorted_b[pb]:
            answer += 1
            pa += 1
            pb += 1
    
    
    
    return answer