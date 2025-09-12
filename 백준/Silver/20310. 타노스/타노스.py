from sys import stdin


ZERO = '0'
ONE = '1'

def half_string(s: str) -> str:
    result = []
    zero_count = s.count(ZERO)
    one_count = len(s)-zero_count
    zero_count //= 2
    one_count //= 2

    for ch in s:
        if ch == ZERO and zero_count:
            result.append(ZERO)
            zero_count -= 1
        elif ch == ONE:
            if one_count:
                one_count -= 1
            else:
                result.append(ONE)

    return ''.join(result)
    

s = stdin.readline().rstrip()
result = half_string(s)
print(result)