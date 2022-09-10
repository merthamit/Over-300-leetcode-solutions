# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])

        for idx, i in enumerate(nums):
            l, r = idx+1, len(nums) - 1

            while r > l:
                sums = i + nums[l] + nums[r]

                if abs(sums - target) < abs(res - target):
                    res = sums

                if sums > target:
                    r -= 1
                elif sums < target:
                    l += 1
                else:
                    return sums

        return res

            

print(Solution().threeSumClosest([-1, 2, 1, -4], 1))