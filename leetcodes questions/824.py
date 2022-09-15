# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def toGoatLatin(self, sentence):
        vowel = set(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'))
        arrSentence = sentence.split(' ')

        for idx, i in enumerate(arrSentence):
            if i[0] not in vowel:
                arrSentence[idx] += arrSentence[idx][0]
                arrSentence[idx] = arrSentence[idx][1:]
            
            arrSentence[idx] += 'ma'
            arrSentence[idx] += ((idx + 1) * 'a')
        
        return ' '.join(arrSentence)


print(Solution().toGoatLatin("I speak Goat Latin"))