# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findTargetSumWays(self, nums, target):
        dp = {}
        
        def backTrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = (backTrack(i+1, total+nums[i]) + backTrack(i+1, total-nums[i]))
            
            return dp[(i, total)]
            
        return backTrack(0, 0)
# 4,4 ve 4,2 --> 5,3 returnluyor fakat 4,4 ve 4,2 3,3 ün içine hiçbirşey returnlamıyor. O yüzden en sonunda reeturn dp[(i, total )] yapıyoruz.
