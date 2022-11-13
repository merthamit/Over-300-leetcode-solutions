# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm



# r > l şu işe yarıyor eğer [1] böyle bir şey verilirse çalıştırmıyor while döngüsünü ve l yi return ediyor 
class Solution(object):
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1

        while r > l:
            mid = (l + r) // 2

            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        
        return l


print(Solution().findPeakElement([1,2,1,3,2,0,4]))
print(Solution().findPeakElement([1,0,1,3,2,0,4]))
print(Solution().findPeakElement([1,2,3,0]))
