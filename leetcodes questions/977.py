# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def sortedSquares(self, nums):
        left, right = 0, len(nums) - 1
        res = []

        while right >= left:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                res.append(nums[left] * nums[left])
                left += 1
            else:
                res.append(nums[right] * nums[right])
                right -= 1
        
        return res[::-1]

# Karışık arraylerde işe yaramaz her iki tarafı sıralı olmak zorunda...
       
print(Solution().sortedSquares([-4,-1,0,3,10]))
print(Solution().sortedSquares([-5,-3,-2,-1]))