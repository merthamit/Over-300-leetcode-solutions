class Solution2(object):
    def isAnagram(self, s, t):
        hashTable = {}
        for idx, i in enumerate(s):
            if(i in hashTable):
                hashTable[i] += 1
            else:
                hashTable[i] = 1
        for idx, i in enumerate(t):
            if(i in hashTable):
                hashTable[i] -= 1
                if(hashTable[i] == 0):
                    del hashTable[i]
            else:
                return False
        return len(hashTable) == 0

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT


print(Solution().isAnagram('sellam','llseam'))