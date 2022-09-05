from sys import stdin

operlist = [lambda a,b:a+b, lambda a,b:a-b]
n = int(stdin.readline())
numlist = list(map(int, stdin.readline().split()))
memo = [[0 for _ in range(21)] for _ in range(n-1)]
memo[0][numlist[0]] = 1

for i in range(n-2):
    cur = memo[i]
    other = numlist[i+1]
    
    for one in range(21):
        if cur[one] == 0:
            continue

        for op in operlist:
            temp = op(one, other)
            if 0 <= temp <= 20:
                memo[i+1][temp] += memo[i][one]
                
result = memo[-1][numlist[-1]]
print(result)