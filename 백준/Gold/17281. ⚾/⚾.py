from sys import stdin
from itertools import permutations

def play(order):
    idx = 0
    score = 0

    for rdata in result_data:
        out_count = 0
        one, two, three = 0, 0, 0
        
        while out_count < 3:
            if rdata[order[idx]] == '0':
                out_count += 1
            elif rdata[order[idx]] == '1':
                score += three
                one, two, three = 1, one, two
            elif rdata[order[idx]] == '2':
                score += two+three
                one, two, three = 0, 1, one
            elif rdata[order[idx]] == '3':
                score += one+two+three
                one, two, three = 0, 0, 1
            elif rdata[order[idx]] == '4':
                score += 1+one+two+three
                one, two, three = 0, 0, 0
            idx = (idx+1)%9

    return score

n = int(stdin.readline())
result_data = [stdin.readline().split() for _ in range(n)]
max_score = 0

for perm in permutations(range(1, 9), 8):
    order = list(perm)
    order.insert(3, 0)
    max_score = max(max_score, play(order))

print(max_score)