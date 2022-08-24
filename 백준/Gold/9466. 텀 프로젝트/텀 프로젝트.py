from sys import stdin

def count_team_up(start):
    result = 0
    team_list = []
    index_dict = {}
    index = 0
    cur_num = start
    next_num = choice_list[start]
    while cur_num not in index_dict:
        if visited[cur_num]:
            result = 0
            break
        visited[cur_num] = True
        team_list.append(cur_num)
        index_dict[cur_num] = index
        index += 1
        cur_num = next_num
        next_num = choice_list[cur_num]
    else:
        loop_start_index = index_dict[cur_num]
        result = index-loop_start_index
    return result

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    choice_list = [None]+list(map(int, stdin.readline().split()))
    visited = [True]+[False for __ in range(n)]
    
    team_up_count = 0
    for i in range(1, n+1):
        if not visited[i]:
            team_up_count += count_team_up(i)
    print(n-team_up_count)