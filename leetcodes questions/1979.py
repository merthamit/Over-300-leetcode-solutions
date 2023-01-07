class Solution(object):
    def findGCD(self, nums):
        maxNum, minNum = nums[0], nums[1]
        for i in nums:
            maxNum = max(maxNum, i)
            minNum = min(minNum, i)
            
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        return gcd(maxNum, minNum)
        