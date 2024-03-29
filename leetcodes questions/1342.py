class Solution(object):
    def numberOfSteps(self, num):
        count = 0

        while num:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            count += 1
        
        return count
        
print(Solution().numberOfSteps(14))
