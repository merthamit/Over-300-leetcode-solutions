# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findRestaurant(self, list1, list2):
        countWords1 = {i:idx for idx, i in enumerate(list1)}
        countWords2 = {i:idx for idx, i in enumerate(list2)}
        resultDict = {}

        for i in countWords1:
            if i in countWords2:
                resultDict[i] = countWords1[i] + countWords2[i]
        
        res = []
        for w in resultDict:
            if not res: res.append(w)
            elif resultDict[w] < resultDict[res[-1]]: res = [w]
            elif resultDict[w] == resultDict[res[-1]]: res.append(w)

        return res

print(Solution().findRestaurant(
["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Shogun","Burger King"]))
