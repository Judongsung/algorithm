from sys import stdin

def solution(n, m, truth_count, truth_know_list, party_list):
    result = 0
    truth_know_set = set(truth_know_list)
    spread_map = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    for party in party_list:
        for e1 in party[1:]:
            for e2 in party[1:]:
                if e1 == e2 or e1 in spread_map[e2]:
                    continue
                spread_map[e1].append(e2)
                spread_map[e2].append(e1)
    
    for know in truth_know_list:
        if visited[know]:
            continue
        queue = [know]
        visited[know] = True
        while queue:
            man = queue.pop()
            for spread in spread_map[man]:
                if not visited[spread]:
                    truth_know_set.add(spread)
                    queue.append(spread)
                    visited[spread] = True
        
    for party in party_list:
        party_set = set(party[1:])
        if not party_set&truth_know_set:
            result += 1
            
    return result

n, m = map(int, stdin.readline().split())
truth_info = list(map(int, stdin.readline().split()))
truth_know_count = truth_info[0]
truth_know_list = truth_info[1:]
party_list = [list(map(int, stdin.readline().split())) for _ in range(m)]
result = solution(n, m, truth_know_count, truth_know_list, party_list)
print(result)