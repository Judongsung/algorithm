from collections import Counter
from typing import List
from sys import stdin


def count_good_number(n: int, numlist: List[int]) -> int:
    good_nums = set()
    counter = Counter(numlist)

    for i, one in enumerate(numlist):
        for j in range(i+1, n):
            other = numlist[j]
            target = one+other
            if target in counter:
                if (target == one or target == other) and counter[target] > 1:
                    if one == other and counter[target] > 2:
                        good_nums.add(target)
                    elif one != other and counter[target] > 1:
                        good_nums.add(target)
                elif target != one and target != other:
                    good_nums.add(target)

    return sum([counter[num] for num in good_nums])

n = int(stdin.readline())
nums = list(map(int, stdin.readline().rstrip().split()))
result = count_good_number(n, nums)
print(result)