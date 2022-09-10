from turtle import right


class Solution(object):
    def reverseWords(self, s):
        strArr = s.split()

        for i in range(len(strArr)):
            strArr[i] = strArr[i][::-1]
        
        return ' '.join(strArr)
            

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution2(object):
    def reverseWords(self, s):  # O(n) both
        res = ''
        l = r = 0

        while len(s) > r:
            if s[r] != ' ':
                r += 1
            else:
                res += s[l:r+1][::-1]
                r += 1
                l = r
        
        res += ' '
        res += s[l:r][::-1]

        return res[1:]



print(Solution2().reverseWords("Let's take LeetCode contest"))