from sys import stdin


def rank(scores: list, new_score: int, top_n: int) -> int:
    if not scores:
        return 1
    elif len(scores) == top_n and new_score <= scores[-1]:
        return -1
    elif new_score < scores[-1]:
        return len(scores)+1
    
    for i, score in enumerate(scores):
        if score <= new_score:
            return i+1
    return -1

n, new_score, top_n = map(int, stdin.readline().rstrip().split())
scores = list(map(int, stdin.readline().rstrip().split()))

print(rank(scores, new_score, top_n))