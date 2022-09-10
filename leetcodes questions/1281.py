# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def subtractProductAndSum(self, n):
        sum, product = 0, 1

        while n:
            digit = n % 10
            sum += digit
            product *= digit
            n //= 10
        
        return product - sum

print(Solution().subtractProductAndSum(234))
