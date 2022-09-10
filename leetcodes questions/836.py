# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        return rec2[3] > rec1[1] and rec2[1] < rec1[3] and rec2[2] > rec1[0] and rec2[0] < rec1[2]

print(Solution().isRectangleOverlap([0,0,2,2],[1,1,3,3]))