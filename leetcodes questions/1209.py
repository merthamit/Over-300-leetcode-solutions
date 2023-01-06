class Solution(object):
    def removeDuplicates(self, s, k):
        if k <= 1: return ''
        
        stack, count = [], k
        for i in s:
            if stack and stack[-1][0] == i:
                _, rest = stack[-1]
                stack.append((i, rest-1))
                if not stack[-1][1]:
                    for _ in range(k):
                        stack.pop()
            else:
                stack.append((i, k-1))
                
        res = ''
        for a, b in stack:
            res += a
        return res

class Solution(object):
    def removeDuplicates(self, s, k):
        if k <= 1: return ''
        
        stack, count = [], 0
        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1] += 1
            else:
                stack.append([i, 1])
                
            if stack[-1][1] == k:
                stack.pop()
                
        res = ''
        for char, count in stack:
            res += (char * count)
            
        return res
    