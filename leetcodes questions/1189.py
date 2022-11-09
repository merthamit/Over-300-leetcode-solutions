from collections import Counter
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def maxNumberOfBalloons(self, text):
        countTxt = Counter(text)
        letterFreq = Counter('balloon')
        m = float('inf')
        for s, c in letterFreq.items():
            if s not in countTxt: return 0
            
            m = min(m, countTxt[s] // c)
        
        return m if m != float('inf') else 0