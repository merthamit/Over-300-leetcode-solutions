# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def removeDuplicates(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l



# Burada r bir kontrol edici, l ise r nin koyulacağı yeri belirtiyor.

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))