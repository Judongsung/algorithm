from collections import deque
from sys import stdin


def find_min_time(start: int, target: int) -> int:
    max_pos = 10**5
    min_times = [float('inf') for _ in range(max_pos+1)]
    routes = [[lambda x:x*2, 0], [lambda x:x-1, 1], [lambda x:x+1, 1]] # [다음 이동 위치 함수, 소요시간]
    queue = deque()
    queue.append((start, 0)) # (현재 위치, 시간)
    min_times[start] = 0

    def validate(next_pos: int, next_time: int) -> bool:
        return 0 <= next_pos <= max_pos and next_time < min_times[next_pos]
    
    def add_queue(next_pos, next_time, to_left=False):
        min_times[next_pos] = next_time
        if to_left:
            queue.appendleft((next_pos, next_time))
            return
        queue.append((next_pos, next_time))
        return
    
    while queue:
        pos, time = queue.popleft()

        for move, move_time in routes:
            next_pos = move(pos)
            next_time = time+move_time
            if validate(next_pos, next_time):
                add_queue(next_pos, next_time, move_time == 0)
                
    return min_times[target]
                
n, k = map(int, stdin.readline().rstrip().split())
result = find_min_time(n, k)
print(result)