from sys import stdin


MOD = 1000

def simulate_bug(adult: int, retire: int, death: int, n: int) -> int:
    total = [0]*(n+1)
    breed_change = [0]*(n+1)
    breed = 0
    total[0] = 1
    if adult <= n:
        breed_change[adult] = 1
    if retire <= n:
        breed_change[retire] = -1
    if death <= n:
        total[death] = -1
    
    for i in range(n):
        breed = (breed+breed_change[i]) % MOD

        if i+adult <= n:
            breed_change[i+adult] = (breed_change[i+adult]+breed) % MOD

        if i+retire <= n:
            breed_change[i+retire] -= breed
        
        if i+death <= n:
            total[i+death] -= breed
        
        total[i+1] = (total[i+1]+total[i]+breed) % MOD
    
    return (total[n]+breed+breed_change[n]) % MOD
            
adult, retire, death, n = map(int, stdin.readline().rstrip().split())
print(simulate_bug(adult, retire, death, n))