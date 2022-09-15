from typing import Counter
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findAnagrams(self, s, p):
        res, countS, countP = [], {}, Counter(p)
        start = 0

        for end in range(len(s)):
            countS[s[end]] = 1 + countS.get(s[end], 0)

            if (end - start + 1) >= len(p):
                if countS == countP: res.append(start)

                countS[s[start]] -= 1
                if countS[s[start]] == 0:
                    countS.pop(s[start])

                start += 1
        
        return res



print(Solution().findAnagrams('cbaebabacd', 'abc'))

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s): return []

        countS, countP = {}, {}
        for i in range(len(p)):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countP[p[i]] = 1 + countP.get(p[i], 0) 

        res = [0] if countS == countP else []
        l = 0

        for r in range(len(p), len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)

            countS[s[l]] -= 1
            if countS[s[l]] == 0:
                countS.pop(s[l])
            l += 1

            if countS == countP:
                res.append(l)
        
        return res

