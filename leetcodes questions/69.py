# Benim çözdüğüm
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def mySqrt(self, x):
        l, r = 1, x
        res = 0

        while r >= l:
            mid = (l + r) // 2
            sqr = mid * mid

            if sqr > x:
                r = mid - 1
            elif sqr < x:
                res = mid
                l = mid + 1
            else:
                return mid

        return res

# Benim çözdüğüm
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def mySqrt(self, x):
        l, r = 1, x
        res = 0

        while r >= l:
            mid = (l + r) // 2
            sqr = mid * mid

            if sqr > x:
                r = mid - 1
            else:
                res = mid
                l = mid + 1

        return res


print(Solution().mySqrt(25))

# Bildiğimiz binary search burada olay şu diyelim ki rakam 25 olsun sonuç 5 bu sonuç 25 içinde olduğu için binary searche uygun.
# sqr eğer x den büyükse demek ki bu rakam büyük bir rakam küçültmek lazım. eğer sqr x den küçükse bu rakam küçük bir rakam büyütmek lazım ve resi burada yazıyoruz
# çünkü bu rakam 40 gibi bir sayı olsaydı burada bulunacaktı sqr > x gibi bir durumda bulamazsın burada bulursun döngü tekrarlanıp buraya geldiğinde
# tekrar res = mid yapıyoruz ve res'in en büyüğünü bulmuş oluyoruz. else durumunda hiç bir statement'a eşit değilse direk mid i dönderiyoruz bu şekilde bulunuyor.



