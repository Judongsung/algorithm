from sys import stdin


MEMORY = 0
BOOT_TIME = 1

def find_min_cost(app_info: list[tuple[int]], threshold: int) -> int:
    max_boot_time = sum([boot_time for _, boot_time in app_info])
    dp = [0]*(max_boot_time+1)
    dp[0] = 0

    for ainfo in sorted(app_info, key=lambda x:x[BOOT_TIME], reverse=True):
        memory, boot_time = ainfo[MEMORY], ainfo[BOOT_TIME]
        for bt in range(max_boot_time, boot_time-1, -1):
            dp[bt] = max(dp[bt], dp[bt-boot_time]+memory)
    
    for bt, memory in enumerate(dp):
        if memory >= threshold:
            return bt
            
n, m = map(int, stdin.readline().rstrip().split())
memory = list(map(int, stdin.readline().rstrip().split()))
cost = list(map(int, stdin.readline().rstrip().split()))
app_info = [(memory[i], cost[i]) for i in range(n)]
print(find_min_cost(app_info, m))