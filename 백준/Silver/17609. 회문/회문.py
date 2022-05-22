import math

def check(s, diff_count=0):
    len_s = len(s)
    half_len = math.ceil(len_s/2)
    front_cur = 0
    end_cur = len_s-1
    
    while front_cur <= end_cur:
        front_ch = s[front_cur]
        end_ch = s[end_cur]
        if front_ch != end_ch:
            if diff_count > 0:
                return 2
            if check(s[front_cur+1:end_cur+1], diff_count+1) == 0 or check(s[front_cur:end_cur], diff_count+1) == 0:
                return 1
            else:
                return 2
        front_cur += 1
        end_cur -= 1
    else:
            return 0

t = int(input())
strings = [input() for _ in range(t)]
for s in strings:
    result = check(s)
    print(result)