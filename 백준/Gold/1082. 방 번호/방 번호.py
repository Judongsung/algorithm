from sys import stdin
from collections import Counter


TOTAL_COUNT = 0
COUNTER = 1

def find_max_number(n: int, prices: list[int], money: int) -> str:
    dp = [[0, Counter()] for _ in range(money+1)]

    def is_better(one: list, other: list) -> bool:
        nonlocal n
        
        if one[TOTAL_COUNT] != other[TOTAL_COUNT]:
            return one[TOTAL_COUNT] > other[TOTAL_COUNT]

        for i in range(n-1, -1, -1):
            if one[COUNTER][i] == other[COUNTER][i]:
                continue
            return one[COUNTER][i] > other[COUNTER][i]
    
    for m in range(1, money+1):
        best_state_for_m = dp[0]
        best_num = -1
        
        for i in range(n):
            price = prices[i]
            prev_cost = m-price

            if prev_cost < 0:
                continue
            
            prev_state = dp[prev_cost]

            if prev_state[TOTAL_COUNT] == 0 and prev_cost != 0:
                continue
    
            if prev_state[TOTAL_COUNT] == 0 and i == 0:
                if m == prices[0]:
                    candidate_state = [1, Counter([0])]
                else:
                    continue
            elif i == 0 and len(prev_state[COUNTER]) == 1 and prev_state[COUNTER][0] > 0:
                continue
            else:
                candidate_state = [prev_state[TOTAL_COUNT]+1, prev_state[COUNTER].copy()]
                candidate_state[COUNTER][i] += 1
                
            if is_better(candidate_state, best_state_for_m):
                best_state_for_m = candidate_state

        dp[m] = best_state_for_m

    total_best_state = dp[0]
    for m in range(1, money+1):
        if is_better(dp[m], total_best_state):
            total_best_state = dp[m]
    
    result = ""
    for d in range(n-1, -1, -1):
        result += str(d)*total_best_state[COUNTER][d]
    
    return result if result else "0"
    
n = int(stdin.readline())
p = list(map(int, stdin.readline().rstrip().split()))
m = int(stdin.readline())

print(find_max_number(n, p, m))