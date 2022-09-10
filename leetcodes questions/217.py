class Solution(object):
    def containsDuplicate(self, nums):
        hashTable = set()

        for i in nums:
            if(i in hashTable):
                return True
            hashTable.add(i)
        
        return False
        
result = Solution()

print(result.containsDuplicate([1,2,3,4]))