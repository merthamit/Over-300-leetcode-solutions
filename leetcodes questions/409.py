# Adamın Çözdüğü 1
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def longestPalindrome(self, s):
        hashTable = {}
        result = 0

        for i in s:
            hashTable[i] = 1 + hashTable.get(i, 0)

        for n in hashTable.values():
            result += int(n / 2) * 2

            if result % 2 == 0 and n % 2 == 1:
                result += 1
            
        return result
         
print(Solution().longestPalindrome("abbbccc"))
# n / 2 yaptığında diyelim sayı 1 olsun int(1/2) * 2 = 0 aşağıya iniyor kontrol ediyor result çiftse ve sayı tekse resulta 1 ekle diyor
# n / 2 tekrar yapıyor sayı 1 olsun ... = 0 yine ama bu sefer kontrol ettiğinde result tek bir sayı artık bir eklemiyor
# n / 2 sayı bu sefer 3 olsun int(3/2) * 2 = 2 result = 3 oluyor ve bu sayede 

# Adamın Çözdüğü 2
class Solution(object):
    def longestPalindrome(self, s):
        hashTable = {}
        result = 0
        isOdd = False
        for i in s:
            hashTable[i] = hashTable.get(i,0) + 1

        for i in hashTable.values():
            if(i % 2 == 0):
                result += i
            else:
                isOdd = True
                result += i - 1
        
        if(isOdd):
            result += 1
        return result
