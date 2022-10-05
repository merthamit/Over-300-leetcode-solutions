
from unittest import result


class Solution2(object):
    def reversePrefix(self, word, ch):
        result = []
        left, right = 0, 0

        for idx, i in enumerate(word):
            if(i == ch):
                right = idx
                break
        for i in word: 
            result.append(i)
        
        while right >= left:
            tmp = result[right]
            result[right] = result[left]
            result[left] = tmp
            
            right -=1
            left +=1 
        
        return ''.join(map(str,result))


class Solution(object):
    def reversePrefix(self, word, ch):
        left, right = 0, 0

        for idx, i in enumerate(word):
            if i == ch:
                left = idx + 1
                right = idx
                break
        
        if left > right:
            result = []

            while right >= 0:
                result.append(word[right])
                right -= 1

            while left < len(word):
                result.append(word[left])
                left += 1

            return ''.join(result)

        return word 

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def reversePrefix(self, word, ch):
        res = []
        start = 0

        for i in range(len(word)):
            if word[i] == ch:
                start = i
                break

        if start == 0: return word

        for i in range(start, -1, -1):
            res.append(word[i])

        for i in range(start+1, len(word)):
            res.append(word[i])
        
        return ''.join(res)

print(Solution().reversePrefix('abcdefd', 'd'))
