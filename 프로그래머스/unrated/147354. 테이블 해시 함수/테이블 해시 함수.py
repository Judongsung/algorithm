def get_s(tpl, idx):
    s = 0
    for el in tpl:
        s += el%idx
    return s

def solution(data, col, row_begin, row_end):
    answer = 0
    sorted_data = sorted(data, key=lambda x:-x[0])
    sorted_data = sorted(sorted_data, key=lambda x:x[col-1])

    cur = get_s(sorted_data[row_begin-1], row_begin)
    for idx in range(row_begin, row_end):
        cur ^= get_s(sorted_data[idx], idx+1)
    
    return cur