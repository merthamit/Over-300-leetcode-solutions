import collections

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r - l + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1

        return output


# print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
# print(Solution().maxSlidingWindow([1,-1], 1))

print(Solution().maxSlidingWindow([1,2,3,4,0,5], 3))
print(Solution().maxSlidingWindow([1,1,1,1,1,4,5], 6))
# print(Solution().maxSlidingWindow([1,-1], 1))