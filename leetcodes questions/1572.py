class Solution(object):
    def diagonalSum(self, mat):
        max = 0
        for idx, i in enumerate(mat):
            if(idx == len(mat) -1 - idx):
                max = max + mat[idx][idx]
                continue
            max = max + mat[idx][idx] + mat[idx][(len(mat) -1) - idx]
        return max


# Space o(mn)
# Time o(n^2)

a = Solution()
print(a.diagonalSum([
            [1,2,3],
            [5,6,7],
            [8,4,9]]))

