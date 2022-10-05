from sys import stdin

def night(score, visited=0, count=0):
    max_count = count
    for i in range(n):
        if i != mafia and not visited&1<<i:
            next_visited = visited|1<<i
            next_score = score.copy()
            for j in range(n):
                next_score[j] += sin_matrix[i][j]
            temp = day(next_score, next_visited, count+1)
            if temp > max_count:
                max_count = temp
    return max_count

def day(score, visited=0, count=0):
    max_score = 0
    max_num = -1
    for i in range(n):
        if not visited&1<<i and score[i] > max_score:
            max_score = score[i]
            max_num = i
    
    if max_num not in (-1, mafia):
        visited |= 1<<max_num
        count = night(score, visited, count)
    return count

n = int(stdin.readline())
sin_score = list(map(int, stdin.readline().split()))
sin_matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
mafia = int(stdin.readline())

if n%2:
    result = day(sin_score)
else:
    result = night(sin_score)
print(result)