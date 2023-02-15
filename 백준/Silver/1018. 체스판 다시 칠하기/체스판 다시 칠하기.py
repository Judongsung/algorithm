from sys import stdin

WHITE = 'W'
BLACK = 'B'
BOARD_SIZE = 8
TOTAL_COUNT = BOARD_SIZE**2
min_count = TOTAL_COUNT

def is_odd_white(el, num):
    return (num%2 and el == WHITE) or (not num%2 and el == BLACK)

n, m = map(int, stdin.readline().split())
memo = [[0 for __ in range(m-BOARD_SIZE+1)] for _ in range(n)]

for row in range(n):
    count = 0
    line = stdin.readline()
    
    for i in range(BOARD_SIZE):
        count += is_odd_white(line[i], i)
    if row%2:
        memo[row][0] = count
    else:
        memo[row][0] = BOARD_SIZE-count
    
    for i in range(m-BOARD_SIZE):
        count -= is_odd_white(line[i], i)
        count += is_odd_white(line[i+BOARD_SIZE], i+BOARD_SIZE)
        if row%2:
            memo[row][i+1] = count
        else:
            memo[row][i+1] = BOARD_SIZE-count

for row in range(n-BOARD_SIZE+1):
    for col in range(m-BOARD_SIZE+1):
        count = sum([memo[r][col] for r in range(row, row+BOARD_SIZE)])
        
        if count < min_count:
            min_count = count
        if TOTAL_COUNT-count < min_count:
            min_count = TOTAL_COUNT-count

print(min_count)