def move_line(raw_line):
    line = raw_line.copy()
    cur = 0
    while cur < len(line)-1:
        if line[cur] == line[cur+1]:
            line.pop(cur)
            line[cur] *= 2
        cur += 1
    return line

def up(board):
    global n
    result = [[0 for _ in range(n)] for __ in range(n)]
    
    for i in range(n):
        line = [row[i] for row in board if row[i] > 0]
        line_moved = move_line(line)
        for j, el in enumerate(line_moved):
            result[j][i] = el
    
    return result

def down(board):
    global n
    result = [[0 for _ in range(n)] for __ in range(n)]
    
    for i in range(n):
        line = [row[i] for row in board if row[i] > 0]
        line.reverse()
        line_moved = move_line(line)
        for j, el in enumerate(line_moved):
            result[n-1-j][i] = el
    
    return result

def left(board):
    global n
    result = [[0 for _ in range(n)] for __ in range(n)]
    
    for i in range(n):
        line = [el for el in board[i] if el > 0]
        line_moved = move_line(line)
        for j, el in enumerate(line_moved):
            result[i][j] = el
    
    return result

def right(board):
    global n
    result = [[0 for _ in range(n)] for __ in range(n)]
    
    for i in range(n):
        line = [el for el in board[i] if el > 0]
        line.reverse()
        line_moved = move_line(line)
        for j, el in enumerate(line_moved):
            result[i][n-1-j] = el
    
    return result

def move(board, count):
    if count == 5:
        return max([max(row) for row in board])
       
    func_list = [up, down, left, right]
    max_num = 0
    for func in func_list:
        temp = move(func(board), count+1)
        if temp > max_num:
            max_num = temp
    return max_num

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
result = move(board, 0)
print(result)