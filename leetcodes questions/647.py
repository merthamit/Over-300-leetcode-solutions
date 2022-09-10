# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def countSubstrings(self, s):
        res = 0

        for i in range(len(s)):
            l = r = i

            while l >= 0 and len(s) > r and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and len(s) > r and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res

print(Solution().countSubstrings("aaab"))