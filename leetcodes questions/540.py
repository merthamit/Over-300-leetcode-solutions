# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def singleNonDuplicate(self, nums):
        l, r = 0, len(nums) - 1

        while r > l:
            mid = (l + r) // 2
            isEven = (r - mid) % 2 == 0

            if nums[mid] == nums[mid + 1]:
                if isEven:
                    l = mid + 2
                else:
                    r = mid - 1
            elif nums[mid] == nums[mid - 1]:
                if isEven:
                    r = mid - 2
                else:
                    l = mid + 1
            else:
                return nums[mid]

        return nums[l]

# Eğer mid == mid+1 e burada bu kontrolü yapıyoruz çünkü isEven da yaptığımız kontrol buraya girdikten sonra işe yarayacak.
# IsEven True ise demek ki mid+1 ile birlikte sağdaki sayılar tamamı çiftmiş ama beklenen tek olacaktı demek ki bizim sonucumuz burada l yi +2 arttırıyoruz
# çünkü mid+1 de aynı sayı +2 arttırıyoruz o yüzden. Eğer isEven çift değilse demek ki aradığımız sayı diğer tarafta r -1 yapıyoruz çünkü zaten mid+1 de bizim 
# bizim sayımız o yüzden 



# print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(Solution().singleNonDuplicate([1,1,2,2,3,3,4,8,8]))
# print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))
# print(Solution().singleNonDuplicate([1,1,2]))
