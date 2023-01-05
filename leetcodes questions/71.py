class Solution(object):
    def simplifyPath(self, path):
        stack = []
        curr = ''
        
        for c in path + '/':
            if c == '/':
                if curr == '..':
                    if stack: stack.pop()
                elif curr != '' and curr != '.':
                    stack.append(curr)
                curr = ''
            else:
                curr += c
                
        return '/' + '/'.join(stack)

class Solution(object):
    def simplifyPath(self, path):
        stack = []
        curr = ''
        
        for i in path + '/':
            if i == '/':
                if curr and curr != '.' and curr != '..':
                    stack.append(curr)
                else:
                    if stack and curr == '..': stack.pop()
                        
                curr = ''
            else:
                curr += i
        
        return '/' + '/'.join(stack)
                
                
                
                
        # '/home/../'