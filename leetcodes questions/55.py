# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def canJump(self, nums):
        goal = len(nums) - 1

        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False



# print(Solution().canJump([2,3,1,0,4]))
# print(Solution().canJump([2,5,0,0,0,0,0]))
# print(Solution().canJump([2,0]))
print(Solution().canJump([3, 1, 2, 0, 10]))