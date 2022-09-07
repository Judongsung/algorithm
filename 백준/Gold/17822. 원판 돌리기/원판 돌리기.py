from sys import stdin

dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

n, m, t = map(int, stdin.readline().split())
rullet = [None for _ in range(n)]
for i in range(n):
    circle = list(map(int, stdin.readline().split()))
    rullet[i] = circle
    
for _ in range(t):
    x, d, k = map(int, stdin.readline().split())
    for i in [i for i in range(n) if (i+1)%x==0]:
        weight = 1 if d == 1 else -1
        rullet[i] = rullet[i][weight*k:]+rullet[i][:weight*k]
    
    after_rullet = [[None for __ in range(m)] for _ in range(n)]
    exist_near_same = False
    
    for r in range(n):
        for c in range(m):
            num = rullet[r][c]
            after_rullet[r][c] = num
            if num == -1:
                continue
            for r_dir, c_dir in dirs:
                near_r = r+r_dir
                near_c = (c+c_dir)%m
                if 0 <= near_r < n:
                    if num == rullet[near_r][near_c]:
                        after_rullet[r][c] = -1
                        exist_near_same = True
    
    if exist_near_same:
        rullet = after_rullet
    else:
        numlist = []
        for circle in rullet:
            numlist += [num for num in circle if num != -1]
            
        if numlist:
            avg = sum(numlist)/len(numlist)

            for r in range(n):
                for c in range(m):
                    if rullet[r][c] == -1:
                        continue
                    if rullet[r][c] > avg:
                        rullet[r][c] -= 1
                    elif rullet[r][c] < avg:
                        rullet[r][c] += 1

result = 0
for circle in rullet:
    for num in circle:
        if num != -1:
            result += num
            
print(result)