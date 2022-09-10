# Benim çözdüğüm
class Solution2(object):
    def intersect(self, nums1, nums2):
        nums1Set, nums2Set = {}, {}

        for i in nums1:
            nums1Set[i] = 1 + nums1Set.get(i, 0)
        
        for i in nums2:
            nums2Set[i] = 1 + nums2Set.get(i, 0)

        result = []
        for n in nums1Set:
            if n in nums2Set:
                for i in range(min(nums2Set[n], nums1Set[n])):
                    result.append(n)
        return result

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def intersect(self, nums1, nums2):
        i, j = 0, 0
        nums1, nums2 = sorted(nums1), sorted(nums2)
        output = []

        while len(nums1) > i and len(nums2) > j:
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                output.append(nums1[i])
                i += 1
                j += 1

        return output


print(Solution().intersect([1,2,2,1], [2,2]))        
