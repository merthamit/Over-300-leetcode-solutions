# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def singleNumber(self, nums):
        res = 0

        for i in nums:
            res = i ^ res
        
        return res

# Şu anlık bilmem gereken biri hariç diğer sayılar iki kez görünüyorsa bu algoritma kullanılır ve tek geçen eleman bulunur.



# 4 | 0 -> 4  // 100 | 0 --> 100--> 4
# 1 | 4 -> 5  // 1 | 100 --> 101--> 5
# 2 | 5 -> 7  // 10 | 101 --> 111--> 7
# 1 | 7 -> 6  // 1 | 111 --> 110--> 6
# 2 | 6 -> 4  // 10 | 110 --> 100--> 4

# XOR 
# 0 0 --> 0
# 1 1 --> 0
# 0 1 --> 1
# 1 0 --> 1



print(Solution().singleNumber([4,1,2,1,2]))
