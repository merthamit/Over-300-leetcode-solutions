# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def totalFruit(self, fruits):
        start, maxLen = 0, 0
        d = {}

        for end in range(len(fruits)):
            d[fruits[end]] = end
            if len(d) >= 3:
                minVal = min(d.values())
                d.pop(fruits[minVal])
                start = minVal + 1
            maxLen = max(maxLen, (end - start + 1))
        return maxLen





print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))