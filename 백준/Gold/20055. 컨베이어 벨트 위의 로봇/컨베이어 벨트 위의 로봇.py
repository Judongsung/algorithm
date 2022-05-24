def down_robot(robot_locations, down_idx):
    result = False
    
    if robot_locations and robot_locations[0] == down_idx:
        robot_locations.pop(0)
        result = True
        
    return result

def get_idx(num, belt_len):
    return (num+belt_len) % belt_len
        
def solution(n, k, alist):
    step = 0
    belt_len = n*2
    up_idx = 0
    down_idx = n-1
    zero_count = alist.count(0)
    robot_locations = []
    
    while True:
        step += 1
        up_idx = get_idx(up_idx-1, belt_len)
        down_idx = get_idx(down_idx-1, belt_len)
        down_robot(robot_locations, down_idx)
        
        cur = 0
        while cur < len(robot_locations):
            cur_robot_loc = robot_locations[cur]
            front_loc = get_idx(cur_robot_loc+1, belt_len)
            if alist[front_loc] > 0 and not (cur > 0 and robot_locations[cur-1] == front_loc):
                robot_locations[cur] = front_loc
                alist[front_loc] -= 1
                if alist[front_loc] == 0:
                    zero_count += 1
                if down_robot(robot_locations, down_idx):
                    continue
            cur += 1
        
        if alist[up_idx] > 0:
            robot_locations.append(up_idx)
            alist[up_idx] -= 1
            if alist[up_idx] == 0:
                zero_count += 1
                
        if zero_count >= k:
            break
    
    return step

n, k = map(int, input().split())
alist = list(map(int, input().split()))
result = solution(n, k, alist)
print(result)