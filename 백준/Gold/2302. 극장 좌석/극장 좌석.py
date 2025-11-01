from sys import stdin


MAX_N = 40

def find_seat_cases(n: int, vips: list[int]) -> int:
    left_seat = 1
    seat_groups = []
    longest_group = 0
    
    for v in vips+[n+1]:
        group = v-left_seat
        seat_groups.append(group)
        left_seat = v+1
        longest_group = max(group, longest_group)

    dp = [1]*(MAX_N+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, longest_group+1):
        dp[i] = dp[i-1]+dp[i-2]
    
    result = 1
    for group in seat_groups:
        result *= dp[group]
        
    return result

n = int(stdin.readline())
m = int(stdin.readline())
vips = []
for _ in range(m):
    vips.append(int(stdin.readline()))

print(find_seat_cases(n, vips))