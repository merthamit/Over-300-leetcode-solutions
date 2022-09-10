# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findMin(self, nums):
        minRes = nums[0]
        l, r = 0, len(nums) - 1

        while r >= l:
            if nums[l] < nums[r]:
                minRes = min(minRes, nums[l])
                break

            mid = (l + r) // 2
            minRes = min(minRes, nums[mid])

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return minRes

            


# Tüm seçeneklere bak ve nasıl çalıştığını öğren.
# Örneğin [1,2,3,4,5], [3,4,5,1,2], [4,5,0,1,2,3] [6,1,2,3,4] [3,4,5,6,1,2]  [4,5,6,1,2,3] de nasıl çalışıyor bak bunuda chunk et çünkü        

print(Solution().findMin([3,4,5,1,2])) 
print(Solution().findMin([3,4,5,6,1,2])) 
print(Solution().findMin([4,5,0,1,2,3])) 
print(Solution().findMin([6,1,2,3,4])) 
print(Solution().findMin([1,2,3,4,5])) 
