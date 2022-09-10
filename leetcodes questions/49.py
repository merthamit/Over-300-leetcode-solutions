from collections import defaultdict


class Solution2(object):
    def groupAnagrams(self, strs):
        uTable = {}
        for i in strs:
            sortedI = ''.join(sorted(i))
            if sortedI in uTable:
                uTable[sortedI].append(i)
            else:
                uTable[sortedI] = [i]

        return uTable.values()


# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
        
        return res.values()

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
