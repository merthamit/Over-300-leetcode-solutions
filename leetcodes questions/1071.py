class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1: return ''
        def gcd(a, b):
            if b == 0:
                return a
            
            return gcd(b, a % b)
        
        gcdVal = gcd(len(str1), len(str2))
        return str2[:gcdVal] 