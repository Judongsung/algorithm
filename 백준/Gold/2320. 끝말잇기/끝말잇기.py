from sys import stdin

def find_max_score(cur, visited=0):
    visited |= 1<<cur
    if not memo[cur][visited]:
        max_score = 0
        for after in range(n):
            if not visited&1<<after and matrix[cur][after]:
                score = find_max_score(after, visited)
                if score > max_score:
                    max_score = score
        
        memo[cur][visited] = max_score+len(words[cur])
    return memo[cur][visited]

n = int(stdin.readline())
words = [stdin.readline().rstrip() for _ in range(n)]
matrix = [[0 for __ in range(n)] for _ in range(n)]
memo = [[0 for __ in range(2**16)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j and words[i][-1] == words[j][0]:
            matrix[i][j] = 1

max_score = 0
for i in range(n):
    score = find_max_score(i)
    if score > max_score:
        max_score = score
print(max_score)