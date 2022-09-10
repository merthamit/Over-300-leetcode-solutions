# Benim çözdüğüm
class Solution(object):
    def sortColors(self, nums):
        l = 0
        i = 0
        while i < 3:
            for r in range(len(nums)):
                if nums[r] != i:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
            l = 0
            i += 1
        return nums


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def sortColors(self, nums):
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while r >= i:
            if nums[i] == 0:
                swap(i, l)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            
            i += 1

        return nums

            



# 0-> Kırmızı 1-> beyaz 2-> mavi
# Sıralanışı 0, 1, 2 ---- kırmızı, beyaz, mavi

print(Solution().sortColors([2,0,2,1,1,0]))
print(Solution().sortColors([1,2,0]))