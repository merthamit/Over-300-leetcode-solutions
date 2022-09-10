# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while r >= l:
            while r > l and nums[l] == nums[l+1]: l += 1
            while r > l and nums[r] == nums[r-1]: r -= 1

            mid = (l + r) // 2
            if nums[mid] == target: return True

            if nums[mid] < nums[r]:
                if nums[mid] < target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] > target and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return False

print(Solution().search([2,5,6,0,1,2], 5))
print(Solution().search([1,0,2,3,4], 3))


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while r >= l:
            while l < r and nums[r] == nums[r-1]:
                r -= 1
            while l < r and nums[l] == nums[l+1]:
                l += 1
            mid = (l + r) // 2

            if nums[mid] == target:
                return True
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return False


        

# print(Solution().search([2,5,6,0,1,2], 5))
# print(Solution().search([1,0,2,3,4], 3))