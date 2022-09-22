# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t): return False
        m1, m2 = {}, {}

        for a, b in zip(s, t):
            if a in m1 and m1[a] != b: return False
            if b in m2 and m2[b] != a: return False

            m1[a] = b
            m2[b] = a
        
        return True

print(Solution().isIsomorphic('egg', 'add'))

            