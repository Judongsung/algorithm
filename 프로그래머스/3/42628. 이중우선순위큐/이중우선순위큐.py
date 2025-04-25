import heapq

INSERT = "I"
DELETE = "D"
MAXNUM = "1"
MINNUM = "-1"

def solution(operations):
    answer = [0, 0]
    max_heap = []
    min_heap = []
    
    for op in operations:
        op1, op2 = op.split()
        
        if op1 == INSERT:
            num = int(op2)
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        elif op1 == DELETE:
            if not max_heap:
                continue
                
            if op2 == MAXNUM:
                num = heapq.heappop(max_heap)
                min_heap.remove(-num)
            elif op2 == MINNUM:
                num = heapq.heappop(min_heap)
                max_heap.remove(-num)
                
    if max_heap:
        answer[0] = -heapq.heappop(max_heap)
        answer[1] = heapq.heappop(min_heap)
    
    return answer