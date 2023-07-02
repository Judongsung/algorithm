from math import ceil, floor, sqrt

def solution(r1, r2):
    count = 0
    inline = pow(r1, 2)
    outline = pow(r2, 2)
    
    for x in range(1, r2+1):
        pow_x = pow(x, 2)
        max_y = floor(sqrt(outline-pow_x))
        min_y = ceil(sqrt(inline-pow_x)) if r1 > x else 0
        
        count += max_y-min_y+1
        
    return count*4