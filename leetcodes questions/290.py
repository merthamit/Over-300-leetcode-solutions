class Solution(object):
    def wordPattern(self, pattern, s):
        def isSame(word):
            lookup = {}
            output = []
            i = 0

            for w in word:
                if w in lookup:
                    output.append(lookup[w])
                else:
                    i += 1
                    lookup[w] = i
                    output.append(lookup[w])
            
            return output

        s = isSame(s.split(' '))

        pattern = isSame(pattern)

        return pattern == s

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split(' ')
        if len(s) != len(pattern): return False

        charToWord, wordToChar = {}, {}
        for c, w in zip(pattern, s):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False

            charToWord[c] = w
            wordToChar[w] = c

        return True 

# Daha önceden eşitlendiği için soruyor daha önceden eşitlediğin sayı w mi diye mesela


print(Solution().wordPattern('abba', 'dog cat cat dog'))