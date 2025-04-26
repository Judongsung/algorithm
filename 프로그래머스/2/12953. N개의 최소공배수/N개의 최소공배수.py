from collections import Counter

def solution(arr):
    lcm_counter = Counter()
    sieve = [True for i in range(max(arr)+1)]
    sieve[0] = False
    sieve[1] = False
    
    for i in range(2, len(sieve)):
        if sieve[i]:
            for j in range(i+1, len(sieve)):
                if sieve[j] and j%i == 0:
                    sieve[j] = False
            
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    
    for num in arr:
        for prime in primes:
            prime_count = 0
            while num%prime == 0:
                prime_count += 1
                num /= prime
            if lcm_counter[prime] < prime_count:
                lcm_counter[prime] = prime_count
    
    lcm = 1
    for prime in lcm_counter:
        lcm *= prime**lcm_counter[prime]
    
    return lcm