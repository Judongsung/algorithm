from __future__ import annotations
from sys import stdin, setrecursionlimit


# setrecursionlimit(10**5)

def count_unique_subseq(n: int, seq: list[int]) -> int:
    count = 0
    uniques = set()
    left = 0
    dp = {}

    def count_subseq(length: int, starts: int) -> int:
        '''
        if starts == 0:
            return 0
        if (length, starts) not in dp:
            dp[(length, starts)] = count_subseq(length, starts-1)+length-starts+1
        return dp[(length, starts)]
        '''
        count = 0
        for i in range(starts):
            count += length-i
        return count

    for right in range(n):
        rnum = seq[right]
        
        if rnum in uniques:
            unique_len = right-left
            unique_starts = 0
            
            while rnum in uniques:
                uniques.remove(seq[left])
                left += 1
                unique_starts += 1
                
            count += count_subseq(unique_len, unique_starts)
            
        uniques.add(rnum)
        
    unique_len = right-left+1
    count += count_subseq(unique_len, unique_len)
    
    return count

n = int(stdin.readline().rstrip())
seq = list(map(int, stdin.readline().rstrip().split()))
result = count_unique_subseq(n, seq)
print(result)