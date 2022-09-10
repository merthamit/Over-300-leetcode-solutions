

from typing import Counter


class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        count = 0

        left, right = 0, len(nums) - 1

        while right > left:
            sum = nums[left] + nums[right]

            if sum > k:
                right -= 1
            elif sum < k:
                left += 1
            else:
                count += 1
                right -= 1
                left += 1


        return count


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def maxOperations(self, nums, k):
        output = 0
        seen = set()
        c = Counter(nums)

        for x in nums:
            if x not in seen and k - x in c:
                if x == k - x:
                    output += c[x] // 2
                else:
                    output += min(c[x], c[k - x])
                
                seen.add(x)
                seen.add(k - x)

        return output



print(Solution().maxOperations([3,1,4,3,3],6))
print(Solution().maxOperations([1,2,3,4],5))
