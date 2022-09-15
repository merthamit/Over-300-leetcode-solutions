# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def sortedSquares(self, nums):
        left, right = 0, len(nums) - 1
        res = []

        while right >= left:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                res.append(nums[left] * nums[left])
                left += 1
            else:
                res.append(nums[right] * nums[right])
                right -= 1
        
        return res[::-1]

# Karışık arraylerde işe yaramaz her iki tarafı sıralı olmak zorunda...
# Eğer sıralamayı ilk başta küçükten büyüye yaparsak şu sonuç ortaya çıkıyor bir sonraki rakamın en küçük sayı olup olmadığını bilmiyorsun ama büyükten
# küçüğe doğru sıraladığında bunu biliyorsun. örn -50, -49 -48, 0, 5, 10, 100  [50, 49, 48... ] böyle gidiyor hani 10? yok çünkü dediğim gibi.
              
print(Solution().sortedSquares([-4,-1,0,3,10]))
print(Solution().sortedSquares([-5,-3,-2,-1]))