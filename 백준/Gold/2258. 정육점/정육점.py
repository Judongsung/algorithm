from sys import stdin


WEIGHT = 0
COST = 1

def find_min_cost(meats: list[tuple[int]], needs: int) -> int:
    cur_w = 0
    sorted_meats = sorted(meats, key=lambda x:(x[COST], -x[WEIGHT]))
    prev_cost = -1
    cost_cnt = 1

    for i, (weight, cost) in enumerate(sorted_meats):
        cur_w += weight
        
        if cost == prev_cost:
            cost_cnt += 1
        else:
            cost_cnt = 1

        if cur_w >= needs:
            result = cost*cost_cnt

            for j in range(i+1, len(sorted_meats)):
                if sorted_meats[j][COST] > cost:
                    result = min(result, sorted_meats[j][COST])
                    break

            return result

        prev_cost = cost

    return -1    

n, m = map(int, stdin.readline().rstrip().split())
meats = []
for _ in range(n):
    w, c = map(int, stdin.readline().rstrip().split())
    meats.append((w, c))

print(find_min_cost(meats, m))