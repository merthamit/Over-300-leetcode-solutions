class Solution(object):
    def getRow(self, rowIndex):
        rows = [[1]]

        for i in range(1, rowIndex+1):
            temp = [1 for _ in range(i + 1)]
            for j in range(1, len(temp)-1):
                temp[j] = rows[-1][j] + rows[-1][j-1]
            rows.append(temp)
        return rows[-1]

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def getRow(self, rowIndex):
        row = [1]
        for _ in range(rowIndex):
            row.append(1)
            for j in range(len(row) - 2, 0, -1):
                row[j] += row[j-1]
        return row


print(Solution().getRow(3))


[1, 1]
[1, 1, 1, 1]
[1, 4, 6, 4, 1]