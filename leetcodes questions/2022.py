# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def construct2DArray(self, original, m, n):
        if m * n != len(original): return []

        twoD = [[] for _ in range(m)]

        row, col = 0, 0

        while len(original) > col:
            if len(twoD[row]) < n:
                twoD[row].append(original[col])
                col += 1
            else:
                row += 1
        
        return twoD



print(Solution().construct2DArray([1,2,3,4], 2, 2))