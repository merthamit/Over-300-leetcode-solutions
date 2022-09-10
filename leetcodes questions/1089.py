# Çözüm sayısı 0 | Hedef 5 çözüm
# Adamın çözdüğü O(n^2) time complexity
class Solution(object):
    def duplicateZeros(self, arr):
        q = []

        for idx, n in enumerate(arr):
            if n == 0:
                q.append(n)
                q.append(n)
            else:
                q.append(n)

            first = q.pop(0)
            arr[idx] = first

        return arr

# Benim çözdüğüm O(n) Time complexity
class Solution(object):
    def duplicateZeros(self, arr):
        q = []
        i = 0

        for idx, n in enumerate(arr):
            if n == 0:
                q.append(n)
                q.append(n)
            else:
                q.append(n)

            first = q[i]
            arr[idx] = first
            i += 1

        return arr
                                

print(Solution().duplicateZeros([1,0,2,3,0,4,5,0]))