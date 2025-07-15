from sys import stdin

def calc_budget(demands: list, threshold: int) -> int:
    return sum([min(demand, threshold) for demand in demands])

def assign_budget(total_budget: int, demands: list) -> int:
    if calc_budget(demands, max(demands)) <= total_budget:
        return max(demands)
        
    max_threshold = 0
    left = 0
    right = total_budget
    
    while left < right:
        cur = (left+right)//2
        budget = calc_budget(demands, cur)
        if budget <= total_budget:
            max_threshold = max(cur, max_threshold)
            left = cur+1
        else:
            right = cur

    return max_threshold
    
n = int(stdin.readline())
demands = list(map(int, stdin.readline().rstrip().split()))
total_budget = int(stdin.readline())
print(assign_budget(total_budget, demands))