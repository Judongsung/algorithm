def time_to_minutes(time):
    return (time//100)*60+time%100

def solution(schedules, timelogs, startday):
    answer = 0
    
    for schedule, log in zip(schedules, timelogs):
        limit = time_to_minutes(schedule)+10
        saturday = (6-startday)%7
        log = [log[i] for i in range(7) if not (saturday == i or (saturday+1)%7 == i)]
        eventlog = sorted(log, reverse=True)
        if time_to_minutes(eventlog[0]) <= limit:
            answer += 1
        
    return answer