# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm

class Solution(object):
    def findDisappearedNumbers(self, nums):
        for n in nums:
            i = abs(n) - 1
            nums[i] = abs(nums[i]) * -1
        
        result = []
        for idx, i in enumerate(nums):
            if i > 0: result.append(idx+1)
        
        return result


print(Solution().findDisappearedNumbers([1,2,4,4,2,6]))

# i de neden abs(n) diye bir şey var çünkü bir sonraki sayı - li bir sayı olabilir index - li bir sayı olmaz olur ama list range yetmeyebilir hata alabiliriz.
# nums[i] = ... bölümündeki abs(nums[i]) oradaki abs de ise daha önceden o index - olmuş olabilir tekrardan - ile çarpmak onu artı yapabilir. o yüzden abs() var.
# neden i+1 yapıyoruz çünkü index 0,1,2 gittiği için örneğin 2.indexdeki sayı yok yani üç 2+1 = 3 sayıyı buluyoruz.



# Benim çözdüğüm 1
class Solution(object):
    def findDisappearedNumbers(self, nums):
        hashTable = {}
        result = []

        for i in nums:
            hashTable[i] = 1
        
        for i in range(1, len(nums) + 1):
            if(i not in hashTable):
                result.append(i)

        return result


# Benim çözdüğüm 2
class Solution(object):
    def findDisappearedNumbers(self, nums):
        hashTable = set()
        
        for i in nums:
            hashTable.add(i)

        for i in range(1,len(nums) + 1):
            if(i in hashTable):
                hashTable.remove(i)
            else:
                hashTable.add(i)
        
        return hashTable
