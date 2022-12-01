class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        tmp, rvrsX = x, 0
        
        while x:
            rvrsX = rvrsX * 10 + x % 10
            x //= 10
        
        return tmp == rvrsX
    
        