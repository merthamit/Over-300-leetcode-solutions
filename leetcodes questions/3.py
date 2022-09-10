# Benim çözdüğüm
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashTable = {}
        maxLength = 0

        left, right = 0, 0

        while right < len(s):
            if s[right] in hashTable:
                left = hashTable[s[right]] +1
                right = left
                hashTable.clear()

            hashTable[s[right]] = right
            maxLength = max(maxLength, len(hashTable))
            right += 1
        
        return maxLength

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charset = set()
        l, res = 0, 0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, (r - l + 1))
        return res

# Left aslında başlangıç noktası demek.


print(Solution().lengthOfLongestSubstring('pwwke'))
print(Solution().lengthOfLongestSubstring('abcaklmn'))
print(Solution().lengthOfLongestSubstring('abcaaklmn'))
# print(Solution().lengthOfLongestSubstring('abcabcbb'))