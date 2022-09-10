# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def flipAndInvertImage(self, image):
        for i in image:
            left, right = 0, len(i) - 1

            while right >= left:
                if i[right] == i[left]:
                    i[right] = 1 - i[left]
                    i[left] = i[right]

                left, right = left+1, right-1

        return image


# Önce ters çevirip sonra sayıları 1 den 0 a veya 0 dan 1 e çevirmeye gerek yok. Eğer left ve right birbirine eşit ise zaten sayıları 1 den 0 a veya 0 dan 1 e çevirmek
# çok daha mantıklı olacaktır ve kısa sürecektir. Sayılar birbirine eşit değil ise zaten sayıları 1 den 0 a veya 0 dan 1 e çevirmeye gerek yok.
        
print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))

