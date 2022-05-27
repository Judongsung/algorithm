def spread_dust(rlen, clen, board):
    result = [[0 for __ in range(clen)] for _ in range(rlen)]
    r_dirs = [-1, 0, 0, 1]
    c_dirs = [0, -1, 1, 0]
    for r in range(rlen):
        for c in range(clen):
            el = board[r][c]
            if el == -1:
                result[r][c] = -1
                continue
            elif el == 0:
                continue
            
            spread_amount = el//5
            spread_count = 0
            if spread_amount:
                for i in range(4):
                    sr = r+r_dirs[i]
                    sc = c+c_dirs[i]
                    if 0 <= sr < rlen and 0 <= sc < clen and board[sr][sc] != -1:
                        result[sr][sc] += spread_amount
                        spread_count += 1
            result[r][c] += el-(spread_amount*spread_count)
    
    return result
    
def run_air_cleaner(rlen, clen, board, ac_loc):
    temp = [row.copy() for row in board]
    
    for i in range(ac_loc-1, 0, -1):
        temp[i][0] = temp[i-1][0]
    for i in range(0, clen-1):
        temp[0][i] = temp[0][i+1]
    for i in range(0, ac_loc):
        temp[i][clen-1] = temp[i+1][clen-1]
    for i in range(clen-1, 1, -1):
        temp[ac_loc][i] = temp[ac_loc][i-1]
    temp[ac_loc][1] = 0
    
    ac_loc_down = ac_loc+1
    for i in range(ac_loc_down+1, rlen-1):
        temp[i][0] = temp[i+1][0]
    for i in range(0, clen-1):
        temp[rlen-1][i] = temp[rlen-1][i+1]
    for i in range(rlen-1, ac_loc_down-1, -1):
        temp[i][clen-1] = temp[i-1][clen-1]
    for i in range(clen-1, 1, -1):
        temp[ac_loc_down][i] = temp[ac_loc_down][i-1]
    temp[ac_loc_down][1] = 0
    
    return temp

def solution(rlen, clen, t, board):
    for i in range(2, rlen-2):
        if board[i][0] == -1:
            air_cleaner_loc = i
            break
    
    for _ in range(t):
        board = spread_dust(rlen, clen, board)
        board = run_air_cleaner(rlen, clen, board, air_cleaner_loc)
    
    return sum([sum(row) for row in board])+2

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
result = solution(r, c, t, board)
print(result)