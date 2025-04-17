import heapq

def solution(n, works):
    q = [-work for work in works]
    heapq.heapify(q)
    
    for _ in range(n):
        work = heapq.heappop(q)
        work += 1
        if work < 0:
            heapq.heappush(q, work)
        elif not q:
            break

    answer = 0
    while q:
        work = heapq.heappop(q)
        answer += work**2
    
    return answer