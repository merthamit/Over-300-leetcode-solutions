# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def reverseString(self, s):
        l, r = 0, len(s) - 1

        while r > l:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r- 1
        
        return s


            
        

print(Solution().reverseString(["h","e","l","l","o"]))