# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def twoSum(self, nums, target):
        hashTable = {}
        for idx, i in enumerate(nums):
            minusEl = target - i 
            if i in hashTable:
                return [hashTable[i], idx]
            hashTable[minusEl] = idx
        
            
        




print(Solution().twoSum([2,7,11,15], 9))