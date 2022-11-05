from bisect import bisect_left


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm 
class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        # BURAYI YAPTIN YARIN DİĞERİNİ ANLA YAP @@@@@@@@@@@@@@
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                       
        return max(dp)


class Solution:
    def lengthOfLIS(self, nums):
        dp = []
        for n in nums:
            ind = bisect_left(dp, n)
            if ind == len(dp):
                dp.append(n)
            else:
                dp[ind] = n

        return len(dp)