# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        l, r = 0, len(letters) - 1
        if letters[0] > target or letters[-1] <= target:
            return letters[l]

        while r >= l:
            mid = (l + r) // 2
            
            if letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return letters[l]
                

# Else kısmında istediğimiz sayıya eşit olunca l ondan 1 fazlası olabiliyor daha fazlası olamıyor ve r eksilmeye başlıyor ve l > r oluyor en sonunda.
# Olmayan rakamda da aynı şekilde oluyor.

print(Solution().nextGreatestLetter(['a', 'b', 'c', 'd'], 'a'))