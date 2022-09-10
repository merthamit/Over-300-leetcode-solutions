# Benim çözdüğüm
class Solution2(object):
    def distributeCandies(self, candyType):
        hashTable = set()
        aliceEat = len(candyType) / 2
        result = 0

        for i in candyType:
            hashTable.add(i)
            result = aliceEat if len(hashTable) > aliceEat else len(hashTable)

        return result

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def distributeCandies(self, candyType):
        hashTable = set()
        aliceEat = len(candyType) / 2

        for i in candyType:
            hashTable.add(i)
        
        return min(len(hashTable), aliceEat)

print(Solution().distributeCandies([1,2,3,4,5,1])) 

# Alice toplamda len(candytype) / 2 yiyebiliyor yani 3 tane. Kaç çeşit şeker yiyebilir?