# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def titleToNumber(self, columnTitle):
        multiple = 1
        col = 0
        
        for i in range(len(columnTitle)-1, -1, -1):
            col += multiple * (ord(columnTitle[i]) - 64)
            multiple *= 26
            
        return col

class Solution(object):
    def titleToNumber(self, columnTitle):
        col = 0
        
        for i in columnTitle:
            col = col * 26 + (ord(i) - 64)
        
        return col

# Burayı şöyle düşün 1 ler 10 lar 100 ler 1000 ler basamağı olarak düşün.
# Basamak olarak 10*10 olarak atlamıyor 26*26 olarak atlıyor
# Ord da ise sayının hangi rakama geldiğini buluyoruz