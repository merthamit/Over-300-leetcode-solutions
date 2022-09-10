class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3: return False
        i = 1
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]: return False
            if arr[i] < arr[i-1]:
                if i == 1: return False
                break
        
        for j in range(len(arr)-1, i-1, -1):
            if arr[j] == arr[j-1]: return False
            if arr[j] > arr[j-1]:
                return False
        return True

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3: return False
        isDec, isInc = False, False

        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                if isDec: return False
                isInc = True
            elif arr[i] > arr[i+1]:
                if not isInc: return False
                isDec = True
            else:
                return False
        
        if isDec and isInc: return True
        return False


print(Solution().validMountainArray([4,5,6,3,2,1]))
print(Solution().validMountainArray([3,5,5]))
                
