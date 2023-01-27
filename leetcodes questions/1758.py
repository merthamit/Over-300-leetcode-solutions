class Solution(object):
    def minOperations(self, s):
        n = len(s)
        
        alt1, alt2 = '', ''
        for i in range(len(s)):
            alt1 += '0' if i % 2 else '1'
            alt2 += '1' if i % 2 else '0'
        
        diff1, diff2 = 0, 0
        for i in range(len(s)):
            if alt1[i] != s[i]: diff1 += 1
            elif alt2[i] != s[i]: diff2 += 1
        
        return min(diff1, diff2)