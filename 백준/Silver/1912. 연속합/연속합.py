from sys import stdin


def find_subseq_sum(sequence: list[int]) -> int:
    max_sum = -float('inf')
    cur_sum = 0

    for num in sequence:
        if cur_sum < 0:
            cur_sum = 0
            
        cur_sum += num
        max_sum = max(cur_sum, max_sum)

    return max_sum
            
n = int(stdin.readline())
seq = list(map(int, stdin.readline().rstrip().split()))
print(find_subseq_sum(seq))