class Solution(object):
    def getSum(self, a, b):
        mask = 0xffffffff

        while b & mask:
            
            tmpa = a
            a = a ^ b
            b = (tmpa & b) << 1
            
        return a & mask if b > mask else a