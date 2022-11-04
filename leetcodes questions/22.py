from collections import Counter


class Solution(object):
    def generateParenthesis(self, n):
        res = []
        
        def backTrack(curr):
            countC = Counter(curr)
            if countC['('] > n or countC[')'] > n: return 
            if countC[')'] > countC['(']: return
            if len(curr) == n * 2:
                res.append(curr)
                return
            
            backTrack(curr + '(')
            backTrack(curr + ')')
        
        backTrack('')
        
        return res


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
# Örüntü şöyle en sondaki ( işaretin gittiği yerlerin kombinasyonu aslında ((())) 3.deyken (()()) 4.ye geliyor en son nereye kadar giderse
class Solution(object):
    def generateParenthesis(self, n):
        res, stack = [], []
        
        def backTrack(openN, closedN):
            if openN == closedN == n:
                res.append(''.join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backTrack(openN + 1, closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(')')
                backTrack(openN, closedN + 1)
                stack.pop()
                
        backTrack(0, 0)
        
        return res
