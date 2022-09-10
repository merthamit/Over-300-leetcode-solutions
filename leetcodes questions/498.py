from collections import defaultdict

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findDiagonalOrder(self, mat):
        twoD = defaultdict(list)

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                twoD[r+c].append(mat[r][c])
        
        res = []
        for i in twoD:
            if i % 2 == 1:
                for j in twoD[i]: res.append(j)
            else:
                for j in twoD[i][::-1]: res.append(j)
        
        return res
        


print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(Solution().findDiagonalOrder([[1,2]]))