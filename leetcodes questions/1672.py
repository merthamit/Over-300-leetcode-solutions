class Solution(object):
    def maximumWealth(self, accounts):
        max = 0
        for idx, i in enumerate(accounts):
            total = 0
            for j in i:
                total += j
            if total > max:
                max = total
        return max
    
# Space o(mn)
# Time o(n^2)

a = Solution()
print(a.maximumWealth([[1,5], [7,3], [3,5]]))