from sys import stdin

def is_mixed(word_a, word_b, word_c, visited, aidx=0, bidx=0, cidx=0):
    if aidx == len(word_a) and bidx == len(word_b):
        return True
    if visited[aidx][bidx]:
        return False
    visited[aidx][bidx] = True
    result_one = False
    result_two = False
    
    if aidx < len(word_a) and word_c[cidx] == word_a[aidx]:
        result_one = is_mixed(word_a, word_b, word_c, visited, aidx+1, bidx, cidx+1)
    if bidx < len(word_b) and word_c[cidx] == word_b[bidx]:
        result_two = is_mixed(word_a, word_b, word_c, visited, aidx, bidx+1, cidx+1)
    return result_one or result_two
    
n = int(input())
for i in range(1, n+1):
    word_a, word_b, word_c = input().split()
    visited = [[False for _ in range(len(word_b)+1)] for _ in range(len(word_a)+1)]
    result = 'yes' if is_mixed(word_a, word_b, word_c, visited) else 'no'
    print('Data set '+str(i)+': '+str(result))