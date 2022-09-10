class Solution(object):
    def dominantIndex(self, nums):
        maxNum, maxNumIdx = nums[0], 0
        
        for i in range(len(nums)):
            maxNumIdx = i if maxNum < nums[i] else maxNumIdx
            maxNum = max(nums[i], maxNum)
        
        for i in nums:
            if i != maxNum and i * 2 > maxNum: return -1
        
        return maxNumIdx


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def dominantIndex(self, nums):
        maxIndex, maxNum = -1, 0

        for i in range(len(nums)):
            if nums[i] >= maxNum * 2:
                maxNum = nums[i]
                maxIndex = i
            elif nums[i] > maxNum:
                maxNum = nums[i]
                maxIndex = -1
            elif nums[i] * 2 > maxNum:
                maxIndex = -1
        
        return maxIndex

print(Solution().dominantIndex([3,6,1,0]))
print(Solution().dominantIndex([1,2,3,4]))
print(Solution().dominantIndex([0,0,2,3]))