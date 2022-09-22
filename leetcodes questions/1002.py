from collections import Counter

# Benim çözdüğüm
class Solution(object):
    def commonChars(self, words):
        check = Counter(words[0])

        for word in words[1:]:
            letterCount = Counter(word)
            newCheck = {}
            for i in letterCount:
                if i in check:
                    newCheck[i] = min(letterCount[i], check[i])
            check = newCheck
        
        res = []
        for s, c in check.items():
            for i in range(c):
                res.append(s)
        return res

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def commonChars(self, words):
        check = list(words[0])
        for word in words:
            newCheck = []
            for i in word:
                if i in check:
                    newCheck.append(i)
                    check.remove(i)
            check = newCheck
        return check


# Neden check.remove(c) yapıyoruz çünkü belki s nin içinde 3 tane a, checkin için de 2 tane vardır o yüzden remove yapıyoruz.
print(Solution().commonChars(["bella","label","roller"]))
