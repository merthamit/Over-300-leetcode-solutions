# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findDuplicate(self, nums):
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: return slow

# Floyd's algorithm diye geçiyor.
# Yukarıdaki fast aslında durdurmak için daha hızlı gideceği yere varıyor ve slow gelince break oluyor.
# slow2 de aynı mantıkta break etmek için kullanılıyor aslında tekrarlanan sayı daha önceden bulunuyor.

# print(Solution().findDuplicate([2,3,1,4,2,5]))
print(Solution().findDuplicate([1,2,4,3,5,4]))
# print(Solution().findDuplicate([2,2,2,2,2]))