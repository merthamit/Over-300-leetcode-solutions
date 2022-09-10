# Çözüm sayısı 0 | Hedef 5 çözüm
# Benim çözdüğüm
class Solution(object):
    def decompressRLElist(self, nums):
        newArr = []

        for i in range(0, len(nums), 2):
            newArr += nums[i] * [nums[i+1]]
        
        return newArr

print(Solution().decompressRLElist([1,2,3,4]))

