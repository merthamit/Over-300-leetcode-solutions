# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution:
    def arrayPairSum(self, nums):
        arr = [0] * 20002
        for i in nums: arr[i + 10001] += 1
        curr = res = 0

        for i in range(len(arr)):
            while arr[i] != 0:
                if curr % 2 == 0: res += i - 10001
                curr += 1
                arr[i] -= 1
        
        return res

# Burada zaten ilk baştaki sayılar küçük olduğu için curr çiftleri alıyoruz yani ilk gelen sayı sonra 3. gelen sayı hep küçük soldakiler hep küçük




print(Solution().arrayPairSum([6,2,6,5,1,2]))
