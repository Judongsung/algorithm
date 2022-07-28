ERROR = -1
ANY = 0
CAMEL = 1
SNAKE = 2

def check_coding_style(data):
    result = ERROR
    upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if not (data[0] in upper_alpha or data[0] == '_' or data[-1] == '_' or '__' in data):
        has_upper_alpha = False
        has_underline = False
        
        for ch in upper_alpha:
            if ch in data:
                has_upper_alpha = True
                break
        has_underline = '_' in data
        
        if has_upper_alpha and not has_underline:
            result = CAMEL
        elif not has_upper_alpha and has_underline:
            result = SNAKE
        elif not has_upper_alpha and not has_underline:
            result = ANY
    return result

def to_camel_case(data):
    result = ''
    is_upper = False
    for ch in data:
        if is_upper:
            ch = ch.upper()
            is_upper = False
        if ch == '_':
            is_upper = True
            continue
        result += ch
    
    return result

def to_snake_case(data):
    result = ''
    for ch in data:
        if ch.isupper():
            result += '_'
            ch = ch.lower()
        result += ch
    
    return result

data = input()
coding_style = check_coding_style(data)
if coding_style == CAMEL:
    result = to_snake_case(data)
elif coding_style == SNAKE:
    result = to_camel_case(data)
elif coding_style == ANY:
    result = data
else:
    result = 'Error!'
print(result)