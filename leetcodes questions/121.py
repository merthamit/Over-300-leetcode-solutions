# Kadena's algorithm or Kadane's algorithm
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution:
    def maxProfit(self,prices):
        l, r = 0, 1
        res = 0

        while len(prices) > r:
            currProfit = prices[r] - prices[l]

            if prices[r] > prices[l]:
                res = max(currProfit, res)
            else:
                l = r
            
            r += 1

        return res

# Neden else kısmında l = r yapıyoruz çünkü burada l ' den daha küçük bir rakam buluyoruz. Ve bu da ileriki r ' lerde bize daha küçük sayı
# bulmamızı sağlıyor.

print(Solution().maxProfit([7,3,5,1,6,4]))