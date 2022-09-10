# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def lengthOfLastWord(self, s):
        i, length = len(s) - 1, 0

        while s[i] == ' ':
            i -= 1

        while i >= 0 and s[i] != ' ':
            i -= 1
            length += 1

        return length

print(Solution().lengthOfLastWord('mert hamit koçer  '))
print(Solution().lengthOfLastWord('a'))
