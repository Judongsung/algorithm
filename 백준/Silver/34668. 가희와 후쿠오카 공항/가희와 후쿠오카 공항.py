from sys import stdin


START_TIME = 360
BOARDING_LIMIT = 50
MOVE_TIME = 4
STOP_TIME = 2
IMPOSSIBLE = "-1"

def get_boarding_delay(order : int) -> int:
    rotation = order//BOARDING_LIMIT
    return (MOVE_TIME+STOP_TIME) * (rotation*2+1)

def num_to_time(num: int) -> str:
    hour, minute = divmod(num, 60)
    if hour >= 24 and minute > MOVE_TIME+STOP_TIME:
        return IMPOSSIBLE
    return f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"
    

q = int(stdin.readline())
for _ in range(q):
    order = int(stdin.readline())
    delay = get_boarding_delay(order) + START_TIME
    print(num_to_time(delay))