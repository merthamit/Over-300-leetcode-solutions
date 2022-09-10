# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def addBinary(self, a, b):
        res = ''
        carry = 0

        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            aDigit = int(a[i]) if len(a) > i else 0
            bDigit = int(b[i]) if len(b) > i else 0 

            total = aDigit + bDigit + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2
        
        if carry:
            res = "1" + res
        
        return res

print(Solution().addBinary("110", "101"))

