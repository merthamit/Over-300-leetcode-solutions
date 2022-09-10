# Çözüm sayısı 0 | Hedef 5 çözüm

class Solution(object):
    def intersection(self, nums1, nums2):
        nums1Hash, nums2Hash = set(), set()

        for i in nums1:
            nums1Hash.add(i)

        for i in nums2:
            nums2Hash.add(i)
        
        result = []
        for n in nums1Hash:
            if n in nums2Hash:
                result.append(n)
        
        return result

print(Solution().intersection([1,1,2,5],[2,1,2]))