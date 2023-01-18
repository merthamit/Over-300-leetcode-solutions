class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 0
        res = 0
        
        while len(prices) > r:
            currProfit = prices[r] - prices[l]
            
            if currProfit > 0:
                res += currProfit
                l = r
            else:
                l = r 
                
            r += 1
        
        return res
            
class Solution(object):
    def maxProfit(self, prices):
        res = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        
        return res