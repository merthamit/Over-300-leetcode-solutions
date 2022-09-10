# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def reverseWords(self, s):
        res = []
        l, r = 0, 0

        while len(s) > l and len(s) > r:
            while len(s) > l and s[l] == ' ': l += 1
            r = l
            while len(s) > r and s[r] != ' ': r += 1
            res.append(s[l:r])
            l = r
        
        if res[-1] == '': res.pop()
        return ' '.join(res[::-1])
         
print(Solution().reverseWords("  hello world  "))
print(Solution().reverseWords("   fly me   to   the moon  "))
print(Solution().reverseWords("the sky is blue"))