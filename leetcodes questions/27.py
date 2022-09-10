# Benim çözdüğüm
class Solution2(object):
    def removeElement(self, nums, val):
        l = 0
        count = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
            else:
                count += 1


        return len(nums) - count

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
# if bölümüne girdiği zamanlar sayıyor kaç tane 2 olup olmadığını
class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
        
print(Solution().removeElement([3,5,1,2,9,3,4],2))