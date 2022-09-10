# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isHappy(self, n):
        visit = set()

        while n not in visit:
            visit.add(n)

            n = self.sumNumber(n)

            if n == 1: return True
        
        return False
    
    
    def sumNumber(self, n):
        digit = 0
        output = 0

        while n:
            digit = n % 10
            output += digit * digit
            n //= 10
        
        return output

# Burada visit olmasının sebebi eğer sayı happy number değilse kendini tekrar ediyor. O yüzden visit var. 


print(Solution().isHappy(13))

