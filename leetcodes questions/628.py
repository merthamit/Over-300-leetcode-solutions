# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def maximumProduct(self, nums):
        max1, max2, max3 = None, None, None
        min1, min2 = None, None

        for i in nums:
            if max1 == None or max1 < i:
                max3 = max2
                max2 = max1
                max1 = i
            elif max2 == None or max2 < i:
                max3 = max2
                max2 = i
            elif max3 == None or max3 < i:
                max3 = i
            
            if min1 == None or min1 > i:
                min2 = min1
                min1 = i
            elif min2 == None or min2 > i:
                min2 = i

        return max(max1 * max2 * max3, min1 * min2 * max1)

print(Solution().maximumProduct([-10, -9, -8, 3, 4]))