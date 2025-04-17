def solution(routes):
    camera = 0
    last_start = -30001
    last_end = -30001
    routes.sort(key=lambda x:x[0])
    
    for start, end in routes:
        if start <= last_end:
            last_start = start
            if end <= last_end:
                last_end = end
        else:
            camera += 1
            last_start = start
            last_end = end
    
    return camera