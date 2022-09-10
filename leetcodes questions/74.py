# Benim çözdüğüm
from tkinter import N
from turtle import right


class Solution2(object):
    def searchMatrix(self, matrix, target):
        for i in matrix:
            lastItem = i[-1]

            if(lastItem >= target):
                leftIndex = 0
                rightIndex = len(i) - 1
                while leftIndex <= rightIndex:
                    middleIndex = (leftIndex + rightIndex) // 2
                    if(i[middleIndex] == target):
                        return True
                    if(i[middleIndex] < target):
                        leftIndex = middleIndex + 1
                    elif(i[middleIndex] > target):
                        rightIndex = middleIndex - 1
        return False


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def searchMatrix(self, matrix, target):
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS -1
        while bot >= top:
            row = (bot + top) // 2

            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        
        if not (top <= bot): return False

        l, r = 0, COLS -1
        row = (top + bot) // 2

        while r >= l:
            mid = (l + r) // 2

            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False


print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],7))

#Time complexity m log n