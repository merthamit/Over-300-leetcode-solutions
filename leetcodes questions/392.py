# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0, 0
        
        while len(s) > i and len(t) > j:
            if len(s) > i and s[i] == t[j]:
                i += 1
            j += 1
        
        return len(s) == i
            