class Solution(object):
    def find132pattern(self, nums):
        stack, currMin = [], nums[0]
        
        for n in nums[1:]:
            while stack and stack[-1][0] <= n:
                stack.pop()
                
            if stack and stack[-1][0] > n and stack[-1][1] < n: return True
            
            stack.append((n, currMin))
            currMin = min(currMin, n)

        return False
                