# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        word1Idx, word2Idx = 0, 0
        char1Idx, char2Idx = 0, 0

        while len(word1) > word1Idx and len(word2) > word2Idx:
            c1 = word1[word1Idx][char1Idx]
            c2 = word2[word2Idx][char2Idx]

            if c1 != c2: return False

            char1Idx += 1
            char2Idx += 1

            if char1Idx >= len(word1[word1Idx]):
                word1Idx += 1
                char1Idx = 0

            if char2Idx >= len(word2[word2Idx]):
                word2Idx += 1
                char2Idx = 0

        
        return len(word1) == word1Idx and len(word2) == word2Idx


print(Solution().arrayStringsAreEqual(["abc","d","def"],["abcddefg"]))