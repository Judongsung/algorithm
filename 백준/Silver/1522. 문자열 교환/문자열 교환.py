from sys import stdin


def find_min_swap(text: str) -> int:
    window_len = text.count('a')
    circular_txt = text+text[:window_len]
    b_count = text[:window_len].count('b')
    min_b_count = b_count

    for i, remove_ch in enumerate(text):
        new_ch = circular_txt[i+window_len]
        
        if remove_ch == 'b':
            b_count -= 1
            
        if new_ch == 'b':
            b_count += 1

        min_b_count = min(b_count, min_b_count)

    return min_b_count

data = stdin.readline().rstrip()
print(find_min_swap(data))