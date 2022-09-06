from sys import stdin
from collections import deque

WALL = '#'
EMPTY = '.'
GOAL = 'O'
RED = 'R'
BLUE = 'B'
SUCCESS = 'S'
FAIL = 'F'
CONTINUE = 'C'
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def move(prev_red_loc, prev_blue_loc, move_dir):
    result_map = {'result': None, 'red_loc': None, 'blue_loc': None}
    
    cur_red_loc = move_ball(prev_red_loc, move_dir)
    cur_blue_loc = move_ball(prev_blue_loc, move_dir)
    
    if cur_blue_loc == goal_loc or (prev_red_loc == cur_red_loc and prev_blue_loc == cur_blue_loc):
        result_map['result'] = FAIL
    elif cur_red_loc == goal_loc:
        result_map['result'] = SUCCESS
    else:
        if cur_red_loc == cur_blue_loc:
            if is_red_back(prev_red_loc, prev_blue_loc, move_dir):
                cur_red_loc = back_ball(cur_red_loc, move_dir)
            else:
                cur_blue_loc = back_ball(cur_blue_loc, move_dir)
        result_map['result'] = CONTINUE
        result_map['red_loc'] = cur_red_loc
        result_map['blue_loc'] = cur_blue_loc
    
    return result_map

def move_ball(ball_loc, move_dir):
    row, col = ball_loc
    r_dir, c_dir = move_dir
    while board[row+r_dir][col+c_dir] != WALL and board[row][col] != GOAL:
        row += r_dir
        col += c_dir
    return (row, col)

def is_red_back(red_loc, blue_loc, move_dir):
    if move_dir in dirs[:2]:
        return red_loc > blue_loc
    else:
        return red_loc < blue_loc

def back_ball(ball_loc, move_dir):
    row, col = ball_loc
    r_dir, c_dir = move_dir
    return (row-r_dir, col-c_dir)

n, m = map(int, stdin.readline().split())
board = [None for _ in range(n)]
red_loc = None
blue_loc = None
goal_loc = None
for row in range(n):
    line = list(stdin.readline().rstrip())
    if not red_loc and RED in line:
        red_col = line.index(RED)
        red_loc = (row, red_col)
        line[red_col] = EMPTY
    if not blue_loc and BLUE in line:
        blue_col = line.index(BLUE)
        blue_loc = (row, blue_col)
        line[blue_col] = EMPTY
    if not goal_loc and GOAL in line:
        goal_col = line.index(GOAL)
        goal_loc = (row, goal_col)
    board[row] = line
    
result = -1
visited = set()
queue = deque([(red_loc, blue_loc, 0, -1)])
flag = True

while flag and queue:
    cur_red_loc, cur_blue_loc, count, prev_dir = queue.popleft()
    if (cur_red_loc, cur_blue_loc) in visited or count >= 10:
        continue
    visited.add((cur_red_loc, cur_blue_loc))

    for i, move_dir in enumerate(dirs):
        move_result = move(cur_red_loc, cur_blue_loc, move_dir)
        if move_result['result'] == SUCCESS:
            result = count+1
            flag = False
            break
        elif move_result['result'] == CONTINUE:
            next_red_loc = move_result['red_loc']
            next_blue_loc = move_result['blue_loc']
            queue.append((next_red_loc, next_blue_loc, count+1, move_dir))

print(result)