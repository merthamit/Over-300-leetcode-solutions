# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
from typing import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        countS1, countS2 = {}, {}
        for i in range(len(s1)):
            countS1[s1[i]] = 1 + countS1.get(s1[i], 0)
            countS2[s2[i]] = 1 + countS2.get(s2[i], 0)
        
        if countS2 == countS1:
            return True
        
        windowStart = 0
        for windowEnd in range(len(s1),len(s2)):
            countS2[s2[windowEnd]] = 1 + countS2.get(s2[windowEnd], 0)
            countS2[s2[windowStart]] -= 1

            if countS2[s2[windowStart]] == 0:
                countS2.pop(s2[windowStart])
            
            windowStart += 1

            if countS2 == countS1:
                return True
        
        return False


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def checkInclusion(self, s1, s2):
        countTarget = Counter(s1)
        letterCount, start = {}, 0

        for end in range(len(s2)):
            letterCount[s2[end]] = 1 + letterCount.get(s2[end], 0)

            if (end - start + 1) >= len(s1):
                if letterCount == countTarget: return True

                letterCount[s2[start]] -= 1
                if letterCount[s2[start]] == 0:
                    letterCount.pop(s2[start])

                start += 1

        return False

print(Solution().checkInclusion('ab','dgfdgdfba'))


