# Benim çözdüğüm
from cgitb import lookup
from unittest import result


class Solution2(object):
    def findAndReplacePattern(self, words, pattern):
        def replaceWord(word):
            hashCount = {}
            count = ['' for i in range(len(word))]
            
            for idx, i in enumerate(word):
                hashCount[i] = idx

            for idx, i in enumerate(word):
                count[idx] = hashCount.get(i, 0)
            
            return count
    
        firstPattern = replaceWord(pattern)
        result = []
        for word in words:
            wordPattern = replaceWord(word)
            print(wordPattern)
            if wordPattern == firstPattern:
                result.append(word)
        
        return result

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def replaceWord(word):
            output = []
            lookup = {}
            i = 0

            for c in word:
                if c in lookup:
                    output.append(lookup[c])
                else:
                    i += 1
                    lookup[c] = i
                    output.append(lookup[c])
            
            return output

        result = []
        pattern = replaceWord(pattern)
        for w in words:
            if replaceWord(w) == pattern:
                result.append(w)

        return result
        
# print(Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], 'abb'))

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution3(object):
    def findAndReplacePattern(self, words, pattern):
        def check(s, p):
            m1, m2 = {}, {}
            for a, b in zip(s, p):
                if a not in m1: m1[a] = b
                if b not in m2: m2[b] = a

                if m1[a] != b or m2[b] != a:
                    return False
            
            return True

        res = []
        for w in words:
            if check(w, pattern):
                res.append(w)
        
        return res

print(Solution3().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], 'abb'))








        