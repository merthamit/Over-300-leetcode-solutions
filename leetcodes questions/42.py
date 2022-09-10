# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm

class Solution(object):
    def trap(self, height):
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while r > l:
            if rightMax > leftMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res


# Mesela diyelim r > l ve buradan su sızdırıyor demek yani bunu atla ve bir arttır eğer l < r olduğu sürece bir artacak en sonunda birbirinin sızmayyacağı
# yerleri hesaplayacak
# Her zaman algoritmada en kötü ne olabilir onu düşün mesela 0,0,0,4 olursa ne olur veya 4,0,0,0 olsa vs gibi...


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))