class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n:
            res += n % 2
            n //= 2
            
        return res

class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n:
            res += 1
            n = n & (n-1)        
        return res

class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n:
            res += n % 2
            n = n >> 1     
        return res