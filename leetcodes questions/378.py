from bisect import bisect_right
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def kthSmallest(self, matrix, k):
        l, r, N = matrix[0][0], matrix[-1][-1], len(matrix)

        def less_k(m):
            cnt = 0
            for i in range(N):
                x = bisect_right(matrix[i], m)
                cnt += x
            return cnt

        while r > l:
            mid = (l + r) // 2

            if less_k(mid) < k:
                l = mid + 1
            else:
                r = mid 
        
        return l

# Eğer less mid > k büyük olursa bu sefer sayıyı küçültmeye başlıyor -1 -1 yaparak r = mid yapıyor yani. Bunun sebebi ise 
# evet less k bu conditiona uyuyor ama acaba daha küçük bir sayı var mı varsa sonuç o mantığıyla çalışıyor

print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))
# 1 5 9 10 11 12 13 13 15