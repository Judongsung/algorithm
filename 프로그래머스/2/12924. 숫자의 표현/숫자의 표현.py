def solution(n):
    answer = 1
    
    for i in range(2, n//2+2):
        num = (i*(i+1))/2
        if num <= n and (n-num)%i == 0:
            answer += 1
    return answer