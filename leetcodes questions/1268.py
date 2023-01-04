class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.futureWords = []
        
    def addWord(self, word):
        curr = self
        curr.futureWords.append(word)
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.futureWords.append(word)

        
        curr.endOfWord = True
        curr.fullyWord = word


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        root = TrieNode()
        res = []
        
        for product in products:
            root.addWord(product)
        
        finish = False
        for s in searchWord:
            if s not in root.children or finish:
                res.append([])
                finish = True
                continue
            root = root.children[s]
            k, subres = 3, []
            root.futureWords.sort()
            for i in root.futureWords:
                if k == 0: break
                subres.append(i)
                k -= 1
                
            res.append(sorted(subres))
            
        return res

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res = []
        
        l, r = 0, len(products) - 1
        
        for i in range(len(searchWord)):
            c = searchWord[i]
            
            while r >= l and (len(products[l]) <= i or products[l][i] != c): l += 1
            while r >= l and (len(products[r]) <= i or products[r][i] != c): r -= 1

            
            res.append([])
            remain = r - l + 1
            for j in range(min(3, remain)):
                res[-1].append(products[l+j])
        
        return res