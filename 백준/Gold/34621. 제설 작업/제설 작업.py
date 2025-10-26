from sys import stdin


def is_empty_list(lst: list[int]) -> bool:
    for el in lst:
        if el > 0:
            return False
    return True

def find_min_elem(lst: list[int]) -> tuple[int, int]:
    min_idx = 0
    min_elem = float('INF')
    
    for i, elem in enumerate(lst):
        if 0 < elem < min_elem:
            min_elem = elem
            min_idx = i
    
    return min_idx, min_elem

def find_min_power(board: list[list[int]]) -> int:
    min_power = 0
    row_sums = [0]*len(board)
    col_sums = [0]*len(board[0])

    for r, row in enumerate(board):
        for c, el in enumerate(row):
            row_sums[r] += el
            col_sums[c] += el
    
    while not is_empty_list(row_sums):
        min_row_idx, min_row_sum = find_min_elem(row_sums)
        min_col_idx, min_col_sum = find_min_elem(col_sums)

        if min_row_sum < min_col_sum:
            min_power = max(min_power, min_row_sum)
            for c, _ in enumerate(col_sums):
                col_sums[c] -= board[min_row_idx][c]
                
            row_sums[min_row_idx] = 0
            
        else:
            min_power = max(min_power, min_col_sum)
            for r, _ in enumerate(row_sums):
                row_sums[r] -= board[r][min_col_idx]
            
            col_sums[min_col_idx] = 0

    return min_power
        
n, m = map(int, stdin.readline().rstrip().split())
board = []
for _ in range(n):
    row = list(map(int, stdin.readline().rstrip().split()))
    board.append(row)
print(find_min_power(board))