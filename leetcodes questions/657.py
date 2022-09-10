# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def judgeCircle(self, moves):
        origin = [0, 0]

        for i in moves:
            if i == 'U':
                origin[0] += 1
            elif i == 'D':
                origin[0] -= 1
            elif i == 'L':
                origin[1] += 1
            elif i == 'R':
                origin[1] -= 1
        
        return True if origin[0] == 0 and origin[1] == 0 else False

print(Solution().judgeCircle("LDRRLRUULR"))
