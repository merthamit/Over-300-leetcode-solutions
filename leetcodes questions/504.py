# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def convertToBase7(self, num):
        if num == 0: return '0'
        symbol = 1
        if num < 0:
            symbol = -1
            num = -num
        
        res = ''
        while num:
            digit = str(num % 7)
            res = digit + res
            num //= 7

        return str(int(res) * symbol)
            
print(Solution().convertToBase7(-10))

