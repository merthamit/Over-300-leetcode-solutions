# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def searchMatrix(self, matrix, target):
        ROWS, COLS = len(matrix), len(matrix[0])
        row, col = ROWS-1, 0

        while row >= 0 and col < COLS:
            if matrix[row][col] == target: return True

            if matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        
        return False


print(Solution().searchMatrix(

[
[1 ,4, 7, 11,15],
[2, 5, 8, 12,19],
[3, 6, 9, 16,22],
[10,13,14,17,24],
[18,21,23,26,30]
]
, 1))