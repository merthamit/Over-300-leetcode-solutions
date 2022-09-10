# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def longestConsecutive(self, nums):
        numset = set(nums)
        longest = 0

        for i in numset:
            if (i - 1) not in numset:
                length = 0
                while (i + length) in numset:
                    length += 1
                    longest = max(longest, length)
        return longest 

print(Solution().longestConsecutive([4,100,1,2,200,3]))