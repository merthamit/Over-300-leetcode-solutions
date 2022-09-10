# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def thirdMax(self, nums):
        firstMax, secondMax, thirdMax = float('inf'), float('inf'), float('inf')
        for i in nums:
            if firstMax == i or secondMax == i or thirdMax == i: continue

            if firstMax == float('inf') or firstMax < i:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = i
            elif secondMax == float('inf') or secondMax < i:
                thirdMax = secondMax
                secondMax = i
            elif thirdMax == float('inf') or thirdMax < i:
                thirdMax = i

        if thirdMax == float('inf'): return firstMax
        return thirdMax


print(Solution().thirdMax([2,2,3,1]))