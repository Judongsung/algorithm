def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

operlist = {'+':add, '-':sub, '*':mul}
calc_map = {}

def calc(num1, num2, op):
    tpl = (num1, num2, op)
    if tpl not in calc_map:
        calc_map[tpl] = op(num1, num2)
    return calc_map[tpl]

def dfs(num_count, nums, opers):
    if num_count == 2:
        return calc(nums[0][0], nums[1][0], opers[0])
    max_result = -2**31
    
    for i in range(num_count-1):
        if i > 0 and (nums[i][1] or nums[i+1][1]):
            continue
        nums_temp = nums.copy()
        opers_temp = opers.copy()
        num1 = nums_temp.pop(i)[0]
        num2 = nums_temp.pop(i)[0]
        op = opers_temp.pop(i)
        num3 = [calc(num1, num2, op), True]
        nums_temp.insert(i, num3)
        temp_result = dfs(num_count-1, nums_temp, opers_temp)
        if temp_result > max_result:
            max_result = temp_result
    return max_result

def solution(n, exp):
    if n == 1:
        return exp
    nums = [[int(num), 0] for i, num in enumerate(exp) if i%2 == 0]
    opers = [operlist[oper] for i, oper in enumerate(exp) if i%2 == 1]
    result = dfs(n//2+1, nums, opers)
    return result

n = int(input())
exp = input()
result = solution(n, exp)
print(result)