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