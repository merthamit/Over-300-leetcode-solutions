# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for idx, i in enumerate(nums):
            if i in d and abs(d[i] - idx) <= k: return True
            d[i] = idx
        return False

print(Solution().containsNearbyDuplicate([1,2,3,1], 3))