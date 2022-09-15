# Benim çözdüğüm
from collections import Counter


class Solution2(object):
    def topKFrequent(self, nums, k):
        countNums = {}
        result = []

        for idx, i in enumerate(nums):
            countNums[i] = 1 + countNums.get(i, 0)

        sortedArr = sorted(countNums.items(), key=lambda x: x[1], reverse=True)       
        for i in range(0, k):
            result.append(sortedArr[i][0])
        
        return result

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k: return res
        
        return res

# It's O(n) because the inner loop won't be executing n times every single time. In total the inner loop will execute n times.
#​ @NeetCode  Yea, but for worst-case time complexity it will be O(n^2), right?
# @Tanmesh Mishra  No, the inner loop will only run up to n times in total, where n is the length of nums. This solution really is O(n) in the worst case.

print(Solution().topKFrequent([1,1,1,2,2,3],2))