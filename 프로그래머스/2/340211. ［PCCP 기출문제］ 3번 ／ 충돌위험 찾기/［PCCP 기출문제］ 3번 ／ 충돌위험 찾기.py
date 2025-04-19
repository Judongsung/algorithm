from collections import deque, Counter

def solution(points, routes):
    warning_count = 0
    robot_points = dict()
    robot_goal_points = deque()
    
    for i, route in enumerate(routes):
        start = tuple(points[route[0]-1])
        robot_points[i] = start
        goal_points = deque()
        
        for route_num in route[1:]:
            goal_points.append(points[route_num-1])
        robot_goal_points.append([i, goal_points])
    
    while robot_goal_points:
        temp = deque()
        point_counter = Counter(robot_points.values())
        
        for _, count in point_counter.most_common():
            if count > 1:
                warning_count += 1
            else:
                break
        
        while robot_goal_points:
            rnum, goal_points = robot_goal_points.popleft()
            if not goal_points:
                del robot_points[rnum]
                continue
            cur_goal = goal_points.popleft()
            cur_robot_point = list(robot_points[rnum])
            
            if cur_robot_point[0] < cur_goal[0]:
                cur_robot_point[0] += 1
                robot_points[rnum] = tuple(cur_robot_point)
            elif cur_robot_point[0] > cur_goal[0]:
                cur_robot_point[0] -= 1
                robot_points[rnum] = tuple(cur_robot_point)
            elif cur_robot_point[1] < cur_goal[1]:
                cur_robot_point[1] += 1
                robot_points[rnum] = tuple(cur_robot_point)
            elif cur_robot_point[1] > cur_goal[1]:
                cur_robot_point[1] -= 1
                robot_points[rnum] = tuple(cur_robot_point)
            
            if cur_robot_point[0] != cur_goal[0] or \
                    cur_robot_point[1] != cur_goal[1]:
                goal_points.appendleft(cur_goal)
            
            temp.append([rnum, goal_points])
            
        robot_goal_points = temp
    
    return warning_count