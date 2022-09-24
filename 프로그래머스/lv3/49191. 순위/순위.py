from collections import deque

PREV_NUM = 0
NEXT_SET = 1

def solution(n, results):
    answer = 0
    all_comparable = 2**n-1
    win_graph = [[0, set()] for _ in range(n+1)]
    lose_graph = [[0, set()] for _ in range(n+1)]
    win_graph[0][PREV_NUM] = -1
    lose_graph[0][PREV_NUM] = -1
    
    for winner, loser in results:
        win_graph[winner][NEXT_SET].add(loser)
        win_graph[loser][PREV_NUM] += 1
        lose_graph[loser][NEXT_SET].add(winner)
        lose_graph[winner][PREV_NUM] += 1
    
    win_bits = find_prev_bit(n, win_graph)
    lose_bits = find_prev_bit(n, lose_graph)
    for i in range(1, n+1):
        if win_bits[i]|lose_bits[i] == all_comparable:
            answer += 1
    
    return answer

def find_prev_bit(n, graph):
    prev_bits = [0 for _ in range(n+1)]
    queue = deque([i for i, node in enumerate(graph) if not node[PREV_NUM]])
    
    while queue:
        cur_node = queue.popleft()
        prev_bits[cur_node] |= 1<<cur_node-1
        
        for next_node in graph[cur_node][NEXT_SET]:
            prev_bits[next_node] |= prev_bits[cur_node]
            graph[next_node][PREV_NUM] -= 1
            if graph[next_node][PREV_NUM] == 0:
                queue.append(next_node)
                
    return prev_bits