# Benim çözdüğüm
from turtle import right


class Solution2(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        maxSum = 0

        while right > left:
            rangeCount = right - left 
            
            if height[right] >= height[left]:
                maxSum = max(maxSum, rangeCount * height[left])
                left += 1
            else:
                maxSum = max(maxSum, rangeCount * height[right])
                right -= 1


        return maxSum

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        res = 0

        while right > left:
            area = (right - left) * min(height[left], height[right])
            res = max(area, res)

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        
        return res

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))