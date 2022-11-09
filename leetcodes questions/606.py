class Solution(object):
    def tree2str(self, root):
        if not root: return ''        
        res  = []
        def dfs(root):
            if not root: return
            res.append('(')
            res.append(str(root.val))
            
            if not root.left and root.right:
                res.append('()')
                
            left = dfs(root.left)
            right = dfs(root.right)
            
            res.append(')')

        dfs(root)
        return ''.join(res)[1:-1]