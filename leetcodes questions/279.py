import collections
class Solution(object):
    def numSquares(self, n):
        if n == 1: return 1
        visit = set()
        q = collections.deque()
        squares = []
        for i in range(1,n):
            if i * i == n:
                return 1
            if i * i < n:
                squares.append(i * i)
                q.append((i * i, 1))
        
        while q:
            lastNum, turn = q.popleft()
            for i in squares:
                mlt = lastNum + i

                if mlt == n: 
                    return turn + 1
                if mlt not in visit and n > mlt:
                    visit.add(mlt)
                    q.append((mlt, turn + 1))
        

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def numSquares(self, n):
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s

                if target - square < 0: break

                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]


print(Solution().numSquares(12))
# Deftere not aldın oraya bakabilirsin.
