from sys import stdin


LED_BITS = [
    0b1110111,
    0b0010001,
    0b0111110,
    0b0111011,
    0b1011001,
    0b1101011,
    0b1101111,
    0b0110001,
    0b1111111,
    0b1111011
]

max_num, max_digit, count, raw_num = map(int, stdin.readline().rstrip().split())
max_led = str(max_num).zfill(max_digit)
raw_led = str(raw_num).zfill(max_digit)

def get_bit_diff(one: int, other: int) -> int:
    return (LED_BITS[one]^LED_BITS[other]).bit_count()

def dfs(led: str, idx: int, remain_count: int) -> int:
    if idx == max_digit:
        if int(led) == 0:
            return 0
        return 1

    result = 0
    cur = int(raw_led[idx])

    for i in range(10):
        next_led = led+str(i)
        if next_led > max_led:
            break
            
        bit_diff = get_bit_diff(cur, i)

        if bit_diff <= remain_count:
            result += dfs(next_led, idx+1, remain_count-bit_diff)

    return result

result = dfs('', 0, count)-1
print(result)