
from unicodedata import digit


class Solution(object):
    def plusOne(self, digits):
        totalDigit = pow(10, len(digits)-1)
        arrToInt = 0

        for i in digits:            
            arrToInt += int(i * totalDigit)
            totalDigit /= 10

        arrToInt += 1

        res = []
        for i in str(arrToInt):
            res.append(int(i))

        return res


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        res = [0] * (len(digits) + 1)
        res[0] = 1
        return res

print(Solution().plusOne([1,2,3,4]))
print(Solution().plusOne([9,9,9]))
print(Solution().plusOne([1,9,7,9]))