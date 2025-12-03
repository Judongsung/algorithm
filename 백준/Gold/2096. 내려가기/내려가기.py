from sys import stdin

COL = 3
MAX = 0
MIN = 1

def solution() -> tuple[int]:
    n = int(stdin.readline())
    row = list(map(int, stdin.readline().rstrip().split()))
    memo = [[score]*2 for score in row]
    
    for r in range(n-1):
        row = list(map(int, stdin.readline().rstrip().split()))
        next_memo = [[0, float('inf')] for _ in range(COL)]
        
        for c in range(COL):
            if c > 0:
                next_memo[c-1][MAX] = max(memo[c][MAX]+row[c-1], next_memo[c-1][MAX])
                next_memo[c-1][MIN] = min(memo[c][MIN]+row[c-1], next_memo[c-1][MIN])
            
            next_memo[c][MAX] = max(memo[c][MAX]+row[c], next_memo[c][MAX])
            next_memo[c][MIN] = min(memo[c][MIN]+row[c], next_memo[c][MIN])

            if c < COL-1:
                next_memo[c+1][MAX] = max(memo[c][MAX]+row[c+1], next_memo[c+1][MAX])
                next_memo[c+1][MIN] = min(memo[c][MIN]+row[c+1], next_memo[c+1][MIN])

        memo = next_memo

    max_score = 0
    min_score = float('inf')

    for scores in memo:
        max_score = max(scores[MAX], max_score)
        min_score = min(scores[MIN], min_score)
    
    return (max_score, min_score)

print(*solution())