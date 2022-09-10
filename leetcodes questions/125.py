# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while right >= left:
            while right > left and not self.isInAscii(s[right]):
                right -= 1
            while right > left and not self.isInAscii(s[left]):
                left += 1

            if s[right].lower() != s[left].lower(): return False

            left, right = left+1, right-1

        return True

    
    def isInAscii(self, l):
        return (
            ord('0') <= ord(l) <= ord('9') or
            ord('A') <= ord(l) <= ord('Z') or
            ord('a') <= ord(l) <= ord('z')
        )



print(Solution().isPalindrome("A man, a plan, a canal: Panama"))

# Benim çözdüğüm
class Solution2(object):
    def isPalindrome(self, s):
        newLetter = ''
        for char in s:
            newLetter += char.lower() if char.isalnum() else ''
        
        left, right = 0, len(newLetter) - 1
        while right >= left:
            if(newLetter[left] != newLetter[right]):
                return False
            left += 1
            right -= 1
        return True



