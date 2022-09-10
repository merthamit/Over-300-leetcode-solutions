# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def countPrimes(self, n):
        if n <= 2: return 0

        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(n):
            if primes[i]:
                for j in range(i * 2, n, i):
                    primes[j] = 0
        return sum(primes) 

print(Solution().countPrimes(1000))