class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        nums2Hash, res = {}, []
        for idx, i in enumerate(nums2):
            nums2Hash[i] = idx
            
        for i in nums1:
            res.append(self.getGreater(i, nums2Hash[i], nums2))
            
        return res
    
    def getGreater(self, i, idx, arr):
        for j in range(idx+1, len(arr)):
            if arr[j] > i: return arr[j]
        return -1

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        nums1Idx = { n: i for i, n in enumerate(nums1) }
        res = [-1] * len(nums1)
        
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and stack[-1] < curr:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = curr
                
            if curr in nums1Idx:
                stack.append(curr)
        
        return res