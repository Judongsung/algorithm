from sys import stdin


def find_max_visit_days(visits: list, days: int) -> tuple:
    visit = sum(visits[:days])
    max_visit = visit
    num = 1

    for i in range(len(visits)-days):
        visit -= visits[i]
        visit += visits[i+days]
        if visit > max_visit:
            max_visit = visit
            num = 1
        elif visit == max_visit:
            num += 1

    return max_visit, num
        
n, x = map(int, stdin.readline().rstrip().split())
visits = list(map(int, stdin.readline().rstrip().split()))
    
max_visit, num = find_max_visit_days(visits, x)
if max_visit == 0:
    print("SAD")
else:
    print(max_visit, num, sep='\n')