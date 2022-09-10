# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def replaceElements(self, arr):
        rightMax = -1
        for i in range(len(arr)-1, -1, -1):
            newMax = max(arr[i], rightMax)
            arr[i] = rightMax
            rightMax = newMax
        
        return arr

 # Bu çok önemli kağıtla kalemle çiz ve tekrar et.           
            

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
        
print(Solution().replaceElements([17,18,5,4,6,1]))