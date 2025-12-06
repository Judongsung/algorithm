from sys import stdin


def find_min_move(left: int, right: int, goals: list[int]) -> int:
    def find_next_moves(left: int, right: int, goal: int, prev_move: int) -> dict[tuple[int], int]:
        result = {}
        
        if 0 <= goal < right:
            result[(goal, right)] = prev_move+abs(left-goal)
            
        if left < goal <= n:
            result[(left, goal)] = prev_move+abs(right-goal)

        return result

    dp = find_next_moves(left, right, goals[0], 0)
    
    for goal in goals[1:]:
        next_dp = {}
        for key, val in dp.items():
            l, r = key
            next_moves = find_next_moves(l, r, goal, val)

            for next_key, next_val in next_moves.items():
                if next_key not in next_dp:
                    next_dp[next_key] = next_val
                    continue
                    
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