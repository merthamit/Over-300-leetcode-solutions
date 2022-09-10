# Benim çözdüğüm
class Solution2(object):
    def minEatingSpeed(self, piles, h):
        count, idx, eatingCount = 0, 0, 1

        while len(piles) > idx:
            calc = piles[idx] / eatingCount
            count += int(-(-calc // 1))
            idx += 1

            if count > h:
                eatingCount += 1
                idx = 0
                count = 0
        return eatingCount


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm

class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        res = right

        while right >= left:
            mid = (left + right) // 2
            hours = 0

            for p in piles:
                hours += ((p - 1) // mid + 1)
            
            if hours <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res


# Neden min yapıyoruz çünkü mid in bir büyüğü dahada küçük bir hours ortaya çıkartacak o yüzden
# Yukarı doğru yuvarlamak gerekiyor çünkü aşağıya yuvarlarsak 3/2 diyelim 1 ama 2 saat geçmesi lazım hepsini yiyebilmesi için         
# mid aslında bölen sayı yanı koko nun yemesi gereken sayı

print(Solution().minEatingSpeed([3,6,7,11], 8))

# Saat başı en az kaç tane muz yemeli ki 8 saatte hepsini bitirsin.
