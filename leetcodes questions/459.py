# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def repeatedSubstringPattern(self, s):
        length = len(s) 

        def pattern(n):
            for i in range(0, length - n, n):
                if s[i: i + n] != s[i + n: i + (n * 2)]: return False
            return True


        for i in range(1, length // 2 + 1):
            if pattern(i): return True
        
        return False


print(Solution().repeatedSubstringPattern("abcabcabcabc"))

# "abcabc|abcabc"

# 8 e kadar gidecek 3 er 3 er atlayarak

# Alttaki for döngüsü 1 tane sayıyla başla bakim true olacak eğer trueyse true dönder diyor aslında tam olarak olay bu.