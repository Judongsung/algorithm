from sys import stdin
from heapq import heapify, heappush, heappop


def has_semi_sequence(n: int, k: int, nums: list[int]) -> list[int]:
    sequence_set = set(nums[:k])
    min_heap = nums[:k]
    heapify(min_heap)
    max_heap = [-num for num in nums[:k]]
    heapify(max_heap)
    
    def is_semi_sequence() -> bool:
        nonlocal min_heap, max_heap

        min_num = min_heap[0]
        max_num = -max_heap[0]
        
        if max_num-min_num+1 == k:
            return True
        return False

    if is_semi_sequence():
        return nums[:k]

    for left_idx, right_idx in zip(range(n-k), range(k, n)):
        left = nums[left_idx]
        right = nums[right_idx]
        
        sequence_set.remove(left)
        sequence_set.add(right)
        heappush(min_heap, right)
        heappush(max_heap, -right)

        while min_heap[0] not in sequence_set:
            heappop(min_heap)
        while -max_heap[0] not in sequence_set:
            heappop(max_heap)

        if is_semi_sequence():
            return nums[left_idx+1:right_idx+1]

    return []
        
        
        
n, k = map(int, stdin.readline().rstrip().split())
nums = list(map(int, stdin.readline().rstrip().split()))
result = has_semi_sequence(n, k, nums)

if result:
    print('YES')
    print(*result)
else:
    print('NO')