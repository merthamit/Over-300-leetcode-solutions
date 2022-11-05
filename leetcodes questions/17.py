# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def letterCombinations(self, digits):
        if not digits: return []
        res = []
        digitToChar = {
            "2": 'abc',
            "3": 'def',
            "4": 'ghi',
            "5": 'jkl',
            "6": 'mno',
            "7": 'pqrs',
            "8": 'tuv',
            "9": 'wxyz'
        }
        
        def backTrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return 
            
            for c in digitToChar[digits[i]]:
                backTrack(i+1, currStr + c)
                
        backTrack(0, '')
        
        return res