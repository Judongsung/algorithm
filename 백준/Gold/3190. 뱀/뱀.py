from sys import stdin
from collections import deque

HEAD = 0
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def solution(n, k, apples, l, turn_infos):
    snake = deque()
    snake.append((1, 1))
    direction = RIGHT
    time = 0
    turn_stack = [[int(t), d] for t, d in turn_infos]
    turn_stack.reverse()
    apples_copy = apples.copy()
    
    while True:
        time += 1
        hr, hc = snake[HEAD]
        r_dir, c_dir = direction
        hr += r_dir
        hc += c_dir
        new_head = (hr, hc)
        if not (0 < hr <= n and 0 < hc <= n) or new_head in snake:
            break
        if new_head in apples_copy:
            apples_copy.remove(new_head)
        else:
            snake.pop()
        snake.appendleft(new_head)
        if turn_stack and time == turn_stack[-1][0]:
            direction = turn_direction(direction, turn_stack.pop()[1])
    
    return time

def turn_direction(cur_dir, turn_dir):
    if cur_dir == UP:
        if turn_dir == 'L':
            return LEFT
        else:
            return RIGHT
    elif cur_dir == DOWN:
        if turn_dir == 'L':
            return RIGHT
        else:
            return LEFT
    elif cur_dir == LEFT:
        if turn_dir == 'L':
            return DOWN
        else:
            return UP
    else:
        if turn_dir == 'L':
            return UP
        else:
            return DOWN
        
n = int(stdin.readline())
k = int(stdin.readline())
apples = [tuple(map(int, stdin.readline().split())) for _ in range(k)]
l = int(stdin.readline())
turn_infos = [stdin.readline().split() for _ in range(l)]
result = solution(n, k ,apples, l, turn_infos)
print(result)