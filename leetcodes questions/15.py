# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums) -1
            while r > l:
                sums = nums[i] + nums[l] + nums[r]

                if sums < 0:
                    l += 1
                elif sums > 0:
                    r -= 1
                else:
                    result.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while r > l and nums[l] == nums[l-1]:
                        l += 1
        
        return result

print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([-2,0,0,2,2]))
