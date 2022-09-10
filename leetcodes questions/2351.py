# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def repeatedCharacter(self, s):
        hashTable = set()
        for c in s:
            if c in hashTable:
                return c
            hashTable.add(c)

print(Solution().repeatedCharacter("abccbaacz"))

# Benim çözdüğüm
class Solution2(object):
    def repeatedCharacter(self, s):
        hashTable = {}

        for c in s:
            hashTable[c] = 1 + hashTable.get(c, 0)
            if hashTable[c] > 1:
                return c

  
  
