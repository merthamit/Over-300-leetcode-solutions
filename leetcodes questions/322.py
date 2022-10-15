import collections


class Solution(object):
    def coinChange(self, coins, amount):
        if amount <= 0: return 0
        q = collections.deque()
        for i in coins:
            q.append((i, 1))
        visit = set()
        
        while q:
            coin, count = q.popleft()
            if coin == amount: return count
            for i in coins:
                total = coin + i
                if total not in visit and amount >= total:
                    visit.add(total)
                    q.append((total, count+1))
        return -1
                    
                
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)


        return dp[amount] if dp[amount] != amount + 1 else -1


print(Solution().coinChange([1,3,4,5], 7))