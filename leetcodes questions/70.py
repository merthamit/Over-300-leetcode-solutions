# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def climbStairs(self, n):
        one, two = 1, 1

        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp
        
        return one

print(Solution().climbStairs(5))