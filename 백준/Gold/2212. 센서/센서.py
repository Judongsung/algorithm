from sys import stdin
import heapq

class MaxHeap:
    def __init__(self, ):
        self.heap = []
    
    def push(self, value:int) -> None:
        heapq.heappush(self.heap, -value)
    
    def pop(self, ) -> int:
        return -heapq.heappop(self.heap)

def find_min_receivable_distance(sensor:int, center:int, sensors:list[int]) -> int:
    if center >= sensor or sensor == 1:
        return 0

    distance_heap = MaxHeap()
    sorted_sensors = sorted(sensors)
    min_receivable_distance = sorted_sensors[-1]-sorted_sensors[0]
    
    for i in range(sensor-1):
        distance = sorted_sensors[i+1]-sorted_sensors[i]
        distance_heap.push(distance)
    
    for _ in range(center-1):
        max_distance = distance_heap.pop()
        min_receivable_distance -= max_distance
    
    return min_receivable_distance

sensor = int(stdin.readline().rstrip())
center = int(stdin.readline().rstrip())
sensors = list(map(int, stdin.readline().rstrip().split()))

result = find_min_receivable_distance(sensor, center, sensors)
print(result)