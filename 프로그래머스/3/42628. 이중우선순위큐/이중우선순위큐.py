import heapq
from collections import Counter

INSERT = "I"
DELETE = "D"
MAXNUM = "1"
MINNUM = "-1"

def solution(operations):
    answer = [0, 0]
    max_heap = []
    min_heap = []
    counter = Counter()
    
    for op in operations:
        op1, op2 = op.split()
        
        if op1 == INSERT:
            num = int(op2)
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
            counter[num] += 1
        elif op1 == DELETE:
            if op2 == MAXNUM:
                while max_heap and counter[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)

                if max_heap:
                    num = -heapq.heappop(max_heap)
                    counter[num] -= 1
                
            elif op2 == MINNUM:
                while min_heap and counter[min_heap[0]] == 0:
                    heapq.heappop(min_heap)

                if min_heap:
                    num = heapq.heappop(min_heap)
                    counter[num] -= 1
    
    while max_heap and counter[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
        
    while min_heap and counter[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    
    if max_heap:
        answer[0] = -max_heap[0]
        answer[1] = min_heap[0]
    
    return answer