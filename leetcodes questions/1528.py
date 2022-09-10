# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def restoreString(self, s, indices):
        res = [''] * len(indices)

        for idx, i in enumerate(indices):
            res[i] = s[idx]

        return ''.join(res)


print(Solution().restoreString('codeleet', [4,5,6,7,0,2,1,3]))
