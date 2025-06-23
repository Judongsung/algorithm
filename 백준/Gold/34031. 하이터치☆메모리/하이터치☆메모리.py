from sys import stdin
from collections import Counter


def count_hightouch(left: list, right: list) -> int:
    if left[0] == ')':
        return 0
    count = 0
    l_counter = Counter()

    l_stack = 0
    for ch in left:
        if ch == '(':
            l_stack += 1
        else:
            l_stack -= 1
            if l_stack < 0:
                break
        l_counter[l_stack] += 1

    r_stack = 0
    r_front = 0
    for ch in right:
        if ch == ')':
            r_stack += 1
            r_front = max(r_stack, r_front)
            if r_stack >= r_front:
                count += l_counter[r_stack]
        else:
            r_stack -= 1

    return count

left = stdin.readline().rstrip()
right = stdin.readline().rstrip()
print(count_hightouch(left, right))