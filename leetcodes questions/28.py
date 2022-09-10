class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1
# KMP ALGORITHM diye geçiyor ikiside
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def strStr(self, haystack, needle):
        if not needle: return ''
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle: return i
        return -1


print(Solution().strStr('hello', 'll'))