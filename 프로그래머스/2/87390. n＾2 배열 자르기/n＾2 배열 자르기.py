def get_line(row, left, right):
    result = []
    row += 1
    
    for i in range(left+1, right+2):
        if i <= row:
            result.append(row)
        else:
            result.append(i)
    
    return result

def solution(n, left, right):
    result = []
    left_row, left_col = divmod(left, n)
    right_row, right_col = divmod(right, n)
    
    if left_row == right_row:
        result += get_line(left_row, left_col, right_col)
    else:
        result += get_line(left_row, left_col, n-1)
        for row in range(left_row+1, right_row):
            result += get_line(row, 0, n-1)
        result += get_line(right_row, 0, right_col)
        
    return result