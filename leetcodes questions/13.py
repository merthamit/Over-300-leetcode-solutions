class Solution(object):
    def romanToInt(self, s):
        roman = {
            "I" :1,
            "V" :5,
            "X" :10,
            "L" :50,
            "C" :100,
            "D" :500,
            "M" :1000,
        }
        
        res = 0
        
        for i in range(len(s)):
            if len(s) > i+1 and roman[s[i+1]] > roman[s[i]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
            
        return res