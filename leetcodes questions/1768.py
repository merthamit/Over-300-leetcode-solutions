# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = []
        i, j = 0, 0
        
        while len(word1) > i or len(word2) > j:
            if len(word1) > i:
                res.append(word1[i])
                i += 1
            if len(word2) > j:
                res.append(word2[j])
                j += 1
        
        return ''.join(res)


print(Solution().mergeAlternately('ab','pqrs'))


# Benim çözdüğüm
# O(n^2) Time Complexity çünkü res += string oluyor burada stringi yeniden tanımlayıp kendi içinde loopa sokuyor
class Solution2(object):
    def mergeAlternately(self, word1, word2):
        res = ''
        i, j = 0, 0

        while len(word1) > i and len(word2) > j:
            res += word1[i]         
            res += word2[j]
            i += 1
            j += 1

        if i == len(word1):
            res += word2[j:]
        elif j == len(word2):
            res += word1[i:]

        return res      



        
