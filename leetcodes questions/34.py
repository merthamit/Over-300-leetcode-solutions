from collections import deque
from turtle import right
# Benim çözdüğüm
class Solution(object):
    def searchRange(self, nums, target):
        if not nums: return [-1, -1]

        l, r = 0, len(nums) -1
        while r >= l:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                lTarget, rTarget = mid, mid
                while len(nums) - 1 > rTarget and nums[rTarget] == nums[rTarget+1]: rTarget += 1
                while lTarget > 0 and nums[lTarget] == nums[lTarget-1]: lTarget -= 1
                return [lTarget, rTarget]

        return [-1, -1]


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm

class Solution(object):
    def searchRange(self, nums, target):
        leftBin = self.binSearch(nums, target, True)
        rightBin = self.binSearch(nums, target, False)
        return [leftBin, rightBin]

    def binSearch(left, nums, target, leftBin):
        l, r = 0, len(nums) - 1
        i = -1

        while r >= l:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                i = mid
                if leftBin:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return i



print(Solution().searchRange([5,7,7,8,8,8,8,8,11], 8)) # --> 3, 7
print(Solution().searchRange([3,3,3], 3)) # --> 0, 2