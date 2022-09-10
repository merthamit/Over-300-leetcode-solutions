from itertools import count
from typing import Counter
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def minWindow(self, s, t):
        if t == '': return ''

        countT, window = Counter(t), {}
        have, need = 0, len(countT)
        res, minLen = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < minLen:
                    res = [l, r]
                    minLen = (r - l + 1)
                
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l:r+1] if minLen != float('inf') else ''
        





print(Solution().minWindow('ADOBECODEBANC', 'ABC'))
print(Solution().minWindow('a', 'a'))