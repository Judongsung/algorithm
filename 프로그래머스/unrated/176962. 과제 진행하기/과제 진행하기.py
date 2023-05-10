from collections import deque

def time_to_num(time):
    hour = int(time[:2])
    minute = int(time[3:])
    return hour*60+minute

def solution(plans):
    answer = []
    sorted_plan = []
    for subject, start, playtime in plans:
        sorted_plan.append([subject, time_to_num(start), int(playtime)])
    sorted_plan.sort(key=lambda x:x[1])
    plan_queue = deque(sorted_plan)
    incomplete_stack = deque() # [subject, remain_time]
    
    while plan_queue:
        subject, start, playtime = plan_queue.popleft()
        if plan_queue:
            next_start = plan_queue[0][1]
            time_margin = next_start-(start+playtime)
            if time_margin < 0:
                incomplete_stack.append([subject, -time_margin])
            else:
                answer.append(subject)
                
                if incomplete_stack:
                    while incomplete_stack and time_margin >= incomplete_stack[-1][1]:
                        last_incomplete = incomplete_stack.pop()
                        time_margin -= last_incomplete[1]
                        answer.append(last_incomplete[0])
                    else:
                        if incomplete_stack:
                            incomplete_stack[-1][1] -= time_margin
        else:
            answer.append(subject)
            while incomplete_stack:
                last_incomplete = incomplete_stack.pop()[0]
                answer.append(last_incomplete)
            
    return answer