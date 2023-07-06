from math import sqrt, floor

def solution(k, d):
    answer = 0
    
    for x in range(0, d+1, k):
        max_y = floor(sqrt(pow(d, 2)-pow(x, 2)))
        answer += max_y//k+1
        
    return answer