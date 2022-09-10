# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def heightChecker(self, heights):
        currHeight = 0
        freq = [0] * 101
        res = 0

        for i in heights:
            freq[i] += 1
        
        for i in range(len(heights)):
            while not freq[currHeight]: currHeight += 1
            
            if currHeight != heights[i]: res += 1
    
            freq[currHeight] -= 1

        return res



# Bunu queue olarak düşünebilirsin sırada iki var o yüzden freq i arttırıyoruz.
                    

print(Solution().heightChecker([3,2,2,4,5]))
print(Solution().heightChecker([1,2,3,4,5]))


class Solution(object):
    def heightChecker(self, heights):
        sortedHeights = sorted(heights)

        count = 0
        for i in range(len(heights)):
            if heights[i] != sortedHeights[i]:
                count += 1

        return count
        

# print(Solution().heightChecker([1,1,4,2,1,3]))