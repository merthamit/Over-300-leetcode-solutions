# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def reverse(self, x):
        result = 0
        symbol = 1

        if x < 0:
            x = -x
            symbol = -1
        
        while x:
            result = result * 10 + x % 10
            x //= 10
        
        return result * symbol if result.bit_length() < 32 else 0

# İlk rakamın negatif bir sayı olup olmadığına bakıyoruz eğer negatif bir sayı ise symbol değişkenini eksi yapıp sayıyı pozitif yapıyoruz.
# Çünkü while döngüsünde yapacağımız işlemde negatif bir sayı olmaması gerekir. Yoksa döngüye girer veya yanlış sonuç verir çünkü -1 % 10 eşittir 0 olmayacak
# result da ise her rakam geldiğinde sayı bir rakam genişliyor ve sonuç ortaya çıkıyor.

print(Solution().reverse(123))