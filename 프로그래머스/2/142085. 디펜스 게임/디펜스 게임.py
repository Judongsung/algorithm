import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    
    for i, en in enumerate(enemy):
        while n < en and k > 0:
            k -= 1
            if heap and -heap[0] > en:
                n -= heapq.heappop(heap)
            else:
                break
        else:
            if n >= en:
                n -= en
                heapq.heappush(heap, -en)
            else:
                return i
            
    return len(enemy)