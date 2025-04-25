def solution(m, n, start_x, start_y, balls):
    answer = []
    
    start_in_mirror = [[(-start_x, start_y), lambda x1,y1,x2,y2:(y1==y2 and x1>x2)],
                       [(m*2-start_x, start_y), lambda x1,y1,x2,y2:(y1==y2 and x1<x2)], 
                       [(start_x, -start_y), lambda x1,y1,x2,y2:(x1==x2 and y1>y2)], 
                       [(start_x, n*2-start_y), lambda x1,y1,x2,y2:(x1==x2 and y1<y2)], 
                       [(-start_x, -start_y), lambda x1,y1,x2,y2:(x1/y1==x2/y2 and x1>x2)], 
                       [(m*2-start_x, n*2-start_y), lambda x1,y1,x2,y2:(x1/y1==x2/y2 and x1<x2)], 
                       [(m*2-start_x, -start_y), lambda x1,y1,x2,y2:(-x1)/y1==(-x2)/y2 and x1>x2], 
                       [(-start_x, n*2-start_y), lambda x1,y1,x2,y2:(-x1)/y1==(-x2)/y2 and x1<x2]]
    
    for ball_x, ball_y in balls:
        min_dist_pow = 4000000
        
        for (mirror_x, mirror_y), crash_check in start_in_mirror:
            if crash_check(start_x, start_y, ball_x, ball_y):
                continue
                
            dist_pow = pow(ball_x-mirror_x, 2)+pow(ball_y-mirror_y, 2)
            min_dist_pow = min(dist_pow, min_dist_pow)
            
        answer.append(min_dist_pow)
    
    return answer