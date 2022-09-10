# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def repeatedNTimes(self, nums):
        hashTable = set()

        for i in nums:
            if i in hashTable:
                return i
            hashTable.add(i)

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution2(object):
    def repeatedNTimes(self, nums):
        return (sum(nums) - sum(set(nums))) // (len(nums) // 2 - 1)

print(Solution2().repeatedNTimes([1,2,3,3]))
print(Solution2().repeatedNTimes([2,1,2,5,3,2]))