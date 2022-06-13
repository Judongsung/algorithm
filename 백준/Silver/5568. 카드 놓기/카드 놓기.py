def dfs(n, k, remain_cards, num_str=''):
    global num_set
    if k == 0:
        num_set.add(num_str)
    for i, card in enumerate(remain_cards):
        next_remains = remain_cards.copy()
        del next_remains[i]
        dfs(n, k-1, next_remains, num_str+card)
    return
            
num_set = set()
n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
dfs(n, k, cards)
print(len(num_set))