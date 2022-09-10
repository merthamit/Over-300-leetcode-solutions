# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxNum = max(candies)

        for idx, i in enumerate(candies):
            if i + extraCandies >= maxNum:
                candies[idx] = True
            else:
                candies[idx] = False

        return candies

print(Solution().kidsWithCandies([2,3,5,1,3],3))