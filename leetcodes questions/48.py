# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def rotate(self, matrix):
        l, r = 0, len(matrix) - 1

        while r >= l:
            for i in range(r - l):
                top, bot = l, r

                topLeft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bot - i][l]

                matrix[bot - i][l] = matrix[bot][r - i]

                matrix[bot][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topLeft

            l, r = l+1, r-1

        return matrix


print(Solution().rotate([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))

