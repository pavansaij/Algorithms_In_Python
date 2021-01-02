def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    
    primes = []
    for p in range(n + 1): 
        if prime[p]: 
            primes.append(p)
            
    return primes

p = SieveOfEratosthenes(4000000)