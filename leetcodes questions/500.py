# Benim çözdüğüm
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findWords(self, words):
        a = set('asdfghjklASDFGHJKL')
        b = set('zxcvbnmZXCVBNM')
        c = set('qwertyuiopQWERTYUIOP')
        result = []
        for i in words:
            firstChar = i[0]
            if firstChar in a:
                if self.isAll(i, a): result.append(i)
            elif firstChar in b:
                if self.isAll(i, b): result.append(i)
            elif firstChar in c:
                if self.isAll(i, c): result.append(i)
        return result

    def isAll(self, s, keyboard):
        for i in s:
            if i not in keyboard: return False
        return True


print(Solution().findWords(['a','b']))
print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))