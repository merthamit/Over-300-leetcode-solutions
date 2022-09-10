from typing import Counter
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findAnagrams(self, s, p):
        countTarget = Counter(p)

        windowStart, letterCount, result = 0, {}, []

        for windowEnd in range(len(s)):
            letterCount[s[windowEnd]] = 1 + letterCount.get(s[windowEnd], 0)

            if windowEnd - windowStart >= len(p) - 1:
                if countTarget == letterCount:
                    result.append(windowStart)

                letterCount[s[windowStart]] -= 1
                if letterCount[s[windowStart]] == 0:
                    del letterCount[s[windowStart]]
                
                windowStart += 1
        
        return result



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

print(Solution().findAnagrams('cbaebabacd', 'abc'))
