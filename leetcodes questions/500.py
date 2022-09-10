# Benim çözdüğüm
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findWords(self, words):
        a = set('asdfghjkl')
        b = set('zxcvbnm')
        c = set('qwertyuiop')
        result = []

        for i in words:
            if i[0].lower() in a:
                if self.isAll(i, a): result.append(i)
            if i[0].lower() in b:
                if self.isAll(i, b): result.append(i)
            if i[0].lower() in c:
                if self.isAll(i, c): result.append(i)
        
        return result



    def isAll(self, word, alp):
        for i in word.lower():
            if i not in alp:
                return False
        return True

print(Solution().findWords(['a','b']))
print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))