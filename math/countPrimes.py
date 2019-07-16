def countPrimes(n):
    prime_list=[1]*n
    for i in range(2,n):
        if prime_list[i]:
            j=i*i
            while j<n:
                prime_list[j]=0
                j=j+i
    return sum(prime_list[2:])

print(countPrimes(2))

def countPrimes(self, n):
    if n < 3:
        return 0
    primes = [1] * n
    primes[0] = primes[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [0] * len(primes[i * i: n: i])
    return sum(primes)
