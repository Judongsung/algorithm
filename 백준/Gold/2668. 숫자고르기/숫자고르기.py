from sys import stdin

def dfs(start):
    num = start
    order_dict = {}
    order = 0
    
    while num not in order_dict:
        visited[num] = True
        order_dict[num] = order
        order += 1
        num = board[num]
    else:
        num_order = order_dict[num]

    result = list(order_dict.keys())
    result.sort(key=lambda x:order_dict[x])
    return set(result[num_order:])

n = int(stdin.readline())
board = [None]+[int(stdin.readline()) for _ in range(n)]
visited = [False for _ in range(n+1)]
result_set = set()

for num in range(1, n+1):
    if not visited[num]:
        temp = dfs(num)
        result_set.update(temp)
result_list = list(result_set)
result_list.sort()
print(len(result_list))
for el in result_list:
    print(el)