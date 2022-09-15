# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def myPow(self, x, n):
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            print(res, x, n)
            res = helper(x * x, n // 2)

            return res * x if n % 2 else res
        
        res = helper(x, abs(n))

        return res if n >= 0 else 1 / res
        
print(Solution().myPow(2, 5))



