from sys import stdin


NO = "NO"
YES = "YES"

def is_interested_in_japan(query: list[int]) -> bool:
    if not (query[0] in [1, 2]):
        return False
    if not (query[3] >= 50):
        return False
    least_score = 100 if query[0] == 1 else 90
    if not ((query[1]*3 < least_score and query[2]*3 < least_score)\
            or (query[1] <= 21 or query[2] <= 21)):
        return False
    return True
    
q = int(stdin.readline())
for _ in range(q):
    query = list(map(int, stdin.readline().rstrip().split()))
    if is_interested_in_japan(query):
        print(YES)
    else:
        print(NO)