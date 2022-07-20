text = input()
length = len(text)
idx = 0

result = 0
cur_num = 0
is_minus = False

while idx < length:
    ch = text[idx]
    if ch.isdigit():
        cur_num = cur_num*10 + int(ch)
    elif is_minus:
        result -= cur_num
        cur_num = 0
    else:
        result += cur_num
        cur_num = 0
        if ch == '-':
            is_minus = True
    idx += 1
else:
    if is_minus:
        result -= cur_num
    else:
        result += cur_num
    
print(result)