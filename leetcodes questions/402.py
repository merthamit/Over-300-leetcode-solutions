class Solution(object):
    def removeKdigits(self, num, k):
        if len(num) == k: return '0'
        stack = []
        
        for i in num:
            while stack and stack[-1] > i and k:
                stack.pop()
                k -= 1
                
            stack.append(i)
        
        while k:
            stack.pop()
            k -= 1
        
        return str(int(''.join(stack)))