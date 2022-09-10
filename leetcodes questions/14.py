# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ''

        for i in range(len(strs[0])):
            for s in strs:
                if len(s) == i or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        
        return res


print(Solution().longestCommonPrefix(["flower","flow",'fly']))