# Benim çözdüğüm
class Solution2(object):
    def firstPalindrome(self, words):
        result = ''

        for i in words:
            left, right = 0, len(i) - 1

            while right >= left:
                if i[right] != i[left]:
                    result = ''
                    break
                else:
                    result = i
            
                left, right = left+1, right-1
            
            if result == i:
                return result

        return result

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution:
    def firstPalindrome(self, words):
        for word in words:
            if self.isPalindrome(word):
                return word
        return ''

    def isPalindrome(self, word):
        l,r = 0, len(word) - 1

        while r >= l:
            if word[l] != word[r]:
                return False
            l, r = l+1, r-1        
        return True

print(Solution().firstPalindrome(["abc","car","ada","racecar","cool",'aaba']))


