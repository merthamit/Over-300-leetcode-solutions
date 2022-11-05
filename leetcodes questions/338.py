# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def countBits(self, n):
        dp = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] =  1 + dp[i - offset]
            
        return dp
#https://content.instructables.com/ORIG/FSM/GFJW/IKYG9OLC/FSMGFJWIKYG9OLC.png?auto=webp&frame=1&md=319f7cdfd3af91962f90665331095e6b
# offsetin ne işe yaradığını hatırla
# her 2 ** n de bir sayıda tek bir tane 1 oluyor o yüzden offset ayarlamak gerekiyor