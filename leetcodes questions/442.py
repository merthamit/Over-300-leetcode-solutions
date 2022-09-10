# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findDuplicates(self, nums):
        result = []
        for n in nums:
            i = abs(n) - 1
            if nums[i] < 0:
                result.append(i + 1)
            nums[i] *= -1
        return result


print(Solution().findDuplicates([5,4,6,7,9,3,10,9,5,6]))