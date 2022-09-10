# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def arrangeCoins(self, n):
        l, r = 1, n
        res = 1

        while r >= l:
            mid = (l + r) // 2
            row = (mid * (mid+1)) / 2

            if row > n:
                r = mid - 1
            else:
                l = mid + 1
                res = mid
        
        return res

print(Solution().arrangeCoins(7))

# Neden burada sadece else kısmında alıyoruz çünkü if kısmında alsaydık sayıyı aşmış olacak bir rakamda verilebilirdi. 
# Ayrıca basamak sayısı n sayısının içinde olduğu için binary search yapıyoruz.
# else kısmında res = mid yapmamın sebebi ise her defasında oraya giren sayı bir öncekinden büyük olacak veya eşit olacak o yüzden
# diyelim ki res 2 oldu ama 3 satırlık yer kaplıyor o coin o yüzden l yi 1 arttırıp tekrardan döngüye devam edip aynen else kısmına girilmeli.