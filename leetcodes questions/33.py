# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while r >= l:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1

# Bu bir binary search sorusu. Klasik, mid eğer target'a eşitse mid'in indexini dönderiyoruz.
# Burada düşüneceğimiz 3 farklı array grubu var. Birincisi küçükten büyüğe giden array örn:[1,2,3,4,5,6,7,8] (sıralı)
# İkincisi büyükten küçüğe giden array örn: [8,9,10,|0|,1,2,3,4,5] ama küçüklerden biri midin solunda
# Üçüncüsü büyükten küçüğe [4,5,6,7,|8|,1,2,3] ama büyüklerden biri sağda
# Buradaki püf nokta sağda veya solda diğer küçük veya büyük sub arrayin diğer arrayin içinde rakamı olup olmadığı yukarıda belirttim.
# Yukarıda gösterdiğim 0 ve 8 dediğime örnek olarak gösterilebilir.
# İlk başta mid > l yapıyoruz ki bu liste sıralı mı değil mi onu öğreniyoruz. Eğer sıralıysa normal binary search yapıyoruz fakat:
# l ile mid arasında o sayı olmayabilir. Bu yüzden l > targetdan kontrolü yapıyoruz eğer büyükse demek ki bu sayı arrayin solunda değil sağında.
# Şimdi ise liste sıralı değilse yani l > mid demek ki büyük sayılar solda ve belki küçük sayıların biri solda olabilir o yüzden target < mid ya da 
# target > r ' den büyükse demek ki rakam sol tarafta
# Sonrasında işlem tekrar ediliyor ve bitiyor.


print(Solution().search([8,9,0,1,2,3,4], 2))
print(Solution().search([4,5,6,7,8,1,2,3], 8)) # 2 ve 8 dene 
print(Solution().search([7,8,9,1,2,3,4], 2)) # 2 ve 8 dene
# ---->>>>> sağında sadece bir rakam mid den fazla olabilir örneğin 8. eğer rakam sayısını arttırırsan sağdan mid bir sağ kayar soldan arttırırsan bir kez sol kayar
print(Solution().search([4,5,6,7,8,0,1,2], 0)) # 0, 8 ve 4 dene
print(Solution().search([8,9,10,3,4,5,6], 4))
print(Solution().search([7,8,9,1,2,3,4,5,6], 6))