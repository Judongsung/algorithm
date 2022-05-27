def check_loop(r, c, k, array):
    if r < len(array) and c < len(array[0]) and array[r][c] == k:
        return False
    return True

def fill_zeros(array):
    max_len = max([len(row) for row in array])
    
    for i, row in enumerate(array):
        rlen = len(row)
        row += [0]*(max_len-rlen)
    return

def sort_row(row):
    result = []
    count_map = {}
    
    for el in row:
        if not el:
            continue
        elif el not in count_map:
            count_map[el] = 0
        count_map[el] += 1

    el_count_pairs = list(count_map.items())
    el_count_pairs.sort(key=lambda x:x[0])
    el_count_pairs.sort(key=lambda x:x[1])
    for el, count in el_count_pairs:
        result += [el, count]
        if len(result) == 100:
            break
    
    return result

def convert_rowcol(array):
    rlen = len(array)
    clen = len(array[0])
    return [[array[r][c] for r in range(rlen)] for c in range(clen)]

def sort_array(array):
    rlen = len(array)
    clen = len(array[0])
    result = []
    
    if rlen >= clen:
        for row in array:
            sorted_row = sort_row(row)
            result.append(sorted_row)
        fill_zeros(result)
    else:
        for col in convert_rowcol(array):
            sorted_col = sort_row(col)
            result.append(sorted_col)
        fill_zeros(result)
        result = convert_rowcol(result)
    return result

def solution(r, c, k, array):
    arr = array
    time = 0
    r -= 1
    c -= 1
    
    while check_loop(r, c, k, arr):
        arr = sort_array(arr)
        time += 1
        if time > 100:
            return -1
    return time

r, c, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(3)]
result = solution(r, c, k, array)
print(result)