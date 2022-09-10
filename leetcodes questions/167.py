# Benim çözdüğüm


class Solution2(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        sum = 0
        while right >= left:
            sum = numbers[right] + numbers[left]
            if(sum == target):
                return [left+1, right+1]
            if(target < sum):
                right -= 1
            if(target > sum):
                left += 1

# Çözüm sayısı 4 | Hedef 5 çözüm
# Adamın çözdüğü
class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        sum = 0

        while right >= left:
            sum = numbers[right] + numbers[left]

            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left+1, right+1]



print(Solution().twoSum([2,7,11,15],9))