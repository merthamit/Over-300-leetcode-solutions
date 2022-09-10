# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        stonesHash, count = set(), 0

        for i in jewels:
            stonesHash.add(i)

        for i in stones:
            if i in stonesHash: count += 1

        return count

print(Solution().numJewelsInStones("aA","aAAbbbb"))