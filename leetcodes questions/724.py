# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def pivotIndex(self, nums):
        sums = sum(nums)
        leftSum = 0
        for idx, i in enumerate(nums):
            if sums - leftSum - i == leftSum: return idx
            leftSum += i
        return -1

print(Solution().pivotIndex([1,7,3,6,5,6]))

# [1,7,3,6,5,6] bu array'in pivotu 3. indexdir neden?
# Algoritmanın mantığı şu şekilde çalışıyor. İlk başta tüm sayıları topluyoruz ve leftSum'da sırasıyla topladığımız rakamları her defasında sums'dan çıkartıyoruz.
# Çünkü leftSum'da topladığımız sayıları sums'dan çıkartırsak geri kalan sayıların toplamını buluruz. E peki if statement'ta neden - nums[i] yapıyorsun?
# Çünkü o sayının da çıkması lazım ki sağ daki sayıların toplamını bulalım. Eğer zaten nums[i]' de çıkıp sonuç bulunuyorsa i. index pivottur.
# 1+7+3 = 5 + 6 = 27 - 13 - 6 = 11 tam olarak budur.


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# FEYNMAN TEKNİĞİ KULLANACAĞIM ARTIK 
# BİR KİŞİYE ANLATIR GİBİ KODUN NASIL ÇALIŞTIĞINI ANLATACAĞIM
# VE KODUN ALTINA YAZACAĞIM
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Saat 12 de başla. Gece saat 2:19 a kadar. Haftada 100 saat eder. 
# Elon Musk gibi ol. 
# Pomodoro tekniği kullan.
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
