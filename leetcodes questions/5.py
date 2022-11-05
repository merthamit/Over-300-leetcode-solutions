class Solution(object):
    def longestPalindrome(self, s):
        maxLen, res = 0, [-1, -1]
        
        for i in range(len(s)):
            l = r = i

            # Burad oddlu olan palindrome yani tek sayı içeren palindrome yani aba veya aacaa gibi
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res = res if maxLen > (r - l + 1) else [l, r]
                maxLen = max(maxLen, (r - l + 1))
                l -= 1
                r += 1
            # Bura even palindrome yani çift sayı içeren aabb gibi aa gibi ccddcc gibi
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res = res if maxLen > (r - l + 1) else [l, r]
                maxLen = max(maxLen, (r - l + 1))
                l -= 1
                r += 1
        
        l, r = res
        return s[l:r+1]
            

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def longestPalindrome(self, s):
        maxLen, res = 0, [-1, -1]
        
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    res = [l, r]
                    maxLen = r - l + 1
                l -= 1
                r += 1
                
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    res = [l, r]
                    maxLen = r - l + 1
                l -= 1
                r += 1
        
        l, r = res
        return s[l:r+1]