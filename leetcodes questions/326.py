class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0: return False
        if n % 3 != 0: return False if n != 1 else True
        
        return self.isPowerOfThree(n / 3)

class Solution(object):
    def isPowerOfThree(self, n):
        m = 3 ** 19
        
        return n > 0 and m % n == 0