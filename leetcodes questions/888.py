# Çözüm sayısı 0 | Hedef 5 çözüm

class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        aliceSum, bobSum, bobHash = 0, 0, set()

        for a in aliceSizes:
            aliceSum += a

        for b in bobSizes:
            bobSum += b
            bobHash.add(b)

        delta = (bobSum - aliceSum) / 2
        
        for i in aliceSizes:
            if i + delta in bobHash:
                return [i, int(i + delta)]

# Bu formül alice ve bob'un ihtiyaç duyduğu sayıyı belirtiyor örneğin alice +1 ihtiyaç duyarken bob - 1 duyuyor
# Deltayı anla ve bitir.

print(Solution().fairCandySwap([4,4,2],[5,4,3]))