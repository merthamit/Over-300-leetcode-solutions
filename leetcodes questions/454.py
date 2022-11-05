# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        res, d = 0, {}
        for n1 in nums1:
            for n2 in nums2:
                tmp = n1 + n2
                d[tmp] = 1 + d.get(tmp, 0)
        for n1 in nums3:
            for n2 in nums4:
                tmp = (n1 + n2)
                res += d.get(-tmp, 0)
        return res

# a + b + c + d = 0
# a + b = -(c + d)
# a + v = - c - d
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 
 

print(Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
