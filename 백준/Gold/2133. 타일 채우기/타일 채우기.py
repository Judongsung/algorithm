from sys import stdin


def find_tile_filling_cases(width: int) -> int:
    if width%2 != 0:
        return 0
        
    height = 3
    h_max_bits = (1<<height)-1
    memo = [[0 for __ in range(h_max_bits+1)] for _ in range(width)]
    
    memo[0][(1<<0)+(1<<1)] = 1
    memo[0][(1<<1)+(1<<2)] = 1
    
    for i in range(height):
        memo[1][1<<i] += memo[0][(h_max_bits)-(1<<i)]
        
    for i in ((1<<0)+(1<<1), (1<<1)+(1<<2)):
        memo[1][i] += memo[0][h_max_bits]
        
    memo[1][h_max_bits] = 3

    for w in range(2, width):
        for i in range(height):
            memo[w][1<<i] += memo[w-1][(h_max_bits)-(1<<i)]
            
        for i in ((1<<0)+(1<<1), (1<<1)+(1<<2)):
            memo[w][i] += memo[w-1][h_max_bits]+memo[w-1][h_max_bits-i]

        memo[w][h_max_bits] += memo[w-2][h_max_bits] + memo[w][1<<0] + memo[w][1<<2]
        
    return memo[-1][h_max_bits]

n = int(stdin.readline())
result = find_tile_filling_cases(n)
print(result)