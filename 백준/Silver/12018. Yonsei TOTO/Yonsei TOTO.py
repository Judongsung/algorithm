from sys import stdin


n, m = map(int, stdin.readline().rstrip().split())
min_success_points = []
for _ in range(n):
    p, l = map(int, stdin.readline().rstrip().split())
    applied_points = list(map(int, stdin.readline().rstrip().split()))
    
    if p < l:
        min_success_points.append(1)
        continue
        
    min_success_point = sorted(applied_points)[p-l]
    min_success_points.append(min_success_point)

result = 0
for point in sorted(min_success_points):
    if point <= m:
        m -= point
        result += 1
    
print(result)