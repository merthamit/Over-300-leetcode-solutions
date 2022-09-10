from collections import defaultdict
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        a = defaultdict(list)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if a[r - c] and a[r - c][0] != matrix[r][c]: return False
                a[r - c].append(matrix[r][c])

        return True

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for r in range(len(matrix) - 1):
            for c in range(len(matrix[0]) - 1):
                if matrix[r][c] != matrix[r + 1][c + 1]: return False
        return True

print(Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))