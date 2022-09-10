# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1

            last -= 1
        

        while n > 0:
            nums1[last] = nums2[n-1]
            last, n = last-1, n-1
        
        return nums1

print(Solution().merge([1,2,3,4,5,6], 3, [-3,-2,-1], 3))