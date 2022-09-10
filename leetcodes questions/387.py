class Solution(object):
    def firstUniqChar(self, s):
        hashTable = {}
        res = len(s)

        for idx, i in enumerate(s):
            if i not in hashTable:
                hashTable[i] = idx
            else:
                hashTable[i] = len(s)
        
        for i in hashTable.values():
            res = min(res, i)


        return res if len(s) > res else -1



# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def firstUniqChar(self, s):
        hashTable = {}

        for i in s:
            hashTable[i] = 1 + hashTable.get(i, 0)
        
        for idx, i in enumerate(s):
            if hashTable[i] == 1: return idx

        return -1        


print(Solution().firstUniqChar('leetcode'))
print(Solution().firstUniqChar('aabb'))