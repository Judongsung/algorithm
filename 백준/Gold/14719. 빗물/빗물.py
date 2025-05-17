LEFT:int = 0
RIGHT:int = 1

def solution(h:int, w:int, heights:list[int]) -> int:
    result:int = 0
    memo:list[list] = [[0, 0] for _ in range(w)]
    
    memo[0][LEFT] = heights[0]
    memo[w-1][RIGHT] = heights[w-1]

    for i in range(w-1):
        memo[i+1][LEFT] = max(heights[i], memo[i][LEFT])

    for i in range(w-1, 0, -1):
        memo[i-1][RIGHT] = max(heights[i], memo[i][RIGHT])

    for i in range(w):
        left, right = memo[i]
        height = heights[i]
        result += max(min(left, right)-height, 0)
    
    return result

h, w = list(map(int, input().split()))
heights = list(map(int, input().split()))

result = solution(h, w, heights)
print(result)