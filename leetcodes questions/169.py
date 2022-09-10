# Çözüm 2 Boyer moore algoritması olarak biliniyor
# En fazla sayılan eleman arrayin uzunluğunun yarısından büyük olmalı yoksa algoritma çalışmaz...

# Benim yaptığım -- Time Complexity: O(n), Space Complexity: O(n)
class Solution3(object):
    def majorityElement(self, nums):
        arrLenDivided = len(nums) // 2
        count = 0
        for idx, i in enumerate(nums):
            if(idx == 0 or nums[idx - 1] != nums[idx]):
                count = 1
            else:
                count += 1
            if(count > arrLenDivided):
                return i


# Çözüm sayısı 0 | Hedef 5 çözüm
# Çözüm 1 -- Time Complexity: O(n), Space Complexity: O(n)
class Solution2(object):
    def majorityElement(self, nums):
        hashTable = {}
        maxCount, result = 0, 0

        for i in nums:
            hashTable[i] = 1 + hashTable.get(i, 0)
            result = i if hashTable[i] > maxCount else result
            maxCount = max(maxCount, hashTable[i])
        
        return result

print(Solution2().majorityElement([2,2,1,1,2]))
        
        
        
        
    
        



# Çözüm sayısı 0 | Hedef 5 çözüm
# Çözüm 2 Boyer Moore Algoritması -- Time Complexity O(n), Space Complexity O(1)
# Algoritmayı çok sorgulama algoritma böyle işte herşeyi bilemezsin.
# En fazla sayılan eleman arrayin uzunluğunun yarısından büyük olmalı yoksa algoritma çalışmaz...
class Solution(object):
    def majorityElement(self,nums):
        count, result = 0, 0

        for i in nums:
            if count == 0:
                result = i
            
            count += 1 if result == i else -1
        
        return result

print(Solution().majorityElement([2,2,1,1,2]))



