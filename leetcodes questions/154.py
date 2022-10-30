class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        res = float('inf')

        while r >= l:
            while r > l and nums[l] == nums[l+1]: l += 1
            while r > l and nums[r] == nums[r-1]: r -= 1
            
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res
            
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res



# Benim çözdüğüm
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        
        while r > l:
            mid = (l + r) // 2
            
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1
        
        return nums[l]
    
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while r > l:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid
            else:
                r -= 1
        
        return nums[l]

# Burayı iki çatı şeklinde düşün birinci çatı ikinci çatıdan yüksek olmak zorunda birinci çatı artıyor ikinci çatıda birincinin son sayısının en fazla bir düşüğü
# olacak şekilde artıyor. Bunu neetcode da adamdan gördüm bir videosunda anlatıyordu oradan aklıma geldi.

print(Solution().findMin([4,4,4,4,5,6,7,0,1,2]))
print(Solution().findMin([2,0,1,1,1]))
print(Solution().findMin([1,0,1,1,1]))
print(Solution().findMin([6,0,1,2]))
