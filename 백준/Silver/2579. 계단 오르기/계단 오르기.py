n = int(input())
stairs = [int(input()) for _ in range(n)]
if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0]+stairs[1])
elif n == 3:
    print(max(stairs[:2])+stairs[2])
else:
    memo = [[] for _ in range(n)]
    memo[0].append(stairs[0])
    memo[0].append(stairs[0])
    memo[1].append(stairs[1])
    memo[1].append(stairs[0]+stairs[1])
    memo[2].append(memo[0][0]+stairs[2])
    memo[2].append(memo[1][0]+stairs[2])
    
    for i in range(3, n):
        memo[i].append(max(memo[i-2])+stairs[i])
        memo[i].append(memo[i-1][0]+stairs[i])
    
    result = max(memo[-1])
    print(result)