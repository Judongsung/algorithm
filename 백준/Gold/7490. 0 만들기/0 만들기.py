from sys import stdin
from itertools import product


ATTACH = 0
ADD = 1
SUB = 2
FUNCS = [lambda a,b: a*10+b, lambda a,b: a+b, lambda a,b: a-b]
CHARS = [' ', '+', '-']

def calc_formula(nums: list, exps: list) -> int:
    num_stack = [nums[0]]
    exp_stack = []
    np = 1
    for exp in exps:
        if exp == ATTACH:
            num_stack[-1] = FUNCS[exp](num_stack[-1], nums[np])
        else:
            num_stack.append(nums[np])
            exp_stack.append(exp)
        np += 1
    
    result = num_stack[0]
    for i, exp in enumerate(exp_stack):
        result = FUNCS[exp](result, num_stack[i+1])
    
    return result

def create_formula_text(nums: int, exps: list) -> str:
    result = []
    for num, exp in zip(nums, exps):
        result.append(str(num))
        result.append(CHARS[exp])
    result.append(str(nums[-1]))
    
    return ''.join(result)

def find_zero_formulas(nums: list) -> list:
    result = []
    
    for exps in product(range(3), repeat=len(nums)-1): # 0: ADD, 1: SUB, 2: ATTACH
        if calc_formula(nums, exps) == 0:
            result.append(create_formula_text(nums, exps))

    return result

t = int(stdin.readline().rstrip())
for i in range(t):
    n = int(stdin.readline().rstrip())
    nums = list(range(1, n+1))
    for formula in find_zero_formulas(nums):
        print(formula)
    if i < t-1:
        print()