class Solution(object):
    def countGoodSubstrings(self, s):
        count = 0

        for x, y, z in zip(s, s[1:], s[2:]):
            if x != y and x != z and y != z:
                count += 1
        
        return count

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def countGoodSubstrings(self, s):
        letterFreq = {}
        count, start = 0, 0

        for end in range(len(s)):
            letterFreq[s[end]] = 1 + letterFreq.get(s[end], 0)

            if (end - start + 1) >= 3:
                if len(letterFreq) == 3:
                    count += 1

                letterFreq[s[start]] -= 1
                if letterFreq[s[start]] == 0:
                    letterFreq.pop(s[start])
                
                start += 1

        return count

 
print(Solution().countGoodSubstrings("aababcabc"))