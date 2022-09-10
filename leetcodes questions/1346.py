from typing import Counter


class Solution(object):
    def checkIfExist(self, arr):
        hashArr = Counter(arr)

        for i in arr:
            if i * 2 in hashArr:
                if i == 0 and hashArr[i] > 1:
                    return True
                elif i != 0:
                    return True

        return False
        
print(Solution().checkIfExist([10, 2, 5, 3]))