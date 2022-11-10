class Solution(object):
    def sumNumbers(self, root):
        if not root: return 0
        res = [0]
        def dfs(root, val):
            if not root: return
            
            val = val * 10 + root.val
            
            if not root.left and not root.right: res[0] += val
            
            dfs(root.left, val)
            dfs(root.right, val)
            
        dfs(root, 0)
        return res[0]

class Solution(object):
    def sumNumbers(self, root):
        if not root: return 0
        def dfs(root, val):
            if not root: return 0
            
            val = val * 10 + root.val
            
            if not root.left and not root.right: return val
            
            return dfs(root.left, val) + dfs(root.right, val)
        
        return dfs(root, 0)
    
    