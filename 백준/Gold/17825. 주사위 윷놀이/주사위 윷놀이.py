from sys import stdin

START = 0
FINISH = 42
SCORE = 0
BASIC_NEXT = 1
FIRST_NEXT = 2

def solution(dice):
    board = create_board()
    return dfs(board, dice, [START, START, START, START])

def create_board():
    board = {}
    for i in range(21):
        board[i*2] = [i*2, (i+1)*2, None]
    board[FINISH] = [0, None, None]
    board[-13] = [13, -16, None]
    board[-16] = [16, -19, None]
    board[-19] = [19, -25, None]
    board[-22] = [22, -24, None]
    board[-24] = [24, -25, None]
    board[-25] = [25, -30, None]
    board[-26] = [26, -25, None]
    board[-27] = [27, -26, None]
    board[-28] = [28, -27, None]
    board[-30] = [30, -35, None]
    board[-35] = [35, 40, None]
    board[10][2] = -13
    board[20][2] = -22
    board[30][2] = -28
    return board

def dfs(board, dice, obj_locations):
    if not dice:
        #print(obj_locations)
        return 0
    max_score = 0
    
    for i, obj_loc in enumerate(obj_locations):
        if obj_loc == FINISH:
            continue
        loc_info = board[obj_loc]
        next_loc = loc_info[FIRST_NEXT] if loc_info[FIRST_NEXT] else loc_info[BASIC_NEXT]
        for _ in range(dice[0]-1):
            if next_loc == FINISH:
                break
            next_loc = board[next_loc][BASIC_NEXT]
        if next_loc in obj_locations and next_loc != FINISH:
            continue
        temp_obj_locations = obj_locations.copy()
        temp_obj_locations[i] = next_loc
        score = board[next_loc][SCORE]+dfs(board, dice[1:], temp_obj_locations)
        max_score = max(score, max_score)
    return max_score

dice = list(map(int, stdin.readline().split()))
result = solution(dice)
print(result)