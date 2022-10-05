# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findKthLargest(self, nums, k):
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p < k:
                return quickSelect(p + 1, r)
            elif p > k:
                return quickSelect(l, p - 1)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)           


# Burada denilmek istenen şey şu diyelim ki en büyük ikinci sayıyı arıyoruz quick sort yaparak bulabiliriz fakat diyelim ki solda işimiz yok solu
# tekrardan sıralamaya gerek yok çünkü aradığımız rakam sağda sadece sağı sıralasak yeter tekrar bunu recursiona sokup en sonnunda sayıyı buluyoruz.
print(Solution().findKthLargest([3,2,1,5,6,4], 2))
# print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
