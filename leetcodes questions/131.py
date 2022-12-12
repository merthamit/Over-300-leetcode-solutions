class Solution(object):
    def partition(self, s):
        res, part = [], []
        
        def dfs(i):
            if len(s) <= i:
                res.append(part[:])
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)

        return res
        
    def isPalindrome(self, word, l, r):
        while r > l:
            if word[l] != word[r]: return False
            l, r = l+1, r-1

        return True