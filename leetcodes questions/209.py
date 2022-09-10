
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def minSubArrayLen(self, target, nums):
        l, total, res = 0, 0, float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(res, (r - l + 1))
                total -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0

print(Solution().minSubArrayLen(15,[5,1,3,5,10,7,4,9,2,8]))