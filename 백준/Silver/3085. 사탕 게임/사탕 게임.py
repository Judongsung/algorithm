from sys import stdin

def count_equal_color_line(arr):
    max_count = 1
    count = 1
    cur = arr[0]
    for e in arr[1:]:
        if e == cur:
            count += 1
        else:
            max_count = max(count, max_count)
            cur = e
            count = 1
    max_count = max(count, max_count)
    return max_count

def get_max_count_bomboni(board):
    max_count = 1
    for i, row in enumerate(board[:-1]):
        count = count_equal_color_line(row)
        max_count = max(count, max_count)
        next_row = board[i+1]
        for j, e in enumerate(row):
            next_e = next_row[j]
            if e != next_e:
                temp = row.copy()
                temp[j] = next_e
                count = count_equal_color_line(temp)
                max_count = max(count, max_count)
                
                temp = next_row.copy()
                temp[j] = e
                count = count_equal_color_line(temp)
                max_count = max(count, max_count)
                
                temp = [row[j] for row in board]
                temp[i] = next_e
                temp[i+1] = e
                count = count_equal_color_line(temp)
                max_count = max(count, max_count)
    count = count_equal_color_line(board[-1])
    max_count = max(count, max_count)
    
    return max_count

n = int(stdin.readline())
board = [list(stdin.readline()) for _ in range(n)]
converted_board = [[board[j][i] for j in range(n)] for i in range(n)]
result = max(get_max_count_bomboni(board), get_max_count_bomboni(converted_board))
print(result)