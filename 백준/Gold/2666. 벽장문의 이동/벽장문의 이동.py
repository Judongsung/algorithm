from sys import stdin


def find_min_move(left: int, right: int, goals: list[int]) -> int:
    dp = {(left, right): 0}
    
    for goal in goals:
        next_dp = {}
        for key, val in dp.items():
            l, r = key

            if goal < r:
                next_key = tuple(sorted([goal, r]))
                next_val = val + abs(l-goal)
                
                if next_key not in next_dp:
                    next_dp[next_key] = next_val
                else:
                    next_dp[next_key] = min(next_val, next_dp[next_key])

            if goal > l:
                next_key = tuple(sorted([l, goal]))
                next_val = val + abs(r-goal)
                
                if next_key not in next_dp:
                    next_dp[next_key] = next_val
                else:
                    next_dp[next_key] = min(next_val, next_dp[next_key])
            
        dp = next_dp
        
    return min(dp.values())

n = int(stdin.readline())
l, r = map(int, stdin.readline().rstrip().split())
m = int(stdin.readline())
goals = []
for _ in range(m):
    goal = int(stdin.readline())
    goals.append(goal)

print(find_min_move(l, r, goals))