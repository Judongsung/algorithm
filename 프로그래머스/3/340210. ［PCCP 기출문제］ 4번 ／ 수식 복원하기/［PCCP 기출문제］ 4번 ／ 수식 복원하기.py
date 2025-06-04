from typing import List, Tuple, Union


X = 'X'
NOT_ONLY_ONE = '?'
PLUS = '+'
MINUS = '-'

def add_other_base(a:str, b:str, base:int) -> str:
    result = []
    if len(a) > len(b):
        b = b.zfill(len(a))
    elif len(a) < len(b):
        a = a.zfill(len(b))
    
    carry = 0
    for ia, ib, in zip(reversed(a), reversed(b)):
        ic = int(ia)+int(ib)+carry
        if ic >= base:
            ic -= base
            carry = 1
        else:
            carry = 0
        result.append(str(ic))
    if carry:
        result.append('1')
        
    return ''.join(reversed(result)).lstrip('0') or '0'

def subtract_other_base(a:str, b:str, base:int) -> str:
    result = []
    if len(a) > len(b):
        b = b.zfill(len(a))
    elif len(a) < len(b):
        a = a.zfill(len(b))
    
    borrow = 0
    for ia, ib, in zip(reversed(a), reversed(b)):
        ic = int(ia)-int(ib)-borrow
        if ic < 0:
            ic += base
            borrow = 1
        else:
            borrow = 0
        result.append(str(ic))
        
    return ''.join(reversed(result)).lstrip('0') or '0'

def close_range(a:str, b:str, c:str, symbol:str, low:int, high:int) -> Tuple[int, int]:
    new_low, new_high = 10, 0
    
    for base in range(low, high+1):
        if symbol == PLUS:
            candidate = add_other_base(a, b, base)
        elif symbol == MINUS:
            candidate = subtract_other_base(a, b, base)

        if candidate == c:
            if new_low == 10:
                new_low = base
            new_high = base
        elif new_low != 10:
            break
        
    return new_low, new_high

def adjust_low(a, b, c, low):
    digits = a+b
    if c != X:
        digits += c
    max_digit = max(int(d) for d in digits)
    return max(low, max_digit+1)

def guess_base_range(exp:str, low=2, high=9) -> Tuple[int, int]:
    a, symbol, b, equal, c = exp.split()
    low = adjust_low(a, b, c, low)
    if c == X:
        return low, high
    return close_range(a, b, c, symbol, low, high)

def update_exp(exp:str, low:int, high:int) -> str:
    a, symbol, b, equal, c = exp.split()
    if c != X:
        return exp

    answers = set()
    for base in range(low, high+1):
        if symbol == PLUS:
            temp = add_other_base(a, b, base)
        elif symbol == MINUS:
            temp = subtract_other_base(a, b, base)
        answers.add(temp)
        
    if len(answers) == 1:
        fill = answers.pop()
    else:
        fill = NOT_ONLY_ONE
    
    return f'{a} {symbol} {b} = {fill}'

def solution(expressions):
    result = []
    low = 2
    high = 9
    
    for exp in expressions:
        low, high = guess_base_range(exp, low, high)
        
    for exp in expressions:
        if exp.split()[4] == X:
            new_exp = update_exp(exp, low, high)
            result.append(new_exp)
    
    return result