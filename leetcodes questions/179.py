class Solution(object):
    def largestNumber(self, nums):
        for i, n in enumerate(nums):
            nums[i] = str(n)
            
        def largest(a, b):
            if a + b > b + a:
                return 0
            elif a + b < b + a:
                return 1
            else:
                return 0

        # Bubble Sort    
        for x in range(len(nums)-1, -1, -1):
            for y in range(x):
                if largest(str(nums[y]), str(nums[y+1])):
                    nums[y], nums[y+1] = nums[y+1], nums[y]
                    
        return str(int(''.join(nums)))
        
def cmp_to_key(): return
class Solution(object):
    def largestNumber(self, nums):
        for i, n in enumerate(nums):
            nums[i] = str(n)
            
        def largest(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
        
        res = sorted(nums, key=cmp_to_key(largest))
        return str(int(''.join(res)))