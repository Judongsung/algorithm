from sys import stdin

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4
dirs = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [1, 4, 3, 5, 2, 6]
dice_num = [0 for _ in range(7)]

def roll_dice(dice, roll_dir):
    temp = [0]*6
    if roll_dir == RIGHT:
        temp[0] = dice[1]
        temp[1] = dice[5]
        temp[2] = dice[0]
        temp[3] = dice[3]
        temp[4] = dice[4]
        temp[5] = dice[2]
    elif roll_dir == LEFT:
        temp[0] = dice[2]
        temp[1] = dice[0]
        temp[2] = dice[5]
        temp[3] = dice[3]
        temp[4] = dice[4]
        temp[5] = dice[1]
    elif roll_dir == UP:
        temp[0] = dice[3]
        temp[1] = dice[1]
        temp[2] = dice[2]
        temp[3] = dice[5]
        temp[4] = dice[0]
        temp[5] = dice[4]
    elif roll_dir == DOWN:
        temp[0] = dice[4]
        temp[1] = dice[1]
        temp[2] = dice[2]
        temp[3] = dice[0]
        temp[4] = dice[5]
        temp[5] = dice[3]
    
    return temp

n, m, x, y, k = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
queries = list(map(int, stdin.readline().split()))
r = x
c = y
top = 1

for move_dir in queries:
    r_dir, c_dir = dirs[move_dir]
    if not (0 <= r+r_dir < n and 0 <= c+c_dir < m):
        continue
        
    r += r_dir
    c += c_dir
    dice = roll_dice(dice, move_dir)
    top = dice[0]
    bottom = dice[5]
    
    if board[r][c] == 0:
        board[r][c] = dice_num[bottom]
    else:
        dice_num[bottom] = board[r][c]
        board[r][c] = 0
        
    print(dice_num[top])