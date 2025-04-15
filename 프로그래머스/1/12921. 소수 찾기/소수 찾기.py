from math import sqrt

def solution(n):
    answer = 1
    primes = [2]
    
    for i in range(3, n+1, 2):
        sqrt_i = sqrt(i)
        for j in primes:
            if j > sqrt_i:
                answer += 1
                primes.append(i)
                break
            if i%j == 0:
                break
    
    return answer