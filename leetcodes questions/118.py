class Solution(object):
    def generate(self, numRows):
        output = []
        for i in range(numRows):
            output.append([1] * (i+1))
        
        for i in range(len(output)-1):
            addIdx, addTotal = -1, 0  
            l, r = 0, 0

            while r < len(output[i]):
                addTotal += output[i][r]
                if (r - l + 1) == 2:
                    addIdx = r
                    output[i+1][addIdx] = addTotal 
                    addTotal -= output[i][l]
                    l = r
                r += 1 
        
        return output


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def generate(self, numRows):
        res = [[1]]

        for i in range(numRows-1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1])+1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res

print(Solution().generate(5))

