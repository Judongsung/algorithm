from sys import stdin

BUCKET_NUM = 3

def dfs(a, b, c):
    if (a, b, c) in checked:
        return
    elif a == 0:
        result_set.add(str(c))
    checked.add((a, b, c))
    
    amounts = [a, b, c]
    
    for one in range(BUCKET_NUM):
        for other in range(one+1, BUCKET_NUM):
            na, nb, nc = pour(amounts, one, other)
            dfs(na, nb, nc)
    for one in range(BUCKET_NUM-1, -1, -1):
        for other in range(one-1, -1, -1):
            na, nb, nc = pour(amounts, one, other)
            dfs(na, nb, nc)
        
def pour(arr, from_num, to_num):
    result = arr.copy()
    
    result[to_num] += result[from_num]
    result[from_num] = 0
    if result[to_num] > bucket_sizes[to_num]:
        result[from_num] = result[to_num]-bucket_sizes[to_num]
        result[to_num] = bucket_sizes[to_num]
        
    return result

bucket_sizes = list(map(int, stdin.readline().split()))
checked = set()
result_set = set()
dfs(0, 0, bucket_sizes[-1])
result = sorted(list(result_set), key=lambda x:int(x))
print(' '.join(result))