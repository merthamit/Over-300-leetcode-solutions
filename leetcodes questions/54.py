# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def spiralOrder(self, matrix):
        output = []
        left, right = 0, len(matrix[0])
        top, bot = 0, len(matrix)


        while left < right and bot > top:
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1

            for i in range(top, bot):
                output.append(matrix[i][right-1])
            right -= 1

            if not (top < bot and left < right): break

            for i in range(right-1, left-1, -1):
                output.append(matrix[bot-1][i])
            bot -= 1

            for i in range(bot-1, top-1, -1):
                output.append(matrix[i][left])
            left += 1
        
        return output
            


        

print(Solution().spiralOrder([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]))
# print(Solution().spiralOrder([[3],[2]]))
print(Solution().spiralOrder([
 [11,22,33,44]
,[55,66,77,88]
,[99,31,12,23]]))