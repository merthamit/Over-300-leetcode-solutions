# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def lemonadeChange(self, bills):
        tens, fives = 0, 0

        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10:
                fives -= 1
                tens += 1
            elif tens > 0:
                tens -= 1
                fives -= 1
            else:
                fives -= 3

            if fives < 0:
                return False
        
        return True

print(Solution().lemonadeChange([5,5,5,10,10,20]))
print(Solution().lemonadeChange([5,5,10,10,20]))
