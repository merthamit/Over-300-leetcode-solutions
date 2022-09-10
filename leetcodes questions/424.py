# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def characterReplacement(self, s, k):
        count, res = {}, 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))
        
        return res


# Burada olay harflerin sayılması ve sayıldıktan sonra k dan büyükse sayılanlardan içinden az olanı o zaman l yi bir öne çekip sayıyoruz.


print(Solution().characterReplacement('ABABBA',2))