from collections import defaultdict

TO = "to"
FROM = "from"
CREATED_NODE = 0
DONUT = 1
BAR = 2
EIGHT = 3

def check_graph_shape(graph, start):
    cur = start

    while True:
        if len(graph[cur][TO]) > 1:
            return EIGHT
        elif not graph[cur][TO]:
            return BAR
        elif graph[cur][TO][0] == start:
            return DONUT
        
        cur = graph[cur][TO][0]
        
def solution(edges):
    result = [0 for _ in range(4)]
    graph = defaultdict(lambda: {FROM:[], TO:[]})
    
    for start, end in edges:
        graph[start][TO].append(end)
        graph[end][FROM].append(start)
    
    for key in graph:
        if not graph[key][FROM]:
            created_node = key
            if len(graph[key][TO]) > 1:
                break
    
    result[CREATED_NODE] = created_node
    
    for node in graph[created_node][TO]:
        shape = check_graph_shape(graph, node)
        result[shape] += 1
    
    return result