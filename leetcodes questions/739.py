# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                sIndex, sTemp = stack.pop()
                res[sIndex] = i - sIndex
            stack.append([i, t])
        
        return res


print(Solution().dailyTemperatures([50,44,47,45,61,62]))